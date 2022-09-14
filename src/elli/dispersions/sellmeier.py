# Encoding: utf-8
"""Sellmeier dispersion."""
import numpy.typing as npt

from .base_dispersion import Dispersion


class Sellmeier(Dispersion):
    r"""Sellmeier dispersion.

    Single parameters:
        --

    Repeated parameters:
        :A: Coefficient for n\ :sup:`2` contribution. Defaults to 0.
        :B: Resonance wavelength. Defaults to 0. Unit in µm\ :sup:`-2`.

    Output:
        .. math::
            \varepsilon(\lambda) = 1 + \sum_j \boldsymbol{A}_j
            \cdot \lambda^2 /(\lambda^2 - \boldsymbol{B}_j)

        With :math:`j` as the index of the respective oscillator.
    """

    single_params_template = {}
    rep_params_template = {"A": 0, "B": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        lbda = lbda / 1e3
        return 1 + sum(
            c.get("A") * lbda**2 / (lbda**2 - c.get("B")) for c in self.rep_params
        )
