"""A helper class to load data from SpectraRay ASCII Files.
It only supplies a rundimentary loading of standard psi/delta values
and misses some other features.
"""
import pandas as pd
from .dispersions.dispersions import TableEpsilon
from .utils import calc_rho
from .math import conversion_wavelength_energy


class SpectraRay:
    """Helper class to load spectraray ascii files into
    pyEllis pandas format."""

    def __init__(self, path: str) -> None:
        self.spectraray_path = path

    def loadDispersionTable(self, fname: str) -> TableEpsilon:
        """Load a dispersion table from a ascii file
        in the spectraray materials ascii format.
        This only accounts for tabulated dielectric function data.
        Spectraray also stores dispersion data in other formats,
        but this function is not able to read these other formats.

        Args:
            fname (str): The filename of the spectraray ascii file.

        Returns:
            TableEpsilon: A dispersion class containing the tabulated data.
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

    @staticmethod
    def read_psi_delta_file(fname: str, decimal: str = ".") -> pd.DataFrame:
        """Read a psi/delta spectraray ascii file.
        Only reads the first entry and does not support reading multiple angles.
        For multiple angles you have to save the data in multiple files.

        Args:
            fname (str): Filename of the measurement ascii file.
            decimal (str, optional): Decimal separator in the datafile. Defaults to ".".

        Returns:
            pd.DataFrame: DataFrame containing the psi/delta data in
            the format to be further processes inside pyElli.
        """
        psi_delta = pd.read_csv(
            fname,
            index_col=0,
            sep=r"\s+",
            decimal=decimal,
            usecols=[0, 1, 2],
            names=["Wavelength", "Ψ", "Δ"],
            skiprows=1,
        )

        psi_delta.loc[:, "Δ"] = psi_delta.loc[:, "Δ"].where(
            psi_delta.loc[:, "Δ"] <= 180, psi_delta.loc[:, "Δ"] - 360
        )

        return psi_delta

    @staticmethod
    def read_mmatrix(fname: str, decimal: str = ".") -> pd.DataFrame:
        """Read a mueller matrix spectraray ascii file.
        Only reads the first entry and does not support reading multiple angles.
        For multiple angles you have to save the data in multiple files.

        Args:
            fname (str): Filename of the measurement ascii file.
            decimal (str, optional): Decimal separator in the datafile. Defaults to ".".

        Returns:
            pd.DataFrame: DataFrame containing the psi/delta data in
            the format to be further processes inside pyElli.
        """
        mueller_matrix = pd.read_csv(
            fname, sep=r"\s+", decimal=decimal, index_col=0
        ).iloc[:, -17:-1]
        mueller_matrix.index.name = "Wavelength"
        mueller_matrix.columns = [
            "M11",
            "M12",
            "M13",
            "M14",
            "M21",
            "M22",
            "M23",
            "M24",
            "M31",
            "M32",
            "M33",
            "M34",
            "M41",
            "M42",
            "M43",
            "M44",
        ]

        return mueller_matrix

    @staticmethod
    def read_rho(fname: str, decimal: str = ".") -> pd.DataFrame:
        """Read a psi/delta spectraray ascii file and converts it to rho values.
        Only reads the first entry and does not support reading multiple angles.
        For multiple angles you have to save the data in multiple files.

        Args:
            fname (str): Filename of the measurement ascii file.
            decimal (str, optional): Decimal separator in the datafile. Defaults to ".".

        Returns:
            pd.DataFrame: DataFrame containing the rho data in
            the format to be further processes inside pyElli.
        """
        psi_delta = SpectraRay.read_psi_delta_file(fname, decimal)
        return calc_rho(psi_delta)
