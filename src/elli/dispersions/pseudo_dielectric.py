# Encoding: utf-8
"""Pseudo dielectric function dispersion."""
from typing import Union
import numpy as np
import numpy.typing as npt
from scipy.interpolate import interp1d

from .base_dispersion import Dispersion, InvalidParameters


class PseudoDielectricFunction(Dispersion):
    r"""A pseudo dielectric function generated from experimental psi/delta values.
    Please note that the pseudo dielectric function can lead to unphysical behaviour, such
    as negative refractive indices or other spurious artifacts.
    Additionally, this formula is only valid for a bulk absorbing material and yields wrong
    results for layered materials.
    Therefore, it is preferable to use the pseudo dielectric function only as a helper for
    constructing other dispersion models.

    Single parameters:
        :angle: The measurement angle in degree under which the psi/delta values where obtained.
        :lbda: The wavelength region of the measurement data. Units in nm.
        :psi: The psi values of the measurement. Units in degree.
        :delta: The delta values of the measurement. Units in degree.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(\lambda) = \sin^2 \left( \Theta \right) \cdot
            \left( 1 + \tan^2 (\Theta) \left( \frac{1 - \rho}{1 + \rho} \right) \right)

        With
        .. math::
            \rho = \tan(\Psi) \cdot \exp (-i \Delta)

        :math:`\Theta` is the angle of incidence.
    """

    single_params_template = {"angle": None, "lbda": None, "psi": None, "delta": None}
    rep_params_template = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for param in self.single_params:
            if self.single_params[param] is None:
                raise InvalidParameters(f"Please specify parameter {param}")

        rho = np.tan(np.deg2rad(self.single_params.get("psi"))) * np.exp(
            -1j * np.deg2rad(self.single_params.get("delta"))
        )
        theta = self.single_params.get("angle") * np.pi / 180
        eps = np.sin(theta) ** 2 * (
            1 + np.tan(theta) ** 2 * ((1 - rho) / (1 + rho)) ** 2
        )

        self.interpolation = interp1d(
            self.single_params.get("lbda"),
            eps,
            kind="cubic",
        )

    def __add__(self, _: Union[int, float, "Dispersion"]) -> "DispersionSum":
        raise NotImplementedError("Adding of tabular dispersions is not yet supported")

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
