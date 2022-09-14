# Encoding: utf-8
"""Dispersion law with gaussian oscillators."""
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt

# pylint: disable=no-name-in-module
from scipy.special import dawsn

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion


class Gaussian(Dispersion):
    r"""Dispersion law with gaussian oscillators.

    Single parameters:
        --

    Repeated parameters:
        :A: Amplitude of the oscillator. Defaults to 1.
        :E: Central energy. Defaults to 1. Unit in eV.
        :sigma: Broadening of the Gaussian. Defaults to 1. Unit in eV.

    Output:

        .. math::
            \varepsilon(E) = \sum_j & \; 2 \cdot \boldsymbol{A}_j / \sqrt{π} \cdot
                    (D\left(2 \cdot \sqrt{2 \cdot \ln(2)} \cdot (E + \boldsymbol{E}_j)
                    / \boldsymbol{sigma}_j\right) \\
                    &- D\left(2 \cdot \sqrt{2 \cdot \ln(2)} \cdot (E - \boldsymbol{E}_j)
                    / \boldsymbol{sigma}_j\right) \\
                    &+ i \cdot \Bigl(\boldsymbol{A}_j \cdot \exp\left(-(4 \cdot \ln(2) \cdot
                    (E - \boldsymbol{E}_j)/ \boldsymbol{sigma}_j\right)^2 \\
                    &- \boldsymbol{A}_j \cdot \exp\left(-(4 \cdot ln(2) \cdot
                    (E + \boldsymbol{E}_j)/ \boldsymbol{sigma}_j\right)^2\Bigr)

        D is the
        `Dawson function
        <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.dawsn.html>`_.
        The summation index :math:`j` is the index of the respective oscillator.

    References:
        * De Sousa Meneses, Malki, Echegut, J. Non-Cryst. Solids 351, 769-776 (2006)
        * Peiponen, Vartiainen, Phys. Rev. B. 44, 8301 (1991)
        * Fujiwara, Collins, Spectroscopic Ellipsometry for Photovoltaics Volume 1,
          Springer International Publishing AG, 2018, p. 137
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 1, "sigma": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        ftos = 2 * sqrt(np.log(2))
        return sum(
            2
            * c.get("A")
            / sqrt(np.pi)
            * (
                dawsn(ftos * (energy + c.get("E")) / c.get("sigma"))
                - dawsn(ftos * (energy - c.get("E")) / c.get("sigma"))
            )
            + 1j
            * (
                c.get("A")
                * np.exp(-((ftos * (energy - c.get("E")) / c.get("sigma")) ** 2))
                - c.get("A")
                * np.exp(-((ftos * (energy + c.get("E")) / c.get("sigma")) ** 2))
            )
            for c in self.rep_params
        )
