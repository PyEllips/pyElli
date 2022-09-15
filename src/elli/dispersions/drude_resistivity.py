# Encoding: utf-8
"""Drude dispersion model with resistivity based parameters."""
import numpy as np
import numpy.typing as npt
import scipy.constants as sc

from ..utils import conversion_wavelength_energy
from .base_dispersion import Dispersion


class DrudeResistivity(Dispersion):
    r"""Drude dispersion model with resistivity based parameters.
    Drude models in the literature typically contain an additional epsilon infinity value.
    Use `EpsilonInf` to add this parameter or simply do DrudeEnergy() + eps_inf.

    Single parameters:
        :rho_opt: Optical resistivity. Defaults to 1. Unit in Ω-cm.
        :tau: Mean scattering time. Defaults to 1. Unit in s.

    Repeated parameters:
        --

    Output:

        .. math::
            \varepsilon(E) = \hbar / (\varepsilon_0  \cdot
            \boldsymbol{rho\_opt} \cdot \boldsymbol{tau} \cdot E^2
            - i \cdot \hbar \cdot E)

       where :math:`\hbar` is the planck constant divided by :math:`2\pi`
       and :math:`\varepsilon_0` is the vacuum dielectric permittivity.
    """

    single_params_template = {"rho_opt": 1, "tau": 1}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        hbar = sc.value("Planck constant in eV/Hz") / 2 / np.pi
        eps0 = sc.value("vacuum electric permittivity") * 1e-2

        return hbar**2 / (
            eps0
            * self.single_params.get("rho_opt")
            * (self.single_params.get("tau") * energy**2 - 1j * hbar * energy)
        )
