# Encoding: utf-8
"""Sellmeier dispersion."""
import numpy.typing as npt

from .base_dispersion import Dispersion


class SellmeierCustomExponent(Dispersion):
    r"""Sellmeier dispersion with custom exponents.

    Single parameters:
        --

    Repeated parameters:
        :A: Coefficient for n\ :sup:`2` contribution. Defaults to 0.
        :B: Resonance wavelength. Defaults to 0. Unit in µm\ :sup:`-2`.
        :e_A:
        :e_B:

    Output:
        .. math::
            \varepsilon(\lambda) = \sum_j \boldsymbol{A}_j
            \cdot \lambda^{\boldsymbol{e_A}j} /(\lambda^2 - \boldsymbol{B}_j^{\boldsymbol{e_B}j})

        With :math:`j` as the index of the respective oscillator.
    """

    single_params_template = {}
    rep_params_template = {"A": 0, "B": 0, "e_A": 1, "e_B": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        lbda = lbda / 1e3
        return sum(
            c.get("A") * lbda ** c.get("e_A") / (lbda**2 - c.get("B") ** c.get("e_B"))
            for c in self.rep_params
        )
