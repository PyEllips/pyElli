# Encoding: utf-8
"""Splines dispersion for fitting."""
from typing import List

import numpy as np
import numpy.typing as npt
from lmfit import Parameters
from scipy.interpolate import BSpline

from .. import Dispersion


class SplinesModel(Dispersion):
    r"""Approximate a dispersion by cubic splines.

    Single parameters:
        :knots: List or array of knots to use.
        :coefficients: List of coefficients for Spline components.
        :k: order of Spline function. Default to 3.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(\lambda) = \boldsymbol{n}^2
    """

    single_params_template = {
        "knots": np.linspace(200, 1000, 24),
        "coefficients": np.linspace(1, 1, 20),
        "k": 3,
        "imaginary": False
    }
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        spl = BSpline(
            self.single_params.get("knots"),
            self.single_params.get("coefficients"),
            self.single_params.get("k"),
            extrapolate=False,
        )
        if self.single_params.get("imaginary"):
            return 0 + 1j * spl(lbda)    
        return spl(lbda)

    @staticmethod
    def generate_params(
        params: Parameters, name: str, n: int, value: float = 1
    ) -> List[Parameters]:
        """_summary_

        Args:
            params (Parameters): _description_
            name (str): _description_
            n (int): _description_
            value (float, optional): _description_. Defaults to 1.

        Returns:
            List[Parameters]: _description_
        """
        coeffs = []
        for i in range(1, n + 1):
            params.add(name + "_c" + str(i), value)
            coeffs.append(name + "_c" + str(i))
        return coeffs
