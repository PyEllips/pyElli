# Encoding: utf-8
"""Dispersion specified by a table of wavelengths (nm) and refractive index values."""

from typing import Union
import numpy.typing as npt
import scipy.interpolate

from elli.dispersions.constant_refractive_index import ConstantRefractiveIndex

from .base_dispersion import IndexDispersion, IndexDispersionSum, InvalidParameters


class Table(IndexDispersion):
    """Dispersion specified by a table of wavelengths (nm) and refractive index values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        :lbda (list): Wavelengths in nm. This value must be provided.
        :n: Complex refractive index values in the convention n + ik.
            This value must be provided.
        :kind: Type of interpolation
            (see scipy.interpolate.interp1d for more information). Defaults to 'linear'.

    Repeated parameters:
        --

    Output:
        The interpolation in the given wavelength range.
    """

    single_params_template = {"lbda": None, "n": None}
    rep_params_template = {}

    def __init__(self, *args, **kwargs) -> None:
        self.kind = kwargs.pop("kind", "linear")

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
            kind=self.kind,
        )

        self.default_lbda_range = self.single_params.get("lbda")

    def __add__(
        self, other: Union[int, float, "IndexDispersion"]
    ) -> "IndexDispersionSum":
        if isinstance(other, (int, float)):
            return IndexDispersionSum(self, ConstantRefractiveIndex(eps=other))

        if isinstance(other, Table):
            raise NotImplementedError(
                "Adding of tabular dispersions is not yet supported"
            )

        if isinstance(other, IndexDispersion):
            return IndexDispersionSum(self, other)

        if isinstance(other, IndexDispersionSum):
            other.dispersions.append(self)
            return other

        raise TypeError(
            f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'"
        )

    def refractive_index(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
