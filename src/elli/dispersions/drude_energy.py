# Encoding: utf-8
"""Drude dispersion model with parameters in units of energy."""
import numpy.typing as npt

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion


class DrudeEnergy(Dispersion):
    r"""Drude dispersion model with parameters in units of energy.
    Drude models in the literature typically contain an additional epsilon infinity value.
    Use `EpsilonInf` to add this parameter or simply add a number, e.g. DrudeEnergy() + 2, where
    2 is the value of epsilon infinity.

    Single parameters:
        :A: Amplitude of Drude oscillator. Defaults to 0. Unit in eV\ :sup:`2`
        :gamma: Broadening of Drude oscillator. Defaults to 0. Unit in eV.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(E)
            = \boldsymbol{A} / (E^2 - i \cdot \boldsymbol{gamma} \cdot E)
    """

    single_params_template = {"A": 0, "gamma": 0}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        return self.single_params.get("A") / (
            energy**2 - 1j * self.single_params.get("gamma") * energy
        )
