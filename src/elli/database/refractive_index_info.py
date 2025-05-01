# Encoding: utf-8
"""Helper class to use the refractiveindex.info database."""

import io
import os
import re
from collections import namedtuple
from typing import List, Tuple, Union

import numpy as np
import pandas as pd
import yaml
from importlib_resources import files
from rapidfuzz import process

from ..dispersions import (
    CauchyCustomExponent,
    EpsilonInf,
    Polynomial,
    Sellmeier,
    SellmeierCustomExponent,
    Table,
)
from ..dispersions.base_dispersion import (
    Dispersion,
    DispersionSum,
    IndexDispersion,
    IndexDispersionSum,
)
from ..materials import IsotropicMaterial

WavelengthFilterType = Union[
    None, float, int, List[Union[float, int]], Tuple[Union[float, int]]
]

nt_entry = namedtuple(
    "Entry",
    [
        "shelf",
        "shelf_longname",
        "book_divider",
        "book",
        "book_longname",
        "page",
        "page_type",
        "author",
        "year",
        "comment",
        "lower_range",
        "upper_range",
        "path",
    ],
)


class RII:
    """Helper class to load tabulated dielectric functions from the https://refractiveindex.info database.

    The database object has to be initialized to load the entire catalog:

    .. highlight:: python
    .. code-block:: python

        RII = elli.db.RII()

    After initialization the Class provides a dataframe with all entries at RII.catalog,
    it follows the naming schema used on the website: Entries are categorized by Shelf, Book and Page.

    Shelfs are broad categories (inorganics, organics, glasses, other), and ignored in the following.

    Book and Page are used to access entries with this helper:
    For inorganic and organic materials 'book' uses the sum formula of the compound and
    'page' is an identifier of the author of the publication.
    In the case of glasses, book is the manufacturer and page the name of the glass.

    Materials can be searched by the RII.search() method.
    Specific fields can be searched by providing a column keyword:

    .. highlight:: python
    .. code-block:: python

        RII.search("Aspnes", column="author")

    Dispersions or respective materials can be loaded by calling these methods:

    .. highlight:: python
    .. code-block:: python

        gold_material = RII.get_mat("Au", "Johnson")
        gold_dispersion = RII.get_dispersion("Au", "Johnson")
    """

    def __init__(self) -> None:
        self.rii_path = files("elli.database.refractiveindexinfo-database.database")

        with open(self.rii_path.joinpath("catalog-nk.yml"), "r", encoding="utf8") as f:
            yml_file = yaml.load(f, yaml.SafeLoader)

        pagename_pattern = re.compile(
            r"(?P<authors>.*) "
            r"(?P<year>\d{4})[^:]*?: "
            r"((?P<comment1>.*); )?"
            r"(?P<type1>.+) (?P<lower_range1>\d+(\.\d*)?(e\W?\d+)?)\W(?P<upper_range1>\d+(\.\d*)?(e\W?\d+)?) µm"
            r"(, (?P<type2>.+) (?P<lower_range2>\d+(\.\d*)?(e\W?\d+)?).(?P<upper_range2>\d+(\.\d*)?(e\W?\d+)?) µm)?"
            r"(; (?P<comment2>.*))?"
        )

        entries = []
        for sh in yml_file:
            b_div = pd.NA
            for b in sh["content"]:
                if "DIVIDER" not in b:
                    p_div = pd.NA
                    for p in b["content"]:
                        if "DIVIDER" not in p:
                            infos = pagename_pattern.match(p["name"])
                            if infos is None:
                                entries.append(
                                    nt_entry(
                                        sh["SHELF"],
                                        sh["name"],
                                        b_div,
                                        b["BOOK"],
                                        b["name"],
                                        p["PAGE"],
                                        p_div,
                                        None,
                                        None,
                                        p["name"],
                                        None,
                                        None,
                                        os.path.join(
                                            "data-nk", os.path.normpath(p["data"])
                                        ),
                                    )
                                )
                            else:
                                entries.append(
                                    nt_entry(
                                        sh["SHELF"],
                                        sh["name"],
                                        b_div,
                                        b["BOOK"],
                                        b["name"],
                                        p["PAGE"],
                                        p_div,
                                        infos.group("authors"),
                                        infos.group("year"),
                                        " ".join(
                                            filter(
                                                None,
                                                (
                                                    infos.group("comment1"),
                                                    infos.group("comment2"),
                                                ),
                                            )
                                        ),
                                        infos.group("lower_range1"),
                                        infos.group("upper_range1"),
                                        os.path.join(
                                            "data-nk", os.path.normpath(p["data"])
                                        ),
                                    )
                                )
                        else:
                            p_div = p["DIVIDER"]
                else:
                    b_div = b["DIVIDER"]

        self.catalog = pd.DataFrame(entries, dtype=pd.StringDtype())

        self.catalog["year"] = pd.to_numeric(
            self.catalog["year"], errors="coerce"
        ).convert_dtypes()
        self.catalog["lower_range"] = 1000 * pd.to_numeric(
            self.catalog["lower_range"], errors="coerce"
        )
        self.catalog["upper_range"] = 1000 * pd.to_numeric(
            self.catalog["upper_range"], errors="coerce"
        )

        book_div = self.catalog["book_divider"].drop_duplicates().dropna().values
        books = self.catalog["book"].drop_duplicates().dropna().values
        book_longnames = self.catalog["book_longname"].drop_duplicates().dropna().values
        pages = self.catalog["page"].drop_duplicates().dropna().values
        authors = self.catalog["author"].drop_duplicates().dropna().values
        comments = self.catalog["comment"].drop_duplicates().dropna().values

        self._filter_lists = {
            "book_divider": book_div,
            "book": books,
            "book_longname": book_longnames,
            "page": pages,
            "author": authors,
            "comment": comments,
        }

    def search(
        self,
        query: Union[str, List[str]],
        column: Union[str, List[str]] = "all",
        wavelength_filter: WavelengthFilterType = None,
        fuzzy: bool = True,
    ) -> pd.DataFrame:
        """Search the catalog by the query string in the requested column.

        Args:
            query (str, List[str]): String or list of strings to search.
            column (str, optional): Column-strings or list of strings to search.
            wavelength_filter (float, int, List[float, int]): Wavelengths in nm included in the results. Default to None.
            fuzzy (bool, optional): Search approximate entries. Defaults to True.

        Returns:
            pd.DataFrame: Filtered Catalog dataframe.
        """
        if isinstance(query, str):
            query = [query]

        if column == "all":
            if fuzzy:
                column = list(self._filter_lists.keys())
            else:
                column = self.catalog.columns
        elif isinstance(column, str):
            column = [column]

        index = self.catalog["shelf"] == ""

        for col in column:
            for q in query:
                if fuzzy:
                    suggestions = process.extract(
                        q, self._filter_lists[col], limit=10, score_cutoff=80
                    )

                    for s, _, _ in suggestions:
                        index = np.logical_or(index, self.catalog[col] == s)

                else:
                    index = np.logical_or(index, self.catalog[col] == q)

        result = self.catalog.loc[index]

        if wavelength_filter is None:
            return result
        elif isinstance(wavelength_filter, (int, float)):
            return result.loc[
                (result.lower_range <= wavelength_filter)
                & (result.upper_range >= wavelength_filter)
            ]
        elif isinstance(wavelength_filter, (list, tuple, np.ndarray)):
            for wl in wavelength_filter:
                result = result.loc[
                    (result["lower_range"] <= wl) & (result["upper_range"] >= wl)
                ]
            return result
        else:
            raise (
                ValueError(
                    "Wavelength_filter only takes numeric values or a list of numeric values."
                )
            )

    def get_mat(self, book: str, page: str) -> IsotropicMaterial:
        """Load a dispersion from the refractive index database and generates an isotropic material.
        Selection by material and source identifiers.

        Args:
            book (str): Name of the Material, named 'Book' on the website and the database. E.g. 'Au'
            page (str): Name of the Source, named 'Page' on the website and the database. E.g. 'Johnson'

        Returns:
            IsotropicMaterial: A material object build from the tabulated dispersion data.
        """
        return IsotropicMaterial(self.get_dispersion(book, page))

    def get_dispersion(
        self, book: str, page: str
    ) -> Union[Dispersion, IndexDispersion]:
        """Load a dispersion from the refractive index database.
        Selection by material and source identifiers.

        Args:
            book (str): Name of the Material, named 'Book' on the website and the database. E.g. 'Au'
            page (str): Name of the Source, named 'Page' on the website and the database. E.g. 'Johnson'

        Returns:
            Dispersion: A dispersion object containing the tabulated data.
        """

        index = self.catalog.loc[
            (self.catalog["book"] == book) & (self.catalog["page"] == page)
        ].index

        if len(index) != 1:
            raise ValueError("No entry found.")

        yml_file = yaml.load(
            self.rii_path.joinpath(self.catalog.loc[index[0]]["path"]).read_text(),
            yaml.SafeLoader,
        )

        dispersion_list = []
        contains_index_dispersion = False

        for dispersion_relation in yml_file["DATA"]:
            if dispersion_relation["type"] == "tabulated nk":
                df = pd.read_table(
                    io.StringIO(dispersion_relation["data"]),
                    sep="\\s+",
                    names=["Wavelength", "n", "k"],
                )
                df["Wavelength"] = df["Wavelength"] * 1000
                df.set_index("Wavelength", inplace=True)

                dispersion = Table(lbda=df.index, n=df["n"] + 1j * df["k"])
                contains_index_dispersion = True

            elif dispersion_relation["type"] == "tabulated n":
                df = pd.read_table(
                    io.StringIO(dispersion_relation["data"]),
                    sep="\\s+",
                    names=["Wavelength", "n"],
                )
                df["Wavelength"] = df["Wavelength"] * 1000
                df.set_index("Wavelength", inplace=True)

                dispersion = Table(lbda=df.index, n=df["n"])
                contains_index_dispersion = True

            elif dispersion_relation["type"] == "tabulated k":
                df = pd.read_table(
                    io.StringIO(dispersion_relation["data"]),
                    sep="\\s+",
                    names=["Wavelength", "k"],
                )
                df["Wavelength"] = df["Wavelength"] * 1000
                df.set_index("Wavelength", inplace=True)

                dispersion = Table(lbda=df.index, n=0 + 1j * df["k"])
                contains_index_dispersion = True

            elif dispersion_relation["type"] == "formula 1":
                coeffs = list(
                    map(float, dispersion_relation["coefficients"].split(" "))
                )
                a = coeffs[slice(1, len(coeffs), 2)]
                b = coeffs[slice(2, len(coeffs), 2)]

                sell = Sellmeier()
                for a_i, b_i in zip(a, b):
                    sell.add(a_i, b_i**2)

                dispersion = sell + EpsilonInf(coeffs[0])

            elif dispersion_relation["type"] == "formula 2":
                coeffs = list(
                    map(float, dispersion_relation["coefficients"].split(" "))
                )
                a = coeffs[slice(1, len(coeffs), 2)]
                b = coeffs[slice(2, len(coeffs), 2)]

                sell = Sellmeier()
                for a_i, b_i in zip(a, b):
                    sell.add(a_i, b_i)

                dispersion = sell + EpsilonInf(coeffs[0])

            elif dispersion_relation["type"] == "formula 3":
                coeffs = list(
                    map(float, dispersion_relation["coefficients"].split(" "))
                )
                f = coeffs[slice(1, len(coeffs), 2)]
                e = coeffs[slice(2, len(coeffs), 2)]

                poly = Polynomial(coeffs[0])
                for f_i, e_i in zip(f, e):
                    poly.add(f_i / 1e3**e_i, e_i)

                dispersion = poly

            elif dispersion_relation["type"] == "formula 4":
                coeffs = list(
                    map(float, dispersion_relation["coefficients"].split(" "))
                )
                a = coeffs[slice(1, 6, 4)]
                e1 = coeffs[slice(2, 7, 4)]
                b = coeffs[slice(3, 8, 4)]
                e2 = coeffs[slice(4, 9, 4)]
                f = coeffs[slice(9, len(coeffs), 2)]
                e = coeffs[slice(10, len(coeffs), 2)]

                poly = Polynomial(coeffs[0])
                sell = SellmeierCustomExponent()

                for a_i, e1_i, b_i, e2_i in zip(a, e1, b, e2):
                    sell.add(a_i, e1_i, b_i, e2_i)

                for f_i, e_i in zip(f, e):
                    poly.add(f_i / 1e3**e_i, e_i)

                dispersion = poly + sell

            elif dispersion_relation["type"] == "formula 5":
                coeffs = list(
                    map(float, dispersion_relation["coefficients"].split(" "))
                )
                f = coeffs[slice(1, len(coeffs), 2)]
                e = coeffs[slice(2, len(coeffs), 2)]

                cauchy = CauchyCustomExponent(coeffs[0])
                for f_i, e_i in zip(f, e):
                    cauchy.add(f_i / 1e3**e_i, e_i)

                dispersion = cauchy
                contains_index_dispersion = True

            else:
                raise ValueError("Unimplemented Format.")

            dispersion_list.append(dispersion)

        if len(dispersion_list) == 1:
            return dispersion_list[0]

        if contains_index_dispersion:
            for i, dispersion in enumerate(dispersion_list):
                if not isinstance(dispersion, IndexDispersion):
                    dispersion_list[i] = dispersion.as_index()

            return IndexDispersionSum(*dispersion_list)
        return DispersionSum(*dispersion_list)

    def get_reference(self, book: str, page: str) -> str:
        """Reads the reference information from the selected dispersion.

        Args:
            book (str): Name of the Material, named 'Book' on the website and the database. E.g. 'Au'
            page (str): Name of the Source, named 'Page' on the website and the database. E.g. 'Johnson'

        Returns:
            str: Reference information.
        """

        index = self.catalog.loc[
            (self.catalog["book"] == book) & (self.catalog["page"] == page)
        ].index

        if len(index) != 1:
            raise ValueError("No entry found.")

        yml_file = yaml.load(
            self.rii_path.joinpath(self.catalog.loc[index[0]]["path"]).read_text(),
            yaml.SafeLoader,
        )

        return yml_file["REFERENCES"]

    def get_comment(self, book: str, page: str) -> str:
        """Reads the measurement/calculation information of the selected dispersion.

        Args:
            book (str): Name of the Material, named 'Book' on the website and the database. E.g. 'Au'
            page (str): Name of the Source, named 'Page' on the website and the database. E.g. 'Johnson'

        Returns:
            str: Dispersion information.
        """

        index = self.catalog.loc[
            (self.catalog["book"] == book) & (self.catalog["page"] == page)
        ].index

        if len(index) != 1:
            raise ValueError("No entry found.")

        yml_file = yaml.load(
            self.rii_path.joinpath(self.catalog.loc[index[0]]["path"]).read_text(),
            yaml.SafeLoader,
        )

        return yml_file["COMMENTS"]
