# Encoding: utf-8
"""Lorentz dispersion law with parameters in units of energy."""
import numpy.typing as npt

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion


class LorentzEnergy(Dispersion):
    r"""Lorentz dispersion law with parameters in units of energy.

    Single parameters:
        --

    Repeated parameters:
        :A: Amplitude of the oscillator. Defaults to 1.
        :E: Resonance energy. Defaults 0. Unit in eV.
        :gamma: Broadening of the oscillator. Defaults to 0. Unit in eV.

    Output:
        .. math::
            \varepsilon(E) = 1 + \sum_j \boldsymbol{A}_j / \left(E^2-\boldsymbol{E}_j^2
            + i \cdot \boldsymbol{gamma}_j \cdot E\right)

        With :math:`j`  as the index for the respective oscillator.
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 0, "gamma": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        return 1 + sum(
            c.get("A") / (c.get("E") ** 2 - energy**2 - 1j * c.get("gamma") * energy)
            for c in self.rep_params
        )
