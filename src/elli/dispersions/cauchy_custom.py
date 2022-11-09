# Encoding: utf-8
"""Cauchy dispersion with custom exponents."""
import numpy.typing as npt

from .base_dispersion import Dispersion


class CauchyCustomExponent(Dispersion):
    r"""Cauchy dispersion with custom exponents.

    Single parameters:
        :n0: Defaults to 1.5.

    Repeated parameters:
        :f: Defaults to 0.
        :e: Defaults to 1.

    Output:
        .. math::
            \varepsilon^{1/2}(\lambda) =
            \boldsymbol{n_0} + \sum_j \boldsymbol{f}_j \cdot \lambda^{\boldsymbol{e}_j}
    """

    single_params_template = {"n0": 1.5}
    rep_params_template = {"f": 0, "e": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        refr_index = self.single_params.get("n0") + sum(
            c.get("f") * lbda ** c.get("e") for c in self.rep_params
        )

        return refr_index**2
