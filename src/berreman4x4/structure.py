# Encoding: utf-8
from abc import ABC, abstractmethod
from .materials import Material, MixtureMaterial
import numpy as np
import numpy.typing as npt
from typing import List, Tuple, Callable

from .experiment import Experiment
from .math import rotation_v_theta
from .solver import Solver
from .solver4x4 import Solver4x4
from .result import Result


class AbstractLayer(ABC):

    def setThickness(self, d: float) -> None:
        """Defines the thickness of this homogeneous layer in nm."""
        self.d = d

    @abstractmethod
    def getPermittivityProfile(self, lbda: npt.ArrayLike) -> List[Tuple[float, npt.NDArray]]:
        pass


class RepeatedLayers(AbstractLayer):
    """Repetition of a structure."""

    n = None        # Number of repetitions
    before = None   # additional layers before the first period
    after = None    # additional layers after the last period
    layers = None   # layers to repeat

    def __init__(self, layers: List[AbstractLayer], n: int, before: int = 0, after: int = 0) -> None:
        """Repeated structure of layers

        'layers' : list of the repeated layers
        'n' : number of repetitions
        'before', 'after' : see method setRepetition()
        """
        self.setRepetition(n, before, after)
        self.setLayers(layers)

    def setRepetition(self, n: int, before: int = 0, after: int = 0) -> None:
        """Defines the number of repetitions.

        'n' : number of repetitions
        'before' : number of additional layers before the first period
        'after' : number of additional layers after the last period

        Example : For layers [1,2,3] with n=2, before=1 and after=0, the
        structure will be 3123123.
        """
        self.n = n
        self.before = before
        self.after = after

    def setLayers(self, layers: List[AbstractLayer]) -> None:
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPermittivityProfile(self, lbda: npt.ArrayLike) -> List[Tuple[float, npt.NDArray]]:
        """Returns permittivity tensor profile.

        Returns list of tuples [(d1, epsilon1), (d2, epsilon2), ... ]
        """
        layers = []
        for L in self.layers:
            layers += L.getPermittivityProfile(lbda) 

        if self.before > 0:
            before = layers[-self.before:]
        else:
            before = []
        return before + self.n * layers + layers[:self.after]


class Layer(AbstractLayer):
    """Homogeneous layer finite of dielectric material."""

    def __init__(self, material: Material, d: float) -> None:
        """New layer of material 'material', with thickness 'd'

        'material' : Material object
        'd'        : Thickness of layer in nm
        """
        self.setMaterial(material)
        self.setThickness(d)

    def setMaterial(self, material: Material) -> None:
        """Defines the material for this layer. """
        self.material = material

    def getPermittivityProfile(self, lbda: npt.ArrayLike) -> List[Tuple[float, npt.NDArray]]:
        """Returns permittivity tensor profile.

        Returns a list containing one tuple: [(d, epsilon)]
        """
        return [(self.d, self.material.getTensor(lbda))]


#########################################################
# Inhomogeneous Layers

class InhomogeneousLayer(Layer):
    """Abstract base class for 
    inhomogeneous layers with varying properties in z-direction."""

    def setDivision(self, div: int) -> None:
        """Defines the number of slices to simulate this TwistedLayer"""
        self.div = div

    def getSlices(self) -> npt.NDArray:
        """Returns z slicing.

        Returns : array of 'z' positions [z0, z1,... , zmax], 
                  with z0 = 0 and zmax = z{d+1}

        Notes:
        * The number of divisions is 'div' (see constructor)
        * Position is relative to this material, not to the whole structure.
        """
        return np.linspace(0, self.d, self.div+1)

    @abstractmethod
    def getTensor(self, z: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns permittivity tensor matrix for position 'z'."""
        pass

    def getPermittivityProfile(self, lbda: npt.ArrayLike) -> List:
        """Returns permittivity tensor profile.

        Tensor is evaluated in the middle of each slice.
        Returns list [(d1, epsilon1), (d2, epsilon2), ... ]
        """
        z = self.getSlices()
        h = np.diff(z)
        zmid = (z[:-1] + z[1:]) / 2.
        tensor = [self.getTensor(z, lbda) for z in zmid]
        return list(zip(h, tensor))


class TwistedLayer(InhomogeneousLayer):
    """Twisted layer."""

    def __init__(self, material: Material, d: float, div: int, angle: float) -> None:
        """Creates a layer with a twisted material.

        'material' : Material object
        'd'        : Thickness of layer in nm
        'angle' : rotation angle for distance 'd'
        'div' : number of slices
        """
        self.setMaterial(material)
        self.setThickness(d)
        self.setDivision(div)
        self.setAngle(angle)

    def setAngle(self, angle: float) -> None:
        """Defines the total twist angle of this TwistedLayer."""
        self.angle = angle

    def getTensor(self, z: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns permittivity tensor matrix for position 'z'."""
        epsilon = self.material.getTensor(lbda)
        R = rotation_v_theta([0, 0, 1], self.angle * z / self.d)
        return R @ epsilon @ R.T


class VaryingMixtureLayer(InhomogeneousLayer):
    """Mixture layer, with varying fraction."""

    def __init__(self, material: MixtureMaterial, d: float, div: int, fraction_modulation: Callable[[float], float]) -> None:
        """Creates a layer with a twisted material.

        'material' : MixtureMaterial object
        'd'        : Thickness of layer in nm
        'div'      : number of slices
        'fraction_modulation' : function to modify the fraction amount, 
                                takes float from 0 to 1 (top to bottom of layer), returns fraction at that level
        """
        self.setMaterial(material)
        self.setThickness(d)
        self.setDivision(div)
        self.fraction_modulation = fraction_modulation

    def getTensor(self, z: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns permittivity tensor matrix for position 'z'."""
        self.material.setFraction(self.fraction_modulation(z / self.d))
        epsilon = self.material.getTensor(lbda)
        return epsilon


#########################################################
# Structure Class

class Structure:
    """Description of the whole structure.

    * front half-space (incident), must be isotropic
    * back half-space (exit), may be anisotropic
    * layer succession
    """
    frontMaterial = None
    backMaterial = None
    layers = []  # list of layers

    def __init__(self, front: Material, layers: List[Layer], back: Material) -> None:
        """Creates an empty structure.

        'front' : front half space, see setFrontHalfSpace()
        'layers' : layer list, see setLayers()
        'back' : back half space, see setBackHalfSpace()
        """
        self.setFrontMaterial(front)
        self.setLayers(layers)
        self.setBackMaterial(back)

    def setFrontMaterial(self, material: Material) -> None:
        """Defines the front half-space material.

        'material' : Material object
        """
        self.frontMaterial = material

    def setBackMaterial(self, material: Material) -> None:
        """Defines the back half-space material.

        'material' : Material object
        """
        self.backMaterial = material

    def setLayers(self, layers: List[Layer]) -> None:
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPermittivityProfile(self, lbda) -> List:
        """Get permittivity profile of the complete structure for the wavelengths lbda.
        """
        permProfile = [self.frontMaterial.getTensor(lbda)]

        for L in self.layers:
            permProfile.extend(L.getPermittivityProfile(lbda))

        permProfile.extend([self.backMaterial.getTensor(lbda)])
        return permProfile

    def evaluate(self, lbda, theta_i, solver: Solver = Solver4x4, **solver_kwargs) -> Result:
        """Return the Evaluation of the structure for the given parameters with standard settings"""
        exp = Experiment(self, lbda, theta_i)
        return exp.evaluate(solver, **solver_kwargs)
