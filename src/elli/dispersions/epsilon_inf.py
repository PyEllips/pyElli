# Encoding: utf-8
"""Constant epsilon infinity."""
import numpy.typing as npt

from .base_dispersion import Dispersion


class EpsilonInf(Dispersion):
    r"""Constant epsilon infinity.

    Single parameters:
        :eps: Constant value for the constant epsilon. Defaults to 1.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(\lambda) = \textbf{eps}
    """

    single_params_template = {"eps": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("eps")
