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
    pd.DataFrame: Psi/Delta DataFrame.
        The index is a multiindex consisting of the angle of incidents as first column
        and the wavlength as second column.
    """
    h5file = h5py.File(nxs_filename, "r")
    if h5file["entry/sample/data_type"][()].decode("utf-8") != "psi / delta":
        raise ValueError("Data type is not psi / delta")

    aois = np.array(h5file["entry/instrument/angle_of_incidence"])
    wavelength = np.array(h5file["entry/sample/wavelength"]) / 10
    psi_delta_df = pd.DataFrame(
        {},
        columns={"Ψ", "Δ"},
        index=pd.MultiIndex.from_product(
            [aois, wavelength], names=["Angle of Incidence", "Wavelength"]
        ),
    )

    data = np.array(h5file["/entry/sample/measured_data"])

    for i, aoi in enumerate(aois):
        psi_delta_df.loc[aoi, "Δ"] = data[:, 1, i, 0, 0]
        psi_delta_df.loc[aoi, "Ψ"] = data[:, 0, i, 0, 0]

    return psi_delta_df


def read_rho(nxs_filename: str) -> pd.DataFrame:
    """Reads rho value from NeXus datafile.
    Currently, this works only with psi / delta representation in the NeXus file.

    Raises:
        ValueError: Is raised when the data is not stored as psi / delta value.

    Returns:
        pd.DataFrame: DataFrame containing the measured data as imaginary rho value.
            The index is a multiindex consisting of the angle of incidents as first column
            and the wavlength as second column.
    """
    return calc_rho(read_psi_delta(nxs_filename))
