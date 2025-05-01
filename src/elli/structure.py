# Encoding: utf-8
"""The virtual representation of a sample is finally build
using the Structure class.

A :class:`Structure` consists of one IsotropicMaterial used as semi-infinite
entry material and a second arbitrary Material as exit material.
A list of Layers can be added as desired in between these materials,
to create a 1D model of layered media.

The basic :class:`Layer` consists of a material and an assigned thickness.
An arbitrary sequence of layers can be stacked and repeated by :class:`RepeatedLayers`,
to create Bragg-mirror or multiple quantum well structures.

There are also classes to approximate layers with varying properties along the z-axis
(inhomogeneous layers) by creating multiple thinner homogeneous slices:

* :class:`TwistedLayer` is able to represent rotating materials, like twisted nematic materials.
* :class:`VaryingMixtureLayer` takes an :class:`MixtureMaterial<elli.materials.MixtureMaterial>` and uses a gradient as mixture fraction.
"""

from abc import ABC, abstractmethod
from typing import Callable, List, Tuple

import numpy as np
import numpy.typing as npt

from .experiment import Experiment
from .materials import IsotropicMaterial, Material, MixtureMaterial
from .result import Result
from .solver import Solver
from .solver4x4 import Solver4x4
from .utils import E_Z, rotation_v_theta


class AbstractLayer(ABC):
    """Abstract class for a layer."""

    @abstractmethod
    def get_permittivity_profile(
        self, lbda: npt.ArrayLike
    ) -> List[Tuple[float, npt.NDArray]]:
        """Returns the permittivity profile of the layer for the given wavelengths.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            List[Tuple[float, npt.NDArray]]:
                Returns list of tuples [(thickness, dielectric tensor), ...]
        """


class RepeatedLayers(AbstractLayer):
    """Repeated structure of layers."""

    repetitions = None  # Number of repetitions
    before = None  # additional layers before the first period
    after = None  # additional layers after the last period
    layers = None  # layers to repeat

    def __init__(
        self,
        layers: List[AbstractLayer],
        repetitions: int,
        before: int = 0,
        after: int = 0,
    ) -> None:
        """Create a repeated structure of layers.

        Example : For layers [1,2,3] with n=2, before=1 and after=0, the structure will be 3123123.

        Args:
            layers (List[AbstractLayer]): List of the repeated layers, starting from z=0
            repetitions (int): Number of repetitions
            before (int, optional):
                Number of additional layers before the first period. Defaults to 0.
            after (int, optional): Number of additional layers after the last period. Defaults to 0.
        """
        self.set_repetitions(repetitions, before, after)
        self.set_layers(layers)

    def set_repetitions(
        self, repetitions: int, before: int = 0, after: int = 0
    ) -> None:
        """Defines the number of repetitions and the first and last layers.

        Example : For layers [1,2,3] with n=2, before=1 and after=0, the structure will be 3123123.

        Args:
            repetitions (int): Number of repetitions
            before (int, optional):
                Number of additional layers before the first period. Defaults to 0.
            after (int, optional): Number of additional layers after the last period. Defaults to 0.
        """
        if repetitions < 1:
            raise ValueError("Number of repetitions need to be at least 1.")

        if before < 0:
            raise ValueError("Before value needs to be 0 or more.")

        if after < 0:
            raise ValueError("Divisions needs to be 0 or more.")

        self.repetitions = repetitions
        self.before = before
        self.after = after

    def set_layers(self, layers: List[AbstractLayer]) -> None:
        """Set list of layers.

        Args:
            layers (List[AbstractLayer]): List of the repeated layers, starting from z=0
        """
        if not isinstance(layers, list):
            raise TypeError("Provide a list of layers.")
        for layer in layers:
            if not isinstance(layer, AbstractLayer):
                raise TypeError(
                    f"Expected a list of Layer objects but found an item of type {type(layer)}."
                )

        self.layers = layers

    def get_permittivity_profile(
        self, lbda: npt.ArrayLike
    ) -> List[Tuple[float, npt.NDArray]]:
        """Returns the permittivity profile of the layer for the given wavelengths.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            List[Tuple[float, npt.NDArray]]:
                Returns list of tuples [(thickness, dielectric tensor), ...]
        """
        layers = []
        for layer in self.layers:
            layers += layer.get_permittivity_profile(lbda)

        if self.before > 0:
            before = layers[-self.before :]
        else:
            before = []
        return before + self.repetitions * layers + layers[: self.after]


class Layer(AbstractLayer):
    """Homogeneous layer of dielectric material."""

    thickness = None

    def __init__(self, material: Material, thickness: float) -> None:
        """New layer of material 'material', with thickness 'thickness'

        Args:
            material (Material): Material object
            thickness (float): Thickness of layer (in nm)
        """
        self.set_material(material)
        self.set_thickness(thickness)

    def set_thickness(self, thickness: float) -> None:
        """Defines the thickness of the layer in nm.

        Args:
            thickness (float): Thickness of the layer in nm.
        """
        if thickness < 0:
            raise ValueError("Thickness value can't be negative.")

        self.thickness = thickness

    def set_material(self, material: Material) -> None:
        """Defines the material for the layer.

        Args:
            material (Material): Material object
        """
        if not isinstance(material, Material):
            raise TypeError(
                f"Expected material to be an Material object but found type {type(material)}."
            )

        self.material = material

    def get_permittivity_profile(
        self, lbda: npt.ArrayLike
    ) -> List[Tuple[float, npt.NDArray]]:
        """Returns the permittivity profile of the layer for the given wavelengths.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            List[Tuple[float, npt.NDArray]]:
                Returns a list containing one tuple [(thickness, dielectric tensor)]
        """
        return [(self.thickness, self.material.get_tensor(lbda))]


#########################################################
# Inhomogeneous Layers


class InhomogeneousLayer(AbstractLayer):
    """Abstract base class for inhomogeneous layers with varying properties in z-direction."""

    thickness = None
    material = None
    div = None

    def set_thickness(self, thickness: float) -> None:
        """Defines the thickness of the layer in nm.

        Args:
            thickness (float): Thickness of the layer in nm.
        """
        if thickness < 0:
            raise ValueError("Thickness value can't be negative.")

        self.thickness = thickness

    def set_material(self, material: Material) -> None:
        """Defines the material for the layer.

        Args:
            material (Material): Material object
        """
        if not isinstance(material, Material):
            raise TypeError(
                f"Expected material to be an Material object but found type {type(material)}."
            )

        self.material = material

    def set_divisions(self, div: int) -> None:
        """Defines the number of slices to simulate the layer.

        Args:
            div (int): Number of slices for the layer
        """
        if div < 1:
            raise ValueError("Number of slices need to be at least 1.")

        self.div = div

    def get_slices(self) -> npt.NDArray:
        """Returns z slicing with the position relative to this layer, not to the whole structure.

        Returns:
            npt.NDArray: array of 'z' positions [z0, z1,... , zmax], with z0 = 0 and zmax = z{d+1}
        """
        return np.linspace(0, self.thickness, self.div + 1)

    @abstractmethod
    def get_tensor(self, z: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns permittivity tensor matrix for position 'z'."""

    def get_permittivity_profile(self, lbda: npt.ArrayLike) -> List:
        """Returns the permittivity profile of the layer for the given wavelengths.
        The tensor is evaluated in the middle of each slice.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            List[Tuple[float, npt.NDArray]]:
                Returns list of tuples [(d1, epsilon1), (d2, epsilon2), ...]
        """
        z = self.get_slices()
        h = np.diff(z)
        zmid = (z[:-1] + z[1:]) / 2.0
        tensor = [self.get_tensor(z, lbda) for z in zmid]
        return list(zip(h, tensor))


class TwistedLayer(InhomogeneousLayer):
    """Twisted layer.
    The material gets rotated around the z axis."""

    def __init__(
        self, material: Material, thickness: float, div: int, angle: float
    ) -> None:
        """Creates a layer with a twisted material.

        Args:
            material (Material): Material object
            thickness (float): Thickness of layer (in nm)
            div (int): Number of slices for the layer
            angle (float): rotation angle over the distance 'd' (in degrees)
        """
        self.set_material(material)
        self.set_thickness(thickness)
        self.set_divisions(div)
        self.set_angle(angle)

    def set_angle(self, angle: float) -> None:
        """Defines the total twist angle of this layer.

        Args:
            angle (float): Rotation angle over the thickness 'd' of the layer (in degrees)
        """
        self.angle = angle

    def get_tensor(self, z: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets permittivity tensor matrix for position 'z' and wavelength 'lbda'.

        Args:
            z (float): Position in the layer (in nm)
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor for position 'z' and wavelength 'lbda'.
        """
        epsilon = self.material.get_tensor(lbda)
        m_r = rotation_v_theta(E_Z, self.angle * z / self.thickness)
        return m_r @ epsilon @ m_r.T


class VaryingMixtureLayer(InhomogeneousLayer):
    """Mixture layer, with varying fraction dependent on z Position.

    Note: The set fraction of the mixture material will be ignored
    and replaced by the result of the fraction modulation function.
    """

    def __init__(
        self,
        material: MixtureMaterial,
        thickness: float,
        div: int,
        fraction_modulation: Callable[[float], float] = lambda x: x,
    ) -> None:
        """
        Args:
            material (MixtureMaterial): MixtureMaterial object
            d (float): Thickness of layer (in nm)
            div (int): Number of slices for the layer
            fraction_modulation (Callable[[float], float]):
                Function to modify the fraction amount,
                takes float from 0 to 1 (top to bottom of layer),
                should return fraction at that level.
                Defaults to a linear profile
                (100% host material to 100% guest material).
        """
        self.set_material(material)
        self.set_thickness(thickness)
        self.set_divisions(div)
        self.set_fraction_modulation(fraction_modulation)

    def set_material(self, material: MixtureMaterial) -> None:
        """Defines the material for the varying mixture layer.

        Args:
            material (MixtureMaterial): Material object
        """
        if not isinstance(material, MixtureMaterial):
            raise TypeError(
                f"Expected material to be an MixtureMaterial object but found type {type(material)}."
            )

        self.material = material

    def set_fraction_modulation(
        self, fraction_modulation: Callable[[float], float] = lambda x: x
    ) -> None:
        """Sets function for variation of the mixture over the layer

        Args:
            fraction_modulation (Callable[[float], float]):
                Function to modify the fraction amount,
                takes float from 0 to 1 (top to bottom of layer),
                should return fraction at that level.
                Defaults to a linear profile
                (100% host material to 100% guest material).
        """
        self.fraction_modulation = fraction_modulation

    def get_tensor(self, z: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets permittivity tensor matrix for position 'z' and wavelength 'lbda'.

        Args:
            z (float): Position in the layer (in nm)
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor for position 'z' and wavelength 'lbda'.
        """
        epsilon = self.material.get_tensor_fraction(
            lbda, self.fraction_modulation(z / self.thickness)
        )
        return epsilon


#########################################################
# Structure Class


class Structure:
    """Description of the whole structure.

    Consists of:

    * front half-space (incident)
    * layer succession
    * back half-space (exit)
    """

    front_material = None
    back_material = None
    layers = []  # list of layers

    def __init__(
        self, front: IsotropicMaterial, layers: List[Layer], back: Material
    ) -> None:
        """
        Args:
            front (IsotropicMaterial): IsotropicMaterial used as front half space
            layers (List[Layer]): List of Layers, starting from z=0
            back (Material): Material used as back half space
        """
        self.set_front_material(front)
        self.set_layers(layers)
        self.set_back_material(back)

    def set_front_material(self, material: IsotropicMaterial) -> None:
        """Defines the front half-space material. Has to be isotropic.

        Args:
            material (IsotropicMaterial): IsotropicMaterial used as front half space
        """
        if not isinstance(material, Material):
            raise TypeError(
                f"Expected front material to be an Material object but found type {type(material)}."
            )

        self.front_material = material

    def set_back_material(self, material: Material) -> None:
        """Defines the back half-space material.

        Args:
            material (Material): Material used as back half space
        """
        if not isinstance(material, Material):
            raise TypeError(
                f"Expected back material to be an Material object but found type {type(material)}."
            )

        self.back_material = material

    def set_layers(self, layers: List[Layer]) -> None:
        """Sets sequence of layers.

        Args:
            layers (List[Layer]): List of Layers, starting from z=0
        """
        if not isinstance(layers, list):
            raise TypeError("Provide a list of layers.")
        for layer in layers:
            if not isinstance(layer, AbstractLayer):
                raise TypeError(
                    f"Expected a list of Layer objects but found an item of type {type(layer)}."
                )

        self.layers = layers

    def get_permittivity_profile(
        self, lbda: npt.ArrayLike
    ) -> List[Tuple[float, npt.NDArray]]:
        """Returns the permittivity profile of the complete structure for the given wavelengths.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            List[Tuple[float, npt.NDArray]]:
                Returns list of tuples [(thickness, dielectric tensor), ...]
        """
        permittivity_profile = [(np.inf, self.front_material.get_tensor(lbda))]

        for layer in self.layers:
            permittivity_profile.extend(layer.get_permittivity_profile(lbda))

        permittivity_profile.extend([(np.inf, self.back_material.get_tensor(lbda))])
        return permittivity_profile

    def evaluate(
        self,
        lbda: npt.ArrayLike,
        theta_i: float,
        solver: Solver = Solver4x4,
        **solver_kwargs,
    ) -> Result:
        """Return the Evaluation of the structure for the given parameters with standard settings.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).
            theta_i (float): Incident angle of the experiment (in degrees).
            solver (Solver, optional): Choose which solver class is used. Defaults to Solver4x4.
            solver_kwargs (optional): Keyword arguments for the Solver can be appended as arguments.

        Returns:
            Result: Result of the experiment.
        """
        exp = Experiment(self, lbda, theta_i)
        return exp.evaluate(solver, **solver_kwargs)
