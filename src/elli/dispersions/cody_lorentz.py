# Encoding: utf-8
"""Cody-Lorentz dispersion law. Model by Ferlauto et al."""
from typing import Dict
import numpy as np
import numpy.typing as npt
from scipy.interpolate import interp1d

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion
from ..kkr import im2re_reciprocal


class CodyLorentz(Dispersion):
    """Tauc-Lorentz dispersion law. Model by Ferlauto et al.

    Single parameters:
        :Eg: Bandgap energy (eV). Defaults to 1.6.
        :A: Amplitude (eV). Defaults to 100.
        :Et: Energy at which the Urbach tail starts (eV). Defaults to 1.8.
        :gamma: Broadening (eV). Defaults to 2.4.
        :Ep:
            Distance from bandgap for transition from Cody type absorption
            to Lorentz type absorption (eV). Defaults to 0.8.
        :E0: Lorentz resonance energy (eV). Defaults to 3.6.
        :Eu: Exponential decay of the Urbach tail (eV). Defaults to 0.05.

    Repeated parameters:
        --

    Output:
        The Cody lorentz dispersion. Please refer to the references for a full formula.

    References:
        * Ferlauto et al., J. Appl. Phys. 92, 2424 (2002)
    """

    single_params_template = {
        "Eg": 1.6,
        "A": 100,
        "Et": 1.8,
        "gamma": 2.4,
        "Ep": 0.8,
        "E0": 3.6,
        "Eu": 0.05,
    }
    rep_params_template: Dict[str, float] = {}

    @staticmethod
    def eps2(E, Eg, A, Et, gamma, Ep, E0, Eu):
        """The imaginary part of the cody lorentz dispersion"""
        # pylint: disable=invalid-name
        def G(E):
            return (E - Eg) ** 2 / ((E - Eg) ** 2 + Ep**2)

        def L(E):
            return A * E0 * gamma * E / ((E**2 - E0**2) ** 2 + gamma**2 * E**2)

        E1 = Et * G(Et) * L(Et)

        # fmt: off
        return (
            E1 / E * np.exp((E - Et) / Eu) * np.heaviside(Et - E, 1)
            + G(E) * L(E) * np.heaviside(E - Et, 0)
        )
        # fmt: on

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)

        lbda_broad = np.linspace(50, 10000, 1000)
        energy_padded = conversion_wavelength_energy(lbda_broad)
        eps1 = im2re_reciprocal(
            CodyLorentz.eps2(energy_padded, **self.single_params), lbda_broad
        )
        eps1_interp = interp1d(lbda_broad, eps1)(lbda)

        return eps1_interp + 1j * CodyLorentz.eps2(energy, **self.single_params)
