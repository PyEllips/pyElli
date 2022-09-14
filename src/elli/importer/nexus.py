"""Read and write NeXus files in the ellipsometry
`standard <https://manual.nexusformat.org/classes/contributed_definitions/NXellipsometry.html#nxellipsometry>`_.
NeXus is a format originating from large beam line facitilies and is adapted for
other smaller labratory experiments to supply an agreed standard for data sharing.
For now only reading is supported but in the future there will also be a writer
to store the whole optical model and fit inside the NeXus file."""
import h5py
import numpy as np
import pandas as pd

from ..utils import calc_rho


def read_nexus_psi_delta(nxs_filename: str) -> pd.DataFrame:
    """Read a NeXus file containing Psi and Delta data.

    Args:
        nxs_filename (str): The filename of the NeXus file.

    Raises:
        ValueError: Is raised when the data is not stored as psi / delta value.

    Returns:
        pd.DataFrame: Psi/Delta DataFrame.
        The index is a multiindex consisting of the angle of incidents as first column
        and the wavelength as second column.
    """
    h5file = h5py.File(nxs_filename, "r")
    if h5file["entry/sample/data_type"].asstr()[()] != "psi/delta":
        raise ValueError("Data type is not psi / delta")

    aois = np.array(h5file["entry/instrument/angle_of_incidence"])
    wavelength = np.array(h5file["entry/instrument/spectrometer/wavelength"]) / 10
    column_names = np.array(h5file["/entry/sample/column_names"].asstr())
    psi_delta_df = pd.DataFrame(
        {},
        columns=column_names,
        index=pd.MultiIndex.from_product(
            [aois, wavelength], names=["Angle of Incidence", "Wavelength"]
        ),
        dtype=float,
    )

    data = np.array(h5file["/entry/sample/measured_data"])

    for i, aoi in enumerate(aois):
        psi_delta_df.loc[aoi, column_names[1]] = data[0, 0, i, 1, :]
        psi_delta_df.loc[aoi, column_names[0]] = data[0, 0, i, 0, :]

    return psi_delta_df.rename(columns={"psi": "Ψ", "delta": "Δ"})


def read_nexus_rho(nxs_filename: str) -> pd.DataFrame:
    """Reads rho value from NeXus datafile.
    Currently, this works only with psi / delta representation in the NeXus file.

    Raises:
        ValueError: Is raised when the data is not stored as psi / delta value.

    Returns:
        pd.DataFrame: DataFrame containing the measured data as imaginary rho value.
        The index is a multiindex consisting of the angle of incidents as first column
        and the wavelength as second column.
    """
    return calc_rho(read_nexus_psi_delta(nxs_filename))
