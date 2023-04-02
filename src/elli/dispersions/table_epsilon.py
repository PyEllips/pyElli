# Encoding: utf-8
"""Dispersion specified by a table of wavelengths (nm) and dielectric function values."""
from typing import Union
import numpy.typing as npt
import scipy.interpolate

from .base_dispersion import Dispersion, InvalidParameters, DispersionSum


class TableEpsilon(Dispersion):
    r"""Dispersion specified by a table of wavelengths (nm) and dielectric function values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        :lbda (list): Wavelengths in nm. This value must be provided.
        :epsilon: Complex dielectric function values in the convention ε1 + iε2.
            This value must be provided.

    Repeated parameters:
        --

    Output:
        The interpolation in the given wavelength range.
    """

    single_params_template = {"lbda": None, "epsilon": None}
    rep_params_template = {}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if len(self.single_params.get("lbda")) == 0:
            raise InvalidParameters("Wavelength array cannot be of length zero.")

        if len(self.single_params.get("epsilon")) != len(
            self.single_params.get("lbda")
        ):
            raise InvalidParameters(
                "Wavelength and epsilon arrays must have the same length."
            )

        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("epsilon"),
            kind="cubic",
        )

        self.default_lbda_range = self.single_params.get("lbda")

    def __add__(self, _: Union[int, float, "Dispersion"]) -> "DispersionSum":
        raise NotImplementedError("Adding of tabular dispersions is not yet supported")

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
