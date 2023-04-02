# Encoding: utf-8
"""Dispersion specified by a table of wavelengths (nm) and refractive index values."""
import numpy.typing as npt
import scipy.interpolate

from .base_dispersion import IndexDispersion, InvalidParameters


class Table(IndexDispersion):
    """Dispersion specified by a table of wavelengths (nm) and refractive index values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        :lbda (list): Wavelengths in nm. This value must be provided.
        :n: Complex refractive index values in the convention n + ik.
            This value must be provided.

    Repeated parameters:
        --

    Output:
        The interpolation in the given wavelength range.
    """

    single_params_template = {"lbda": None, "n": None}
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
            self.single_params.get("n"),
            kind="cubic",
        )

        self.default_lbda_range = self.single_params.get("lbda")

    def refractive_index(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
