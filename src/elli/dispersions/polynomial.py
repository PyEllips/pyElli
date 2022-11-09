# Encoding: utf-8
"""Polynomial dispersion."""
import numpy.typing as npt

from .base_dispersion import Dispersion


class Polynomial(Dispersion):
    r"""Polynomial expression for the dielectric function.

    Single parameters:
        :e0: Defaults to 1.

    Repeated parameters:
        :f: Defaults to 0.
        :e: Defaults to 0.

    Output:
        .. math::
            \varepsilon(\lambda) =
            \boldsymbol{\varepsilon_0} + \sum_j \boldsymbol{f}_j \cdot \lambda^{\boldsymbol{e}_j}
    """

    single_params_template = {"e0": 1}
    rep_params_template = {"f": 0, "e": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("e0") + sum(
            c.get("f") * lbda ** c.get("e") for c in self.rep_params
        )
