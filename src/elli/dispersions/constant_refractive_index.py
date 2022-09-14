# Encoding: utf-8
"""Constant refractive index."""
import numpy.typing as npt

from .base_dispersion import Dispersion


class ConstantRefractiveIndex(Dispersion):
    r"""Constant refractive index.

    Single parameters:
        :n: The constant value of the refractive index. Defaults to 1.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(\lambda) = \boldsymbol{n}^2
    """

    single_params_template = {"n": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("n") ** 2
