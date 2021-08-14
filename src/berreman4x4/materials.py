# Encoding: utf-8
from abc import ABC, abstractmethod
import numpy as np
from numpy.lib.scimath import sqrt

from .math import unitConversion, rotation_v_theta
from .settings import settings


class Material(ABC):
    """Base class for materials (abstract class).

    Method that should be implemented in derived classes:
    * getTensor(lbda) : returns the permittivity tensor for wavelength 'lbda'.
    """

    law_x = None
    law_y = None
    law_z = None
    rotationMatrix = np.identity(3)

    @abstractmethod
    def setDispersion(self):
        """Creates a new material -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def setRotation(self, R):
        """Rotates the Material.

        'R' : rotation matrix (from rotation_Euler() or others)
        """
        self.rotationMatrix = R

    def getTensor(self, lbda):
        """Returns permittivity tensor matrix for the desired wavelength."""

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
        epsilon = np.zeros((i, 3, 3), dtype=settings['dtype'])

        # get get dielectric functions from dispersion law
        epsilon[:, 0, 0] = self.law_x.getDielectric(lbda)
        epsilon[:, 1, 1] = self.law_y.getDielectric(lbda)
        epsilon[:, 2, 2] = self.law_z.getDielectric(lbda)

        epsilon = self.rotationMatrix @ epsilon @ self.rotationMatrix.T
        return epsilon

    def getRefractiveIndex(self, lbda):
        """Returns refractive index."""
        return sqrt(self.getTensor(lbda))


class IsotropicMaterial(Material):
    """Isotropic material."""

    def __init__(self, law=None):
        """Creates isotropic material with dispersion law.

        'law' : Dispersion law object
        """
        self.law_x = law
        self.law_y = law
        self.law_z = law


class UniaxialMaterial(Material):
    """Uniaxial material."""

    def __init__(self, law_o=None, law_e=None):
        """Creates a uniaxial material with dispersion law.

        'law_o' : dispersion law for ordinary crystal axes (x and y direction)
        'law_o' : dispersion law for extraordinary crystal axis (z direction)
        """
        self.law_x = law_o
        self.law_y = law_o
        self.law_z = law_e


class BiaxialMaterial(Material):
    """Biaxial material."""

    def __init__(self, law_x=None, law_y=None, law_z=None):
        """Creates a biaxial material with dispersion law.

        'law_x' : dispersion law for x axis
        'law_y' : dispersion law for y axis
        'law_z' : dispersion law for z axis
        """
        self.law_x = law_x
        self.law_y = law_y
        self.law_z = law_z


#########################################################
# Inhomogeneous materials...


class InhomogeneousMaterial:
    """Base class for inhomogeneous materials (abstract class).

    Method that should be implemented in derived classes:
    * getTensor(z, lbda) : permittivity tensor at position z
    * getSlices() : returns z_i, position of the slices
    """

    def __init__(self):
        """Creates a new inhomogeneous material -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def getTensor(self, z, lbda):
        """Returns permittivity tensor for position 'z' and wavelength 'lbda'.

        'z' : position where the tensor is evaluated
        'lbda' : wavelength
        """
        raise NotImplementedError("Should be implemented in derived classes")

    def getSlices(self):
        """Returns z slicing (including z0 and zmax).

        Origin of 'z' is not important, only relative positions matter.
        """
        raise NotImplementedError("Should be implemented in derived classes")


class TwistedMaterial(InhomogeneousMaterial):
    """Twisted material.

    Used to describe twisted nematic or cholesteric liquid crystal for example.
    """

    material = None  # Material for the twisted layer
    d = None  # Thickness of the layer
    angle = None  # Angle of the twist
    div = None  # Number of slices

    def __init__(self, material, d, angle=90, div=25):
        """Creates a layer with a twisted material.

        'material' : material for the twisted layer
        'd' : thickness of the layer in nm or tuple (thickness, unit)
        'angle' : rotation angle for distance 'd'
        'div' : number of slices

        Note: Let us call h = d / div. It is useful to assess whether k0·h is
        greater or smaller than 1. If it is greater than 1, evaluation of the
        exponential for the propagator will not be possible with linear
        expansion, and may require a Taylor expansion with a very high order
        for convergence. In this case, use the Padé approximation or the
        exact result with eigenvector decomposition. On the other hand, if
        k0·h is small, a linear or Taylor approximation may suffice.
        """
        self.setThickness(d)
        self.setMaterial(material)
        self.setAngle(np.deg2rad(angle))
        self.setDivision(div)

    def setDivision(self, div):
        """Defines the number of slices in this TwistedMaterial."""
        self.div = div

    def setAngle(self, angle):
        """Defines the total twist angle of this TwistedMaterial."""
        self.angle = angle

    def setMaterial(self, material):
        """Defines the material making this TwistedMaterial."""
        self.material = material

    def setThickness(self, d):
        """Defines the thickness of this TwistedMaterial."""
        self.d = unitConversion(d)

    def getTensor(self, z, lbda):
        """Returns permittivity tensor matrix for position 'z'."""
        epsilon = self.material.getTensor(lbda)
        R = rotation_v_theta([0, 0, 1], self.angle * z / self.d)
        return R @ epsilon @ R.T

    def getSlices(self):
        """Returns z slicing.

        Returns : array of 'z' positions [z0, z1,... , zmax],
                  with z0 = 0 and zmax = z{d+1}

        Notes:
        * The number of divisions is 'div' (see constructor)
        * Position is relative to this material, not to the whole structure.
        """
        return np.linspace(0, self.d, self.div+1)
