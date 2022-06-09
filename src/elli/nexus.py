"""Read and write NeXus files."""
import h5py
import pandas as pd


class NexusReader:
    """Read NeXus ellipsometry files into pandas dataframes"""

    def __init__(self, h5_filename: str) -> None:
        self.h5file = h5py.File(h5_filename, "r")

    def psi_delta(self) -> pd.DataFrame:
        """Read the Ψ and Δ data from the NeXus file

        Returns:
            pd.DataFrame: Psi/Delta DataFrame
        """
        raise NotImplementedError()

    def rho(self) -> pd.DataFrame:
        """Read the rho values from the NeXus file

        Returns:
            pd.DataFrame: Imaginary rho DataFrame
        """
        raise NotImplementedError()
