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

from .base_dispersion import Dispersion
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

        self.catalog = pd.DataFrame(entries)

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

        if yml_file["DATA"][0]["type"] == "tabulated nk":
            df = pd.read_table(
                io.StringIO(yml_file["DATA"][0]["data"]),
                sep="\\s+",
                names=["Wavelength", "n", "k"],
            )
            df["Wavelength"] = df["Wavelength"] * 1000
            df.set_index("Wavelength", inplace=True)
        else:
            raise ValueError("Unimplemented Format.")

        return Table(lbda=df.index, n=df["n"] + 1j * df["k"])
