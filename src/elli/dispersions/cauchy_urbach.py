# Encoding: utf-8
"""Cauchy dispersion, with Urbach tail."""

import numpy as np
import numpy.typing as npt

from .base_dispersion import IndexDispersion
from ..utils import conversion_wavelength_energy


class CauchyUrbach(IndexDispersion):
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
        .. math::
            n(E) =
            \boldsymbol{n_0} + \boldsymbol{B} E^2 + \boldsymbol{C} E^4
            + i \boldsymbol{D} \exp (\frac{E - \boldsymbol{E_g}}{\boldsymbol{E_u}})

    References:
        * Fujiwara: Spectroscopic Ellipsometry: Principles and Applications,
          John Wiley & Sons Ltd, 2007, p. 258
    """

    single_params_template = {"n0": 1.5, "B": 0, "C": 0, "D": 0, "Eg": 2, "Eu": 0.5}
    rep_params_template = {}

    def refractive_index(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        return (
            self.single_params.get("n0")
            + self.single_params.get("B") * energy**2
            + self.single_params.get("C") * energy**4
            + 1j
            * self.single_params.get("D")
            * np.exp(
                (energy - self.single_params.get("Eg")) / self.single_params.get("Eu")
            )
        )
