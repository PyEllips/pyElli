"""A helper class to load data from SpectraRay ASCII Files
"""
import pandas as pd
import scipy.constants as sc
from .dispersions import DispersionTableEpsilon
from .utils import calc_rho

class SpectraRay():

    def __init__(self, path: str) -> None:
        self.spectraray_path = path

    def loadDispersionTable(self, fname: str) -> DispersionTableEpsilon:
        start = 0
        stop = 0
        with open(self.spectraray_path + fname, 'r', encoding='utf8') as file:
            line = file.readline()
            cnt = 0
            while line:
                if line.strip() == 'Begin of array':
                    start = cnt + 1
                if line.strip() == 'End of array':
                    stop = cnt
                line = file.readline()
                cnt += 1

                if line.startswith('Units='):
                    x_unit = line.split('=')[1].split(',')[0]

        df = pd.read_csv(self.spectraray_path + fname,
                         delim_whitespace=True,
                         skiprows=start, nrows=stop-start,
                         index_col=0, usecols=[0, 1, 2],
                         names=[x_unit, 'ϵ1', 'ϵ2'])

        if x_unit == 'Wavelength':
            return DispersionTableEpsilon(df.index, df.loc[:, 'ϵ1'] + 1j * df.iloc[:, 'ϵ2'])
        return DispersionTableEpsilon(SpectraRay.eV2nm(df.index), df.loc[:, 'ϵ1'] + 1j * df.loc[:, 'ϵ2'])

    @staticmethod
    def read_psi_delta_file(fname: str, decimal: str = '.') -> pd.DataFrame:
        psi_delta = pd.read_csv(fname,
                                index_col=0,
                                sep=r'\s+',
                                decimal=decimal,
                                usecols=[0, 1, 2],
                                names=['Wavelength', 'Ψ', 'Δ'],
                                skiprows=1)

        psi_delta.loc[:,'Δ'] = psi_delta.loc[:,'Δ'].where(
            psi_delta.loc[:,'Δ'] <= 180, psi_delta.loc[:,'Δ'] - 360
        )

        return psi_delta

    @staticmethod
    def read_mmatrix(fname: str, decimal: str = '.') -> pd.DataFrame:
        """Read a Mueller matrix from a Sentech ASCII file.
        Save the file in SpectraRay under Save As -> Ascii (.txt)"""
        mueller_matrix = pd.read_csv(fname,
                                     sep=r'\s+',
                                     decimal=decimal,
                                     index_col=0).iloc[:, -17:-1]
        mueller_matrix.index.name = 'Wavelength'
        mueller_matrix.columns = ['M11', 'M12', 'M13', 'M14',
                                 'M21', 'M22', 'M23', 'M24',
                                 'M31', 'M32', 'M33', 'M34',
                                 'M41', 'M42', 'M43', 'M44']

        return mueller_matrix

    @staticmethod
    def read_rho(fname: str, decimal: str = '.') -> pd.DataFrame:
        psi_delta = SpectraRay.read_psi_delta_file(fname, decimal)
        return calc_rho(psi_delta)

    @staticmethod
    def eV2nm(wlen):
        return sc.value('Planck constant in eV s') * sc.c * 1e9 / wlen
