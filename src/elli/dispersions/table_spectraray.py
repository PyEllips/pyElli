# Encoding: utf-8
"""Helper class to load spectraray's tabulated dielectric functions."""
import pandas as pd

from ..utils import conversion_wavelength_energy
from .table_epsilon import TableEpsilon


class TableSpectraRay:
    """Helper class to load spectraray's tabulated dielectric functions."""

    def __init__(self, path: str) -> None:
        """
        Args:
            path (str): Defines the folder where the Spectraray files are saved.
        """
        self.spectraray_path = path

    def load_dispersion_table(self, fname: str) -> TableEpsilon:
        """Load a dispersion table from a ascii file
        in the spectraray materials ascii format.
        This only accounts for tabulated dielectric function data.
        Spectraray also stores dispersion data in other formats,
        but this function is not able to read these other formats.

        Args:
            fname (str): The filename of the spectraray ascii file.

        Returns:
            TableEpsilon: A dispersion object containing the tabulated data.
        """
        start = 0
        stop = 0
        with open(self.spectraray_path + fname, "r", encoding="utf8") as file:
            line = file.readline()
            cnt = 0
            while line:
                if line.strip() == "Begin of array":
                    start = cnt + 1
                if line.strip() == "End of array":
                    stop = cnt
                line = file.readline()
                cnt += 1

                if line.startswith("Units="):
                    x_unit = line.split("=")[1].split(",")[0]

        df = pd.read_csv(
            self.spectraray_path + fname,
            delim_whitespace=True,
            skiprows=start,
            nrows=stop - start,
            index_col=0,
            usecols=[0, 1, 2],
            names=[x_unit, "ϵ1", "ϵ2"],
        )

        if x_unit == "Wavelength":
            return TableEpsilon(
                lbda=df.index, epsilon=df.loc[:, "ϵ1"] + 1j * df.iloc[:, "ϵ2"]
            )
        return TableEpsilon(
            lbda=conversion_wavelength_energy(df.index),
            epsilon=df.loc[:, "ϵ1"] + 1j * df.loc[:, "ϵ2"],
        )
