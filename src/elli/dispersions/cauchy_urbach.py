# Encoding: utf-8
"""Cauchy dispersion."""
import numpy.typing as npt

from .base_dispersion import Dispersion
from ..utils import conversion_wavelength_energy


class CauchyUrbach(Dispersion):
    r"""Cauchy dispersion, with an Urbach Tail absorption.

    Single parameters:
        :n0: Defaults to 1.5.
        :B: Defaults to 0. Unit in 1/eV\ :sup:`2`.
        :C: Defaults to 0. Unit in 1/eV\ :sup:`4`.
        :D: Defaults to 0.
        :Eg: Defaults to 0. Unit in eV.
        :Eu: Defaults to 1. Unit in eV.

    Repeated parameters:
        --

    Output:
    """

    single_params_template = {"n0": 1.5, "B": 0, "C": 0, "D": 0, "Eg": 0, "Eu": 1}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        refr_index = (
            self.single_params.get("n0")
            + self.single_params.get("B") * energy**2
            + self.single_params.get("C") * energy**4
            + 1j
            * self.single_params.get("D")
            * np.exp(
                (energy - self.single_params.get("Eg")) / self.single_params.get("Eu")
            )
        )
        return refr_index**2
