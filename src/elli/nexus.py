"""Read and write NeXus files."""
import h5py
import numpy as np
import pandas as pd

from .utils import calc_rho


def read_psi_delta(nxs_filename: str) -> pd.DataFrame:
    """Read a NeXus file containing Psi and Delta data.

    Args:
        nxs_filename (str): The filename of the NeXus file.

    Raises:
        ValueError: Is raised when the data is not stored as psi / delta value.

    Returns:
        pd.DataFrame: Psi/Delta DataFrame
    """
    h5file = h5py.File(nxs_filename, "r")
    if h5file["entry/sample/data_type"][()].decode("utf-8") != "psi / delta":
        raise ValueError("Data type is not psi / delta")

    wavelength = np.array(h5file["entry/sample/wavelength"])
    psi = np.array(h5file["entry/sample/measured_data"])[:, 0, 0, 0, 0]
    delta = np.array(h5file["entry/sample/measured_data"])[:, 1, 0, 0, 0]

    df = pd.DataFrame({"Ψ": psi, "Δ": delta}, index=wavelength / 10)
    df.index.name = "Wavelength"
    return df


def read_rho(nxs_filename: str) -> pd.DataFrame:
    """Reads rho value from NeXus datafile.
    Currently, this works only with psi / delta representation in the NeXus file.

    Raises:
        ValueError: Is raised when the data is not stored as psi / delta value.

    Returns:
        pd.DataFrame: DataFrame containing the measured data as imaginary rho value.
    """
    return calc_rho(read_psi_delta(nxs_filename))
