# Encoding: utf-8
import pandas as pd
import numpy as np
import scipy.constants as sc
from numpy.lib.scimath import sqrt

def calc_pseudo_diel(rho, angle: float, output: str = 'eps') -> pd.DataFrame:
    """Calculates the pseudo dielectric function of a measurement from rho.

    Args:
        rho (pandas.DataFrame):
            Measurement DataFrame containing rho as complex number as column and wavelength as index
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
    """Calculate rho from a Psi-Delta DataFrame.
            The Psi-Delta DataFrame should be structured as follows:
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

def get_qwp_thickness(material: "Material", lbda: float) -> float:
    """Return the thickness of a material in nm for a quater wave plate at wavelength 'lbda'.

    Args:
        material (Material): Material object of the quarter wave plate
        lbda (float): Wavelength (in nm) at which the quarter wave plate is calculated

    Returns:
        float: Thickness (in nm) of quarter wave plate
    """
    nr = np.real(material.get_refractive_index(lbda)[0, 0, 0])
    return lbda / (4.*nr)
