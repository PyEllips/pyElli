# Encoding: utf-8
from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt
from typing import List, Tuple

from .dispersions import DispersionLaw
from .math import rotation_v_theta


class Material(ABC):
    """Base class for materials (abstract class).

    Method that should be implemented in derived classes:
    * getTensor(lbda) : returns the permittivity tensor for wavelength 'lbda'.
    """

    @abstractmethod
    def getTensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        pass

    def getRefractiveIndex(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns refractive index for wavelength 'lbda'."""
        return sqrt(self.getTensor(lbda))


class SingleMaterial(Material):
    """Base class for single materials (abstract class).

    Method that should be implemented in derived classes:
    * getTensor(lbda) : returns the permittivity tensor for wavelength 'lbda'.
    """

    law_x = None
    law_y = None
    law_z = None
    rotated = False

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
        # Check for shape of lbda
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

        return epsilon


class IsotropicMaterial(SingleMaterial):
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


class UniaxialMaterial(SingleMaterial):
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


class BiaxialMaterial(SingleMaterial):
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


class MixtureMaterial(Material):
    """Abstract Class for mixed materials"""

    def __init__(self, host_material: Material, guest_material: Material, fraction: float) -> None:
        """Creates a material mixture from two materials

        'host_material': Host Material
        'guest_material': Material incorporated in the host
        'fraction' : Fraction of the guest material (Range 0 - 1) 
        """
        self.setConstituents(host_material, guest_material)
        self.setFraction(fraction)

    def setConstituents(self, host_material: Material, guest_material: Material) -> None:
        """ Sets Materials in the mixture
        'host_material': Host Material
        'guest_material': Material incorporated in the host
        """
        self.host_material = host_material
        self.guest_material = guest_material

    def setFraction(self, fraction: float) -> None:
        """ Sets fraction and checks if fraction is in range from 0 to 1.
        'fraction' : Fraction of the guest material (Range 0 - 1)
        """
        if not 0 <= fraction <= 1:
            raise ValueError('Fractions not in range from 0 to 1')

        self.fraction = fraction

    @abstractmethod
    def getTensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        pass


class VCAMaterial(MixtureMaterial):
    """Mixture Material approximated with a simple virtual crystal like average."""

    def getTensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        epsilon = self.host_material.getTensor(lbda) * (1 - self.fraction) \
            + self.guest_material.getTensor(lbda) * self.fraction
        return epsilon


class MaxwellGarnetEMA(MixtureMaterial):
    """Mixture Material approximated with the Maxwell Garnet formula.
       It is valid for spherical inclusions with small volume fraction.
    """

    def getTensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        e_h = self.host_material.getTensor(lbda)
        e_g = self.guest_material.getTensor(lbda)

        epsilon = e_h * (2 * self.fraction * (e_g - e_h) + e_g + 2 * e_h) \
            / (2 * e_h + e_g - self.fraction * (e_g - e_h))
        return epsilon
