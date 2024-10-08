"""A helper class to load data from Accurion EP4 DAT files.
Typical files look like: Si3N4_on_4inBF33_W03_20240905-105631.ds.dat
"""

import numpy as np
import pandas as pd
import xarray as xr

from elli.utils import calc_rho

from . import detect_encoding


def read_accurion(fname: str) -> xr.Dataset:
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
            "AOI": "Angle_of_Incidence",
            "Lambda": "Wavelength",
            "Delta": "delta",
            "Psi": "psi",
        }
    )
    psi_delta_df = psi_delta_df.groupby(["Angle_of_Incidence", "Wavelength"]).sum()

    # wrap delta range
    psi_delta_df.loc[:, "delta"] = psi_delta_df.loc[:, "delta"].where(
        psi_delta_df.loc[:, "delta"] <= 180, psi_delta_df.loc[:, "delta"] - 360
    )

    return calc_rho(psi_delta_df.to_xarray())
