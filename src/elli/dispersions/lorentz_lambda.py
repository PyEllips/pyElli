# Encoding: utf-8
"""Lorentz dispersion law with parameters in units of wavelengths."""
import numpy.typing as npt

from .base_dispersion import Dispersion


class LorentzLambda(Dispersion):
    r"""Lorentz dispersion law with parameters in units of wavelengths.

    Single parameters:
        --

    Repeated parameters:
        :A: Amplitude of the oscillator. Defaults to 1.
        :lambda_r: Resonance wavelength. Defaults to 0. Unit in nm.
        :gamma: Broadening of the oscillator. Defaults to 0. Unit in nm.

    Output:

        .. math::
            \varepsilon(\lambda) = 1 + \sum_j \boldsymbol{A}_j
            \cdot \lambda^2 / (\lambda^2 - \boldsymbol{lambda\_r}_j^2
            + i \cdot \boldsymbol{gamma}_j \cdot \lambda)

        The summation index :math:`j` refers to the respective oscillator.
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "lambda_r": 0, "gamma": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return 1 + sum(
            c.get("A")
            * lbda**2
            / (lbda**2 - c.get("lambda_r") ** 2 - 1j * c.get("gamma") * lbda)
            for c in self.rep_params
        )
