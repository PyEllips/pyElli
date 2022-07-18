# Encoding: utf-8
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt


if TYPE_CHECKING:
    from .dispersions.dispersions import Dispersion


class Material(ABC):
    """Base class for materials (abstract)."""

    @abstractmethod
    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the marterial for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """

    def get_refractive_index(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the refractive index tensor for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Refractive index tensor.
        """
        return sqrt(self.get_tensor(lbda))


class SingleMaterial(Material):
    """Base class for non mixed materials (abstract)."""

    dispersion_x = None
    dispersion_y = None
    dispersion_z = None
    rotated = False
    rotation_matrix = None

    @abstractmethod
    def set_dispersion(self) -> None:
        """Sets dispersion relation of the material."""

    def set_rotation(self, r: npt.NDArray) -> None:
        """Sets rotation of the Material.

        Args:
            r (npt.NDArray): rotation matrix (from rotation_Euler() or others)
        """
        self.rotated = True
        self.rotation_matrix = r

    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the marterial for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        # Check for shape of lbda
        shape = np.shape(lbda)
        if shape == ():
            i = 1
        else:
            i = shape[0]

        # create empty tensor
        epsilon = np.zeros((i, 3, 3), dtype=np.complex128)

        # get get dielectric functions from dispersion
        epsilon[:, 0, 0] = self.dispersion_x.get_dielectric(lbda)
        epsilon[:, 1, 1] = self.dispersion_y.get_dielectric(lbda)
        epsilon[:, 2, 2] = self.dispersion_z.get_dielectric(lbda)

        if self.rotated:
            epsilon = self.rotation_matrix @ epsilon @ self.rotation_matrix.T

        return epsilon


class IsotropicMaterial(SingleMaterial):
    """Isotropic material."""

    def __init__(self, dispersion: "Dispersion") -> None:
        """Creates isotropic material with a dispersion.

        Args:
            dispersion (Dispersion): Dispersion relation of all three crystal directions.
        """
        self.set_dispersion(dispersion)

    def set_dispersion(self, dispersion: "Dispersion") -> None:
        """Sets dipsersion relation of the isotropic material.

        Args:
            dispersion (Dispersion): Dispersion relation of all three crystal directions.
        """
        self.dispersion_x = dispersion
        self.dispersion_y = dispersion
        self.dispersion_z = dispersion


class UniaxialMaterial(SingleMaterial):
    """Uniaxial material."""

    def __init__(self, dispersion_o: "Dispersion", dispersion_e: "Dispersion") -> None:
        """Creates a uniaxial material with two dispersions.

        Args:
            dispersion_o (Dispersion): Dispersion relation for ordinary crystal axes (x and y direction).
            dispersion_e (Dispersion): Dispersion relation for extraordinary crystal axis (z direction).
        """
        self.set_dispersion(dispersion_o, dispersion_e)

    def set_dispersion(self, dispersion_o: "Dispersion", dispersion_e: "Dispersion") -> None:
        """Sets dipsersion relations of the uniaxial material.

        Args:
            dispersion_o (Dispersion): Dispersion relation for ordinary crystal axes (x and y direction).
            dispersion_e (Dispersion): Dispersion relation for extraordinary crystal axis (z direction).
        """
        self.dispersion_x = dispersion_o
        self.dispersion_y = dispersion_o
        self.dispersion_z = dispersion_e


class BiaxialMaterial(SingleMaterial):
    """Biaxial material."""

    def __init__(
        self,
        dispersion_x: "Dispersion",
        dispersion_y: "Dispersion",
        dispersion_z: "Dispersion",
    ) -> None:
        """Creates a biaxial material with three dispersions.

        Args:
            dispersion_x (Dispersion): Dispersion relation for x crystal axes.
            dispersion_y (Dispersion): Dispersion relation for y crystal axes.
            dispersion_z (Dispersion): Dispersion relation for z crystal axes.
        """
        self.set_dispersion(dispersion_x, dispersion_y, dispersion_z)

    def set_dispersion(
        self,
        dispersion_x: "Dispersion",
        dispersion_y: "Dispersion",
        dispersion_z: "Dispersion",
    ) -> None:
        """Sets dipsersion relations of the biaxial material.

        Args:
            dispersion_x (Dispersion): Dispersion relation for x crystal axes.
            dispersion_y (Dispersion): Dispersion relation for y crystal axes.
            dispersion_z (Dispersion): Dispersion relation for z crystal axes.
        """
        self.dispersion_x = dispersion_x
        self.dispersion_y = dispersion_y
        self.dispersion_z = dispersion_z


class MixtureMaterial(Material):
    """Abstract Class for mixed materials."""

    host_material = None
    guest_material = None
    fraction = None

    def __init__(
        self, host_material: Material, guest_material: Material, fraction: float
    ) -> None:
        """Creates a material mixture from two materials.

        Args:
            host_material (Material): Host Material.
            guest_material (Material): Material incorporated in the host.
            fraction (float): Fraction of the guest material (Range 0 - 1).
        """
        self.set_constituents(host_material, guest_material)
        self.set_fraction(fraction)

    def set_constituents(
        self, host_material: Material, guest_material: Material
    ) -> None:
        """Sets Materials in the mixture.

        Args:
            host_material (Material): Host Material.
            guest_material (Material): Material incorporated in the host.
        """
        self.host_material = host_material
        self.guest_material = guest_material

    def set_fraction(self, fraction: float) -> None:
        """Sets fraction and checks if fraction is in range from 0 to 1.

        Args:
            fraction (float): Fraction of the guest material (Range 0 - 1).
        """
        if not 0 <= fraction <= 1:
            raise ValueError("Fractions not in range from 0 to 1")

        self.fraction = fraction

    @abstractmethod
    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the marterial for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """


class VCAMaterial(MixtureMaterial):
    """Mixture Material approximated with a simple virtual crystal like average."""

    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the marterial for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        epsilon = (
            self.host_material.get_tensor(lbda) * (1 - self.fraction)
            + self.guest_material.get_tensor(lbda) * self.fraction
        )
        return epsilon


class LooyengaEMA(MixtureMaterial):
    """Mixture Material approximated with Looyenga's formula.
    Valid if materials have small contrast.
    Looyenga, H. (1965). Physica, 31(3), 401–406.
    """

    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the marterial for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        epsilon = (
            self.host_material.get_tensor(lbda) ** (1 / 3) * (1 - self.fraction)
            + self.guest_material.get_tensor(lbda) ** (1 / 3) * self.fraction
        ) ** 3
        return epsilon


class MaxwellGarnettEMA(MixtureMaterial):
    """Mixture Material approximated with the Maxwell Garnett formula.
    It is valid for spherical inclusions with small volume fraction.
    """

    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the marterial for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        e_h = self.host_material.get_tensor(lbda)
        e_g = self.guest_material.get_tensor(lbda)

        epsilon = (
            e_h
            * (2 * self.fraction * (e_g - e_h) + e_g + 2 * e_h)
            / (2 * e_h + e_g - self.fraction * (e_g - e_h))
        )
        return epsilon
