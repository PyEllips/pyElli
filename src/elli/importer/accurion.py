"""A helper class to load data from Accurion EP4 DAT files.
Typical files look like: Si3N4_on_4inBF33_W03_20240905-105631.ds.dat
"""

import numpy as np
import pandas as pd

from ..utils import convert_delta_range
from . import detect_encoding


def read_accurion_psi_delta(fname: str) -> pd.DataFrame:
    r"""Read a psi/delta Accurion dat file.

    Args:
      fname (str): Filename of the measured dat file

    Returns:
      pd.DataFrame: DataFrame containing the psi/delta data in the pyElli-compatible format.
    """
    encoding = detect_encoding(fname)
    psi_delta_df = pd.read_csv(
        fname, delimiter="\t", encoding=encoding, skiprows=0, header=0
    )[1:].astype(float)
    psi_delta_df = psi_delta_df.reindex(columns=list(["AOI", "Lambda", "Delta", "Psi"]))
    psi_delta_df = psi_delta_df.rename(
        columns={
            "AOI": "Angle of Incidence",
            "Lambda": "Wavelength",
            "Delta": "Δ",
            "Psi": "Ψ",
        }
    )
    psi_delta_df = psi_delta_df.groupby(["Angle of Incidence", "Wavelength"]).sum()

    # wrap delta range
    psi_delta_df.loc[:, "Δ"] = convert_delta_range(psi_delta_df.loc[:, "Δ"], -180, 180)

    return psi_delta_df
