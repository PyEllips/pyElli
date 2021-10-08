# Encoding: utf-8
from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt

from .dispersions import DispersionLaw
from .math import rotation_v_theta


class Material(ABC):
    """Base class for materials (abstract class).

    Method that should be implemented in derived classes:
    * getTensor(lbda) : returns the permittivity tensor for wavelength 'lbda'.
    """

    law_x = None
    law_y = None
    law_z = None
    rotated = False
    last_lbda_n = None
    last_lbda_e = None
    last_n = None
    last_e = None

    @abstractmethod
    def setDispersion(self) -> None:
        """Creates a new material -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def setRotation(self, R: npt.NDArray) -> None:
        """Rotates the Material.

        'R' : rotation matrix (from rotation_Euler() or others)
        """
        self.rotated = True
        self.rotationMatrix = R

    def getTensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns permittivity tensor matrix for the desired wavelength."""
        if np.array_equal(self.last_lbda_e, lbda):
            if isinstance(self.last_e, np.ndarray):
                return self.last_e

        self.last_lbda_e = lbda

        # Check for shape of lbda
        if type(lbda) == tuple:
            shape = np.shape(lbda[0])
        else:
            shape = np.shape(lbda)

        if shape == ():
            i = 1
        else:
            i = shape[0]

        # create empty tensor
        epsilon = np.zeros((i, 3, 3), dtype=np.complex128)

        # get get dielectric functions from dispersion law
        epsilon[:, 0, 0] = self.law_x.getDielectric(lbda)
        epsilon[:, 1, 1] = self.law_y.getDielectric(lbda)
        epsilon[:, 2, 2] = self.law_z.getDielectric(lbda)

        if self.rotated:
            epsilon = self.rotationMatrix @ epsilon @ self.rotationMatrix.T

        self.last_e = epsilon
        return epsilon

    def getRefractiveIndex(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns refractive index."""
        if np.array_equal(self.last_lbda_n, lbda):
            if isinstance(self.last_n, np.ndarray):
                return self.last_n

        self.last_lbda_n = lbda
        self.last_n = sqrt(self.getTensor(lbda))
        return self.last_n


class IsotropicMaterial(Material):
    """Isotropic material."""

    def __init__(self, law: DispersionLaw) -> None:
        """Creates isotropic material with dispersion law.

        'law' : Dispersion law object
        """
        self.setDispersion(law)

    def setDispersion(self, law: DispersionLaw) -> None:
        self.law_x = law
        self.law_y = law
        self.law_z = law


class UniaxialMaterial(Material):
    """Uniaxial material."""

    def __init__(self, law_o: DispersionLaw, law_e: DispersionLaw) -> None:
        """Creates a uniaxial material with dispersion law.

        'law_o' : dispersion law for ordinary crystal axes (x and y direction)
        'law_o' : dispersion law for extraordinary crystal axis (z direction)
        """
        self.setDispersion(law_o, law_e)

    def setDispersion(self, law_o: DispersionLaw, law_e: DispersionLaw) -> None:
        self.law_x = law_o
        self.law_y = law_o
        self.law_z = law_e


class BiaxialMaterial(Material):
    """Biaxial material."""

    def __init__(self, law_x: DispersionLaw, law_y: DispersionLaw, law_z: DispersionLaw) -> None:
        """Creates a biaxial material with dispersion law.

        'law_x' : dispersion law for x axis
        'law_y' : dispersion law for y axis
        'law_z' : dispersion law for z axis
        """
        self.setDispersion(law_x, law_y, law_z)

    def setDispersion(self, law_x: DispersionLaw, law_y: DispersionLaw, law_z: DispersionLaw) -> None:
        self.law_x = law_x
        self.law_y = law_y
        self.law_z = law_z
