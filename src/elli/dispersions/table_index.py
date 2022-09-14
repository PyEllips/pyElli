# Encoding: utf-8
"""Dispersion specified by a table of wavelengths (nm) and refractive index values."""
import numpy as np
import numpy.typing as npt
import scipy.interpolate

from .base_dispersion import Dispersion, InvalidParameters


class Table(Dispersion):
    """Dispersion specified by a table of wavelengths (nm) and refractive index values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        :lbda (list): Wavelengths in nm. Defaults to np.linspace(0, 3000, 1000).
        :epsilon: Complex refractive index values in the convention n + ik.
            Defaults to np.ones(1000).

    Repeated parameters:
        --

    Output:
        The interpolation in the given wavelength range.
    """

    single_params_template = {"lbda": np.linspace(0, 3000, 1000), "n": np.ones(1000)}
    rep_params_template = {}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if len(self.single_params.get("lbda")) == 0:
            raise InvalidParameters("Wavelength array cannot be of length zero.")

        if len(self.single_params.get("n")) != len(self.single_params.get("lbda")):
            raise InvalidParameters(
                "Wavelength and refractive index arrays must have the same length."
            )

        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("n") ** 2,
            kind="cubic",
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
