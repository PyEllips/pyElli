# Encoding: utf-8
"""Tauc-Lorentz dispersion law. Model by Jellison and Modine."""
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion


class TaucLorentz(Dispersion):
    """Tauc-Lorentz dispersion law. Model by Jellison and Modine.

    Single parameters:
        :Eg: Bandgap energy (eV). Defaults to 1.

    Repeated parameters:
        :A: Strength of the absorption. Typically 10 < A < 200. Defaults to 20.
        :E: Lorentz resonance energy (eV). Always keep E > Eg!!. Defaults to 1.5.
        :C: Lorentz broadening (eV). Typically 0 < Ci < 10. Defaults to 1.

    Output:
        The Tauc lorentz dispersion. Please refer to the references for a full formula.

    References:
        * G.E. Jellision and F.A. Modine, Appl. Phys. Lett. 69 (3), 371-374 (1996)
        * Erratum, G.E. Jellison and F.A. Modine, Appl. Phys. Lett 69 (14), 2137 (1996)
        * H. Chen, W.Z. Shen, Eur. Phys. J. B. 43, 503-507 (2005)
    """

    single_params_template = {"Eg": 1}
    rep_params_template = {"A": 20, "E": 1.5, "C": 1}

    @staticmethod
    def eps1(E, Eg, Ai, Ei, Ci):
        gamma2 = sqrt(Ei**2 - Ci**2 / 2) ** 2
        alpha = sqrt(4 * Ei**2 - Ci**2)
        aL = (
            (Eg**2 - Ei**2) * E**2
            + Eg**2 * Ci**2
            - Ei**2 * (Ei**2 + 3 * Eg**2)
        )
        aA = (E**2 - Ei**2) * (Ei**2 + Eg**2) + Eg**2 * Ci**2
        zeta4 = (E**2 - gamma2) ** 2 + alpha**2 * Ci**2 / 4

        # fmt: off
        return (
            Ai*Ci*aL/2.0/np.pi/zeta4/alpha/Ei*np.log((Ei**2 + Eg**2 + alpha*Eg)/(Ei**2 + Eg**2 - alpha*Eg)) - \
            Ai*aA/np.pi/zeta4/Ei*(np.pi - np.arctan((2.0*Eg + alpha)/Ci) + np.arctan((alpha - 2.0*Eg)/Ci)) + \
            2.0*Ai*Ei*Eg/np.pi/zeta4/alpha*(E**2 - gamma2)*(np.pi + 2.0*np.arctan(2.0/alpha/Ci*(gamma2 - Eg**2))) - \
            Ai*Ei*Ci*(E**2 + Eg**2)/np.pi/zeta4/E*np.log(abs(E - Eg)/(E + Eg)) + \
            2.0*Ai*Ei*Ci*Eg/np.pi/zeta4 * \
            np.log(abs(E - Eg) * (E + Eg) / sqrt((Ei**2 - Eg**2)**2 + Eg**2 * Ci**2))
        )
        # fmt: on

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        energy_g = self.single_params.get("Eg")
        return sum(
            (
                1j
                * (
                    c.get("A")
                    * c.get("E")
                    * c.get("C")
                    * (energy - energy_g) ** 2
                    / (
                        (energy**2 - c.get("E") ** 2) ** 2
                        + c.get("C") ** 2 * energy**2
                    )
                    / energy
                )
                * np.heaviside(energy - energy_g, 0)
                + self.eps1(energy, energy_g, c.get("A"), c.get("E"), c.get("C"))
            )
            for c in self.rep_params
        )
