"""Abstract base class and utility classes for pyElli dispersion"""
from abc import ABC, abstractmethod
import sys
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt
import pandas as pd


class Dispersion(ABC):
    """Dispersion (abstract class).

    Functions provided for derived classes:
    * dielectricFunction(lbda) : returns dielectric constant for wavelength 'lbda'
    """

    @property
    @abstractmethod
    def single_params_template(self) -> dict:
        """Specifies the single parameters of the model and its default values."""

    @property
    @abstractmethod
    def rep_params_template(self) -> dict:
        """Specifies the repeated parameters of the model and its default values."""

    def __init__(self, **kwargs):
        super()
        self.rep_params = []
        self.single_params = {}

        if not np.in1d(
            list(kwargs.keys()), list(self.single_params_template.keys())
        ).all():
            raise Exception("Unkown parameter set")

        for param in self.single_params_template.keys():
            if not param in kwargs:
                self.single_params[param] = self.single_params_template.get(param)
            else:
                self.single_params[param] = kwargs.get(param)

    @abstractmethod
    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """_summary_

        Args:
            lbda (npt.ArrayLike): _description_

        Returns:
            npt.NDArray: _description_
        """

    def add_param_set(self, **kwargs):
        if not np.in1d(
            list(self.rep_params_template.keys()), list(kwargs.keys())
        ).all():
            raise Exception("Not all params set")

        self.rep_params.append(kwargs)

        return self

    def __add__(self, other: "Dispersion") -> "Dispersion":
        """Add up the dielectric function of multiple models"""
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
            lbda (npt.ArrayLike, optional): The wavlength range to use.
                If this parameter is not given a default spectral range
                from 200 to 1000 nm with 500 points is used.
                Defaults to None.
            conjugate (bool, optional): Per default the convention ε1 + iε2 is returned.
                If this flag is set to True, the ε1 + iε2 convention is returned.
                Defaults to False.

        Returns:
            pd.DataFrame:
                A pandas dataframe containing the wavelength as index
                and two rows containing ε1 and ε2.
        """
        lbda = np.linspace(200, 1000, 500) if lbda is None else lbda
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
            lbda (npt.ArrayLike, optional): The wavlength range to use.
                If this parameter is not given a default spectral range
                from 200 to 1000 nm with 500 points is used.
                Defaults to None.
            conjugate (bool, optional): Per default the convention n + ik is returned.
                If this flag is set to True, the n + ik convention is returned.
                Defaults to False.

        Returns:
            pd.DataFrame:
                A pandas dataframe containing the wavelength as index
                and two rows containing n and k.
        """
        lbda = np.linspace(200, 1000, 500) if lbda is None else lbda
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
            + "\n\nOscillators\n"
            + "===========\n"
            + "\n".join(_dict_to_str(p) for p in self.rep_params)
        )


class DispersionFactory:
    """A factory class for dispersion law objects"""

    @staticmethod
    def get_dispersion(identifier: str) -> Dispersion:
        """Creates a DispersionLaw object identified by its string name and initializes it with the
        given parameters.

        Args:
            identifier (str): Identifier of the DispersionLaw object, e.g. DispersionCauchy.

        Returns:
            DispersionLaw: The DispersionLaw object initialized with the given parameters.
        """
        bad_classes = ["DispersionLaw", "DispersionFactory", "DispersionSum"]
        if identifier in bad_classes:
            raise ValueError(f"No valid dispersion: {identifier}")

        if hasattr(sys.modules[__name__], identifier):
            return getattr(sys.modules[__name__], identifier)

        raise ValueError(f"No such dispersion: {identifier}")

    @staticmethod
    def get_dispersion_short(identifier: str) -> Dispersion:
        """Creates a DispersionLaw object identified by
        its short string name and initializes it with the
        given parameters.

        Args:
            identifier (str): Identifier of the DispersionLaw object,
            e.g. DispersionCauchy, dispersion_cauchy or cauchy.

        Returns:
            DispersionLaw: The DispersionLaw object initialized with the given parameters.
        """
        gen_ident = identifier.strip().lower()
        if gen_ident.startswith("dispersion_"):
            disp_name = gen_ident.split("_")[1].capitalize()
            full_identifier = f"Dispersion{disp_name}"
        elif gen_ident.startswith("dispersion"):
            full_identifier = f"Dispersion{gen_ident[10:].capitalize()}"
        else:
            full_identifier = f"Dispersion{gen_ident.capitalize()}"

        return DispersionFactory.get_dispersion(full_identifier)


class DispersionSum(Dispersion):
    """Representation for a sum of two dispersions"""

    single_params_template = {}
    rep_params_template = {}

    def __init__(self, *dispersions: Dispersion) -> None:
        super().__init__()
        self.dispersions = dispersions

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        dielectric_function = np.sum(
            disp.dielectric_function(lbda) for disp in self.dispersions
        )
        return dielectric_function
