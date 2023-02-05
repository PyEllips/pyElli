# Encoding: utf-8
"""Abstract base class and utility classes for pyElli dispersion"""
from abc import ABC, abstractmethod
from typing import List, Union

import numpy as np
import numpy.typing as npt
import pandas as pd
from numpy.lib.scimath import sqrt

from .. import materials
from .. import dispersions


class InvalidParameters(Exception):
    """Exception for invalid dispersion parameters."""


class Dispersion(ABC):
    """Dispersion (abstract class).

    Functions provided for derived classes:
    * dielectric_function(lbda) : returns dielectric constant for wavelength 'lbda'
    """

    @property
    @abstractmethod
    def single_params_template(self) -> dict:
        """Specifies the single parameters of the model and its default values."""

    @property
    @abstractmethod
    def rep_params_template(self) -> dict:
        """Specifies the repeated parameters of the model and its default values."""

    @staticmethod
    def _guard_invalid_params(params1, params2):
        missing_params = np.array(params1)[np.where(~np.in1d(params1, params2))]

        if len(missing_params) > 0:
            missing_param_strings = ", ".join(f"{p}" for p in missing_params)
            raise InvalidParameters(f"Invalid parameter(s): {missing_param_strings}")

    @staticmethod
    def _fill_params_dict(template: dict, *args, **kwargs) -> dict:
        Dispersion._guard_invalid_params(list(kwargs.keys()), list(template.keys()))

        if (len(kwargs) + len(args)) > len(template):
            raise InvalidParameters("Too many parameters")

        params = template.copy()
        pos_arguments = set()

        for i, val in enumerate(args):
            key = list(template.keys())[i]
            params[key] = val
            pos_arguments.add(key)

        for key, value in kwargs.items():
            if key in pos_arguments:
                raise InvalidParameters(
                    f"Parameter {key} already set by positional argument"
                )
            params[key] = value

        return params

    def __init__(self, *args, **kwargs):
        super()
        self.rep_params = []

        self.single_params = self._fill_params_dict(
            self.single_params_template, *args, **kwargs
        )

    @abstractmethod
    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Calculates the dielectric function in a given wavelength window.

        Args:
            lbda (npt.ArrayLike): The wavelength window with unit nm.

        Returns:
            npt.NDArray: The dielectric function for each wavelength point.
        """

    def get_mat(self):
        """Returns this dispersion as an isotropic material"""
        return materials.IsotropicMaterial(self)

    def add(self, *args, **kwargs) -> "Dispersion":
        """Adds a set of parameters to the dispersion.

        Returns:
            Dispersion: The current object with the additional parameters added.
        """
        rep_param_set = self._fill_params_dict(
            self.rep_params_template, *args, **kwargs
        )
        self.rep_params.append(rep_param_set)

        return self

    def _check_valid_operand(self, other: Union[int, float, "Dispersion"]):
        if not isinstance(other, (int, float, Dispersion)):
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'"
            )

    def _is_non_std_dispersion(self, other: Union[int, float, "Dispersion"]) -> bool:
        return isinstance(other, (IndexDispersion, dispersions.Table))

    def __radd__(self, other: Union[int, float, "Dispersion"]) -> "DispersionSum":
        """Add up the dielectric function of multiple models"""
        return self.__add__(other)

    def __add__(self, other: Union[int, float, "Dispersion"]) -> "DispersionSum":
        """Add up the dielectric function of multiple models"""
        self._check_valid_operand(other)

        if self._is_non_std_dispersion(other):
            return other.__add__(self)

        if isinstance(other, DispersionSum):
            other.dispersions.append(self)
            return other

        if isinstance(other, (int, float)):
            return DispersionSum(self, dispersions.EpsilonInf(other))

        return DispersionSum(self, other)

    def get_dielectric(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns the dielectric constant for wavelength 'lbda' default unit (nm)
        in the convention ε1 + iε2."""
        return np.asarray(self.dielectric_function(lbda), dtype=np.complex128)

    def get_refractive_index(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns the refractive index for wavelength 'lbda' default unit (nm)
        in the convention n + ik."""
        return sqrt(self.dielectric_function(lbda))

    def get_dielectric_df(
        self, lbda: npt.ArrayLike = None, conjugate=False
    ) -> pd.DataFrame:
        """Returns the dielectric function as a pandas dataframe

        Args:
            lbda (npt.ArrayLike, optional): The wavelength range to use.
                If this parameter is not given a default spectral range
                from 200 to 1000 nm with 801 points is used.
                Defaults to None.
            conjugate (bool, optional): Per default the convention ε1 + iε2 is returned.
                If this flag is set to True, the ε1 + iε2 convention is returned.
                Defaults to False.

        Returns:
            pd.DataFrame:
                A pandas dataframe containing the wavelength as index
                and two rows containing ε1 and ε2.
        """
        lbda = np.linspace(200, 1000, 801) if lbda is None else lbda
        eps = self.get_dielectric(lbda)

        return pd.DataFrame(
            {"ϵ1": eps.real, "ϵ2": -eps.imag if conjugate else eps.imag},
            index=pd.Index(lbda, name="Wavelength"),
        )

    def get_refractive_index_df(
        self, lbda: npt.ArrayLike = None, conjugate=False
    ) -> pd.DataFrame:
        """Returns the refractive index as a pandas dataframe

        Args:
            lbda (npt.ArrayLike, optional): The wavelength range to use.
                If this parameter is not given a default spectral range
                from 200 to 1000 nm with 801 points is used.
                Defaults to None.
            conjugate (bool, optional): Per default the convention n + ik is returned.
                If this flag is set to True, the n + ik convention is returned.
                Defaults to False.

        Returns:
            pd.DataFrame:
                A pandas dataframe containing the wavelength as index
                and two rows containing n and k.
        """
        lbda = np.linspace(200, 1000, 801) if lbda is None else lbda
        nk = self.get_refractive_index(lbda)

        return pd.DataFrame(
            {"n": nk.real, "k": -nk.imag if conjugate else nk.imag},
            index=pd.Index(lbda, name="Wavelength"),
        )

    def __repr__(self):
        def _dict_to_str(dic):
            return ", ".join(f"{item[0]} = {item[1]}" for item in dic.items())

        return (
            type(self).__name__
            + "\n"
            + "=" * len(type(self).__name__)
            + "\n"
            + _dict_to_str(self.single_params)
            + (
                "\n\nOscillators\n"
                + "===========\n"
                + "\n".join(_dict_to_str(p) for p in self.rep_params)
                if len(self.rep_params) > 0
                else ""
            )
        )


class IndexDispersion(Dispersion):
    """A dispersion based on a refractive index formulation."""

    @abstractmethod
    def refractive_index(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Calculates the refractive index in a given wavelength window.

        Args:
            lbda (npt.ArrayLike): The wavelength window with unit nm.

        Returns:
            npt.NDArray: The refractive index for each wavelength point.
        """

    def __add__(self, other: Union[int, float, "Dispersion"]) -> "DispersionSum":
        self._check_valid_operand(other)

        if isinstance(other, IndexDispersion):
            raise NotImplementedError(
                "Adding of index based dispersions is not supported yet"
            )

        raise TypeError(
            "Cannot add refractive index and dielectric function based dispersions."
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.refractive_index(lbda) ** 2


class DispersionFactory:
    """A factory class for dispersion objects"""

    @staticmethod
    def get_dispersion(identifier: str, *args, **kwargs) -> Dispersion:
        """Creates a Dispersion object identified by its string name and initializes it with the
        given parameters.

        Args:
            identifier (str): Identifier of the Dispersion object, e.g. Cauchy.

        Returns:
            DispersionLaw: The Dispersion object initialized with the given parameters.
        """
        bad_identifier = ["Dispersion"]

        if hasattr(dispersions, identifier) and identifier not in bad_identifier:
            return getattr(dispersions, identifier)(*args, **kwargs)

        raise ValueError(f"No such dispersion: {identifier}")


class DispersionSum(Dispersion):
    """Represents a sum of two dispersions"""

    single_params_template: dict = {}
    rep_params_template: dict = {}
    dispersions: List[Dispersion]

    def __init__(self, *disps: Dispersion) -> None:
        super().__init__()
        self.dispersions = list(disps)

    def __add__(self, other: Union[int, float, "Dispersion"]) -> "DispersionSum":
        self._check_valid_operand(other)

        if self._is_non_std_dispersion(other):
            return other.__add__(self)

        if isinstance(other, DispersionSum):
            self.dispersions += other.dispersions
            return self

        if isinstance(other, (int, float)):
            self.dispersions.append(dispersions.EpsilonInf(eps=other))
            return self

        self.dispersions.append(other)
        return self

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        dielectric_function = sum(
            disp.dielectric_function(lbda) for disp in self.dispersions
        )
        return dielectric_function

    def __repr__(self):
        return (
            "DispersionSum\n"
            + "=" * 13
            + "\n\n"
            + "\n\n".join(map(str, self.dispersions))
        )
