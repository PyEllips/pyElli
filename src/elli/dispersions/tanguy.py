# Encoding: utf-8
"""Fractional dimensional Tanguy model."""
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt

# pylint: disable=no-name-in-module
from scipy.special import digamma, gamma

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion


class Tanguy(Dispersion):
    r"""Fractional dimensional Tanguy model.
    This model is an analytical expression of Wannier excitons, including
    bound and unbound states.

    Single parameters:
          :A: Amplitude (eV). Defaults to 1.
          :d: Dimensionality 1 < d <= 3. Defaults to 3.
          :gamma: Excitonic broadening (eV). Defaults to 0.1.
          :R: Excitonic binding energy (eV). Defaults to 0.1.
          :Eg: Optical band gap energy (eV). Defaults to 1.
          :a: Sellmeier coefficient for background dielectric constant (eV²).
            Defaults to 0.
          :b: Sellmeier coefficient for background dielectric constant (eV²).
            Defaults to 0.

    Repeated parameters.
        --

    Output:
        The Tanguy dispersion. Since the formula is rather long it is not written here.
        Please refer to the references for a full formula.

    References:
        * C. Tanguy, Phys. Rev. Lett. 75, 4090 (1995). Errata, Phys. Rev. Lett. 76, 716 (1996).
        * C. Tanguy, Phys. Rev. B. 60. 10660 (1990).
    """

    single_params_template = {
        "A": 1,
        "d": 3,
        "gamma": 0.1,
        "R": 0.1,
        "Eg": 1,
        "a": 0,
        "b": 0,
    }
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = conversion_wavelength_energy(lbda)
        A = self.single_params.get("A")
        d = self.single_params.get("d")
        gam = self.single_params.get("gamma")
        R = self.single_params.get("R")
        Eg = self.single_params.get("Eg")
        a = self.single_params.get("a")
        b = self.single_params.get("b")

        return (
            1
            + a / (b - E**2)
            + A
            * R ** (d / 2 - 1)
            / (E + 1j * gam) ** 2
            * (
                Tanguy.g(Tanguy.xsi(E + 1j * gam, R, Eg), d)
                + Tanguy.g(Tanguy.xsi(-E - 1j * gam, R, Eg), d)
                - 2 * Tanguy.g(Tanguy.xsi(E * 0, R, Eg), d)
            )
        )

    @staticmethod
    def xsi(z, R, Eg):
        return sqrt(R / (Eg - z))

    @staticmethod
    def g(xsi, d):
        if d == 2:
            return 2 * np.log(xsi) - 2 * digamma(0.5 - xsi)
        if d == 3:
            return 2 * np.log(xsi) - 2 * digamma(1 - xsi) - 1 / xsi

        D = d - 1
        return (
            2
            * np.pi
            * gamma(D / 2 + xsi)
            / gamma(D / 2) ** 2
            / gamma(1 - D / 2 + xsi)
            / xsi ** (d - 2)
            * (1 / np.tan(np.pi * (D / 2 - xsi)) - 1 / np.tan(np.pi * D))
        )
