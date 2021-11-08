# Encoding: utf-8
import pandas as pd
import numpy as np
import scipy.constants as sc
from numpy.lib.scimath import sqrt
from .dispersions import DispersionTableEpsilon

def calcPseudoDiel(rho, angle: float, output: str = 'eps') -> pd.DataFrame:
    """Calculates the pseudo dielectric function of a measurement from rho.

    Args:
        rho (pandas.DataFrame): Measurement DataFrame containing rho as complex number as column and wavelength as index
        angle (float): Angle of measurement in degree
        output (str, optional): Output format for dielectric function.
            'n': refractive index,
            'eps': Dielectic function as two-column pandas.DataFrame,
            'epsi': Dielectric function as imaginary number.
            Defaults to 'eps'.

    Returns:
        pandas.DataFrame: Frame containing the pseudo dielectric function or refractive index.
    """
    theta = angle * np.pi / 180
    eps = np.sin(theta)**2 * (1 + np.tan(theta)**2 * ((1 - rho) / (1 + rho))**2)

    if output == 'n':
        n = sqrt(eps)
        return pd.DataFrame({'n': n.real,
                             'k': n.imag}, index=eps.index)

    if output == 'epsi':
        return eps

    return pd.concat({'ϵ1': eps.apply(lambda x: x.real),
                      'ϵ2': eps.apply(lambda x: x.imag)}, axis=1)


def calc_rho(psi_delta: pd.DataFrame) -> pd.DataFrame:
    """Calculate rho from a Psi-Delta DataFrame. The Psi-Delta DataFrame should be structured as follows:
        index: Wavelength
        column 'Ψ': Psi from measurement
        column 'Δ': Delta from measurement

        This format is as returned from SpectraRay.read_psi_delta_file(...).

    Args:
        psi_delta (pandas.DataFrame): DataFrame containing Psi+Delta Measurement data

    Returns:
        pandas.DataFrame: Frame containing rho as an imaginary number.
    """
    return psi_delta.apply(lambda x: np.tan(np.deg2rad(x['Ψ'])) *
                           np.exp(-1j * np.deg2rad(x['Δ'])),
                           axis=1)

class SpectraRay():

    def __init__(self, path: str) -> None:
        self.spectraray_path = path

    def loadDispersionTable(self, fname: str) -> DispersionTableEpsilon:
        start = 0
        stop = 0
        with open(self.spectraray_path + fname, 'r') as f:
            line = f.readline()
            cnt = 0
            while line:
                if line.strip() == 'Begin of array':
                    start = cnt + 1
                if line.strip() == 'End of array':
                    stop = cnt
                line = f.readline()
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
        elif x_unit == 'eV':
            return DispersionTableEpsilon(SpectraRay.eV2nm(df.index), df.loc[:, 'ϵ1'] + 1j * df.loc[:, 'ϵ2'])

    @staticmethod
    def read_psi_delta_file(fname: str, decimal: str = '.') -> pd.DataFrame:
        return pd.read_csv(fname,
                           index_col=0,
                           sep=r'\s+',
                           decimal=decimal,
                           usecols=[0, 1, 2],
                           names=['Wavelength', 'Ψ', 'Δ'],
                           skiprows=1)

    @staticmethod
    def read_rho(fname: str, decimal: str = '.') -> pd.DataFrame:
        psi_delta = SpectraRay.read_psi_delta_file(fname, decimal)
        return calc_rho(psi_delta)

    @staticmethod
    def eV2nm(wlen):
        return sc.value('Planck constant in eV s') * sc.c * 1e9 / wlen


def get_QWP_thickness(material: "Material", lbda: float) -> float:
    """Return the thickness in nm of a Quater Wave Plate at wavelength 'lbda'."""
    nr = np.real(material.getRefractiveIndex(lbda)[0, 0, 0])
    return lbda / (4.*nr)
