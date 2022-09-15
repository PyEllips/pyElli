# Encoding: utf-8
"""Dispersion law for an UV and IR pole."""
import numpy.typing as npt

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion


class Poles(Dispersion):
    r"""Dispersion law for an UV and IR pole,
    i.e. Lorentz oscillators outside the fitting spectral range and zero broadening.

    Single parameters:
        :A_ir: IR Pole amplitude. Defaults to 1. Unit in eV\ :sup:`2`.
        :A_uv: UV Pole amplitude. Defaults to 1. Unit in eV\ :sup:`2`.
        :E_uv: UV Pole energy. Defaults to 6. Unit in eV.

    Repeated parameters:
        --

    Output:
        .. math::
                \varepsilon(E) = \boldsymbol{A\_ir} / E^2
                + \boldsymbol{A\_uv} / (\boldsymbol{E\_uv}^2 - E^2)
    """

    single_params_template = {"A_ir": 1, "A_uv": 1, "E_uv": 6}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        return self.single_params.get("A_ir") / energy**2 + self.single_params.get(
            "A_uv"
        ) / (self.single_params.get("E_uv") ** 2 - energy**2)
