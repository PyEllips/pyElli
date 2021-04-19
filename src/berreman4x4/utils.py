# Encoding: utf-8
import pandas as pd
import numpy as np
import scipy.constants as sc

from .dispersions import DispersionTableEpsilon


UnitConversion = {
    'm': 1,
    'cm': 1e-2,
    'mm': 1e-3,
    'µm': 1e-6,
    'um': 1e-6,
    'nm': 1e-9,
    'A': 1e-10,
    'Å': 1e-10,
    'pm': 1e-12
}


def lambda2E(value, unit='nm'):
    '''Returns the Energy in eV of the given wavelength in [unit] (default 'nm')'''
    return sc.speed_of_light * sc.Planck / (value * UnitConversion[unit] / UnitConversion['nm'])


def calcPseudoDiel(df, angle):
    psi = df['Ψ'] * np.pi / 180
    delta = df['Δ'] * np.pi / 180
    theta = angle * np.pi / 180

    rho = np.tan(psi) * np.exp(1j * delta)
    eps = np.sin(theta)**2 * (1 + np.tan(theta)**2 * ((1 - rho) / (1 + rho))**2)

    return pd.concat({'ϵ1': eps.apply(lambda x: x.real),
                      'ϵ2': eps.apply(lambda x: x.imag)}, axis=1)


class SpectraRay():

    def __init__(self, path):
        self.spectraray_path = path

    def loadDispersionTable(self, fname):
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
    def read_psi_delta_file(fname):
        return pd.read_csv(fname, index_col=0, sep=' ', usecols=[0, 1, 2], names=['Wavelength', 'Ψ', 'Δ'], skiprows=1)

    @staticmethod
    def eV2nm(wlen):
        return sc.value('Planck constant in eV s') * sc.c * 1e9 / wlen
