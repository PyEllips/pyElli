"""
A helper class to load data from Woollam ASCII Files.
It supports loading of standard psi/delta values.
"""
from typing import TextIO
import re
import logging

from pint import UndefinedUnitError, DimensionalityError
import pandas as pd

from ..units import ureg
from ..utils import calc_rho

logger = logging.getLogger(__name__)


def is_wvase_tabular(line: str) -> bool:
    """
    Checks whether the provided line is in wvase tabular layout.

    Args:
        line (str): The line to check

    Returns:
        bool: True if the line is in wvase tabular layout.
    """
    return bool(re.search(r"^(\d+\.\d+\t){5}\d+\.\d+$", line))


def is_complete_ease_tabular(line: str) -> bool:
    """
    Checks whether the provided line is in complete ease tabular layout.

    Args:
        line (str): The line to check

    Returns:
        bool: True if the line is in complete ease tabular layout.
    """
    return bool(re.search(r"^[a-zA-Z]+\t(\d+\.\d+\t){5}\d+\.\d+$", line))


def scale_to_nm(unit: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Scales the wavelength axis of the given dataframe from the
    provided unit to nm.

    Args:
        unit (str): The unit string. Should be pint compatible.
        dataframe (pd.DataFrame): The dataframe which axis should be scaled.

    Returns:
        pd.DataFrame: The dataframe with scaled wavelength axis.
    """
    try:
        scaling = ureg(unit).to("nm").magnitude
        dataframe.index = dataframe.index.set_levels(
            dataframe.index.levels[1] * scaling, level=1
        )

        return dataframe
    except UndefinedUnitError:
        logger.warning(
            "Unrecognized unit %s. "
            "The wavelength axis may not be scaled appropriately.",
            unit,
        )
        return dataframe
    except DimensionalityError:
        logger.warrning(
            "Unit %s is not a valid wavelength unit. "
            "The wavelength axis may not be scaled appropriately.",
            unit,
        )
        return dataframe


def read_wvase_dataframe(file_object: TextIO) -> pd.DataFrame:
    """
    Reads a wvase formated table from a TextIO file object.
    The pointer of the file object should point to the first line
    of the data table.

    Args:
        file_object (TextIO): The file object containing the wvase table.

    Returns:
        pd.DataFrame:
            Dataframe containing the psi/delta values.
            Ready to be further processed by pyElli.
    """
    dframe = pd.read_csv(
        file_object,
        sep="\t",
        header=None,
        names=["Ψ", "Δ", "Ψ_err", "Δ_err"],
        index_col=(1, 0),
    )
    dframe.index.names = ("Angle of Incidence", "Wavelength")
    return dframe


def read_complete_ease_dataframe(file_object: TextIO) -> pd.DataFrame:
    """
    Reads a complete ease formated table from a TextIO file object.
    The pointer of the file object should point to the first line
    of the data table.

    Args:
        file_object (TextIO): The file object containing the complete ease table.

    Returns:
        pd.DataFrame:
            Dataframe containing the psi/delta values.
            Ready to be further processed by pyElli.
    """
    dframe = pd.read_csv(file_object, sep="\t", header=None, index_col=(2, 1))
    dframe = dframe[dframe[0] == "E"]
    dframe = dframe.iloc[:, 1:]
    dframe.index.names = ("Angle of Incidence", "Wavelength")
    dframe.columns = ["Ψ", "Δ", "Ψ_err", "Δ_err"]
    return dframe


def read_woollam_psi_delta(fname: str) -> pd.DataFrame:
    r"""Read a psi/delta woollam ascii file.

    Args:
        fname (str): Filename of the measurement ascii file.

    Returns:
        pd.DataFrame: DataFrame containing the psi/delta data in
        the format to be further processes inside pyElli.
    """

    with open(fname, encoding="utf-8") as fobj:
        line_number = fobj.tell()
        metadata = []
        file_format = ""
        line = fobj.readline()
        while line:
            if is_wvase_tabular(line):
                line_number = fobj.tell()
                file_format = "wvase"
                break
            if is_complete_ease_tabular(line):
                line_number = fobj.tell()
                file_format = "complete_ease"
                break
            metadata.append(line)
            line = fobj.readline()
        fobj.seek(line_number)

        if not line:
            raise ValueError(f"Invalid file format for {fname}")

        reader_map = {
            "wvase": read_wvase_dataframe,
            "complete_ease": read_complete_ease_dataframe,
        }

        if file_format not in reader_map:
            raise ValueError(f"Invalid file format {file_format} for file {fname}")
        data = reader_map.get(file_format)(fobj)

    data = scale_to_nm(metadata[-1], data)
    return data.iloc[:, :-2]


def read_woollam_rho(fname: str) -> pd.DataFrame:
    r"""Read a psi/delta woollam ascii file and converts it to rho values.

    Args:
        fname (str): Filename of the measurement ascii file.

    Returns:
        pd.DataFrame: DataFrame containing the rho data in
        the format to be further processes inside pyElli.
    """
    psi_delta = read_woollam_psi_delta(fname)
    return calc_rho(psi_delta)