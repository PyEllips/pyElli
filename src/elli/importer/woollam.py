"""
A helper class to load data from Woollam ASCII Files.
It supports loading of standard psi/delta values.
"""

import logging
import re
from typing import TextIO, Union

import pandas as pd
from pint import DimensionalityError, UndefinedUnitError

from ..units import ureg
from ..utils import calc_rho
from . import detect_encoding

logger = logging.getLogger(__name__)


is_float_regex = re.compile(r"[+-]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)")


def is_float(line: Union[float, int, str]) -> bool:
    """Checks whether the given line is a float

    Args:
        line (str): The line presumably containing a float

    Returns:
        bool: True if it is a float, False otherwise
    """
    if isinstance(line, (float, int)):
        return True
    if isinstance(line, str):
        return bool(is_float_regex.search(line))
    return False


def _is_wvase_tabular(line: str) -> bool:
    """
    Checks whether the provided line is in wvase tabular layout.

    Args:
        line (str): The line to check

    Returns:
        bool: True if the line is in wvase tabular layout.
    """
    return bool(re.search(r"^(\d*\.\d*\s+){5}\d*\.\d*$", line))


def _is_complete_ease_tabular(line: str) -> bool:
    """
    Checks whether the provided line is in complete ease tabular layout.

    Args:
        line (str): The line to check

    Returns:
        bool: True if the line is in complete ease tabular layout.
    """
    return bool(re.search(r"^[a-zA-Z]+\s+(\d+\.\d+\s+){5}\d+\.\d+$", line))


def _is_tan_cos_format(line: str) -> bool:
    """
    Checks whether the line denotes a wvase tan/cos format.

    Args:
        line (str): The line to check

    Returns:
        bool: True if the line is of the format {unit} TRIG.
    """
    return bool(re.search(r"^[a-zA-Z]+\s+TRIG", line))


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
            dataframe.index.levels[1].astype(float) * scaling, level=1
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
        logger.warning(
            "Unit %s is not a valid wavelength unit. "
            "The wavelength axis may not be scaled appropriately.",
            unit,
        )
        return dataframe


def _read_wvase_dataframe(file_object: TextIO) -> pd.DataFrame:
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
        names=["Wavelength", "Angle of Incidence", "Ψ", "Δ", "Ψ_err", "Δ_err"],
    )

    dframe = (
        dframe[dframe.apply(lambda x: is_float(x.iloc[0]), axis=1)]
        .set_index(["Wavelength", "Angle of Incidence"])
        .swaplevel(0, 1)
    )
    return dframe


def _read_complete_ease_dataframe(file_object: TextIO) -> pd.DataFrame:
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

    encoding = detect_encoding(fname)

    with open(fname, encoding=encoding) as fobj:
        line_number = fobj.tell()
        metadata = []
        file_format = ""
        line = fobj.readline()
        while line:
            if _is_wvase_tabular(line):
                line_number = fobj.tell()
                file_format = "wvase"
                break
            if _is_complete_ease_tabular(line):
                line_number = fobj.tell()
                file_format = "complete_ease"
                break
            if _is_tan_cos_format(line):
                raise NotImplementedError(
                    "The wvase Tan(Psi)/Cos(Delta) format is not supported. "
                    "Please try using wvase's psi/delta format."
                )
            metadata.append(line)
            line = fobj.readline()
        fobj.seek(line_number)

        if not line:
            raise ValueError(f"Invalid file format for {fname}")

        reader_map = {
            "wvase": _read_wvase_dataframe,
            "complete_ease": _read_complete_ease_dataframe,
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
