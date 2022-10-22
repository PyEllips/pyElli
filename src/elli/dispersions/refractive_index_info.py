# Encoding: utf-8
"""Helper classes to use the refractiveindex.info database.

For now the database from https://github.com/polyanskiy/refractiveindex.info-database
needs to be downloaded manually.

After initialization the Class provides a dataframe at DatabaseRII.catalog .
It can be searched similar to catalog.loc[catalog['book']=='Ag'] .
"""

import io
import os
from collections import namedtuple
from typing import Tuple

from importlib_resources import files
import pandas as pd
import yaml
from rapidfuzz import process

from .base_dispersion import Dispersion, DispersionSum
from .table_index import Table

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
        "page_longname",
        "path",
    ],
)


class DatabaseRII:
    """Helper class to load tabulated dielectric functions from the refractiveindex.info database."""

    def __init__(self) -> None:
        self.rii_path = files("elli.refractiveindexinfo-database.database")

        yml_file = yaml.load(
            self.rii_path.joinpath("library.yml").read_text(), yaml.SafeLoader
        )

        entries = []
        for sh in yml_file:
            b_div = pd.NA
            for b in sh["content"]:
                if "DIVIDER" not in b:
                    p_div = pd.NA
                    for p in b["content"]:
                        if "DIVIDER" not in p:
                            entries.append(
                                nt_entry(
                                    sh["SHELF"],
                                    sh["name"],
                                    b_div,
                                    b["BOOK"],
                                    b["name"],
                                    p["PAGE"],
                                    p_div,
                                    p["name"],
                                    os.path.join("data", os.path.normpath(p["data"])),
                                )
                            )
                        else:
                            p_div = p["DIVIDER"]
                else:
                    b_div = b["DIVIDER"]

        self.catalog = pd.DataFrame(entries, dtype=pd.StringDtype())
        self.books = self.catalog["book"].unique().tolist()
        self.book_longnames = self.catalog["book_longname"].unique().tolist()
        self.pages = self.catalog["page"].unique().tolist()

    def search_material(
        self, query: str, fuzzy: bool = False, longname: bool = False
    ) -> pd.DataFrame:
        """Search the catalog by the query string in the book field.
        Optionally able to search approximate entries and the book_longname field.

        Args:
            query (str): String to search.
            fuzzy (bool, optional): Search approximate entries. Defaults to False.
            longname (bool, optional): Search book_longname instead. Defaults to False.

        Returns:
            pd.DataFrame: Filtered Catalog dataframe.
        """

        if longname:
            name_list = "book_longnames"
            subcatalog = "book_longname"
        else:
            name_list = "books"
            subcatalog = "book"

        return self._search(query, name_list, subcatalog, fuzzy)

    def search_source(self, query: str, fuzzy: bool = False) -> pd.DataFrame:
        """Search the catalog by the query string in the page field.
        Optionally able to search approximate entries.

        Args:
            query (str): String to search.
            fuzzy (bool, optional): Search approximate entries. Defaults to False.

        Returns:
            pd.DataFrame: Filtered Catalog dataframe.
        """
        return self._search(query, "pages", "page", fuzzy)

    def _search(
        self, query: str, name_list: str, subcatalog: str, fuzzy: bool
    ) -> pd.DataFrame:
        if fuzzy:
            suggestions = process.extract(
                query, getattr(self, name_list), limit=10, score_cutoff=80
            )

            if len(suggestions) == 0:
                return self.catalog.loc[self.catalog[subcatalog] == ""]

            result = pd.concat(
                [
                    self.catalog.loc[self.catalog[subcatalog] == s]
                    for s, _, _ in suggestions
                ]
            )

        else:
            result = self.catalog.loc[self.catalog[subcatalog] == query]

        return result

    def load_dispersion(self, entry: Tuple[str, str]) -> Dispersion:
        """Load a dispersion from the refractive index database.
        Selection by tuple of material and source.

        Args:
            entry (Tuple[str, str]): Tuple of material and source to select an entry.
                E.g. ('Au', 'Johnson').

        Returns:
            Dispersion: A dispersion object containing the tabulated data.
        """
        index = self.catalog.loc[
            (self.catalog["book"] == entry[0]) & (self.catalog["page"] == entry[1])
        ].index

        if len(index) == 1:
            return self.load_dispersion_index(index[0])
        else:
            raise ValueError("No entry found.")

    def load_dispersion_index(self, index: int) -> Dispersion:
        """Load a dispersion from the refractive index database.
        Currently only tabulated data is supported.

        Args:
            index (int): The index of the dispersion in the catalog.

        Returns:
            Dispersion: A dispersion object containing the tabulated data.
        """
        yml_file = yaml.load(
            self.rii_path.joinpath(self.catalog.loc[index]["path"]).read_text(),
            yaml.SafeLoader,
        )

        dispersion_list = []

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

            elif dispersion_relation["type"] == "tabulated n":
                df = pd.read_table(
                    io.StringIO(dispersion_relation["data"]),
                    sep="\\s+",
                    names=["Wavelength", "n"],
                )
                df["Wavelength"] = df["Wavelength"] * 1000
                df.set_index("Wavelength", inplace=True)

                dispersion = Table(lbda=df.index, n=df["n"])

            elif dispersion_relation["type"] == "tabulated k":
                df = pd.read_table(
                    io.StringIO(dispersion_relation["data"]),
                    sep="\\s+",
                    names=["Wavelength", "k"],
                )
                df["Wavelength"] = df["Wavelength"] * 1000
                df.set_index("Wavelength", inplace=True)

                dispersion = Table(lbda=df.index, n=0 + 1j * df["k"])

            else:
                raise ValueError("Unimplemented Format.")

            dispersion_list.append(dispersion)

        if len(dispersion_list) == 1:
            return dispersion_list[0]
        else:
            return DispersionSum(*dispersion_list)
