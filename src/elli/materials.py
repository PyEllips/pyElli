# Encoding: utf-8
"""The Materials submodule provides the classes to build
complex materials from :doc:`dispersion models<dispersions>`.

The simplest provided material is the
:class:`IsotropicMaterial<elli.materials.IsotropicMaterial>`.
It takes only one Dispersion which is used for all three axis of the material.
It can also be created by calling dispersion.get_mat().

For Crystals with two or three different dispersions, there are the
:class:`UniaxialMaterial<elli.materials.UniaxialMaterial>` and
:class:`UniaxialMaterial<elli.materials.UniaxialMaterial>` respectively.

The respective materials can be rotated to achieve different crystal orientations.
A good visualization for these rotations can be found in Figure 6.10 of Fujiwara's
book 'Spectroscopic Ellipsometry' [1]_.

Additionally two materials can be combined via various :ref:'Effective medium approximations',
to create mixtures or account for interface roughness.

.. rubric:: References

.. [1] H. Fujiwara,
   Spectroscopic Ellipsometry,
   Principles and Applications,
   Chichester, UK, John Wiley & Sons, Ltd (2007).
   https://doi.org/10.1002/9780470060193
"""
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt

if TYPE_CHECKING:
    from .dispersions.dispersions import Dispersion


class Material(ABC):
    """Base class for materials (abstract class)."""

    @abstractmethod
    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the material for wavelength 'lbda'.

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
    """Base class for non-mixed materials (abstract class)."""

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
            r (npt.NDArray):
                rotation matrix (from :func:`rotation_euler<elli.utils.rotation_euler>` or others)
        """
        self.rotated = True
        self.rotation_matrix = r

    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the material for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        # Check for shape of lbda
        shape = np.shape(lbda)
        if shape == ():
            length = 1
        else:
            length = shape[0]

        # create empty tensor
        epsilon = np.zeros((length, 3, 3), dtype=np.complex128)

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

    # pylint: disable=arguments-differ
    def set_dispersion(self, dispersion: "Dispersion") -> None:
        """Sets dispersion relation of the isotropic material.

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
            dispersion_o (Dispersion):
                Dispersion relation for ordinary crystal axes (x and y direction).
            dispersion_e (Dispersion):
                Dispersion relation for extraordinary crystal axis (z direction).
        """
        self.set_dispersion(dispersion_o, dispersion_e)

    # pylint: disable=arguments-differ
    def set_dispersion(
        self, dispersion_o: "Dispersion", dispersion_e: "Dispersion"
    ) -> None:
        """Sets dispersion relations of the uniaxial material.

        Args:
            dispersion_o (Dispersion):
                Dispersion relation for ordinary crystal axes (x and y direction).
            dispersion_e (Dispersion):
                Dispersion relation for extraordinary crystal axis (z direction).
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

    # pylint: disable=arguments-differ
    def set_dispersion(
        self,
        dispersion_x: "Dispersion",
        dispersion_y: "Dispersion",
        dispersion_z: "Dispersion",
    ) -> None:
        """Sets dispersion relations of the biaxial material.

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
    def get_tensor_fraction(self, lbda: npt.ArrayLike, fraction: float) -> npt.NDArray:
        """Gets the permittivity tensor of the material for wavelength 'lbda',
        while overwriting the set fraction. Used in VaryingMixtureLayers.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).
            fraction (float): Fraction of the guest material used for evaluation. (Range 0 - 1).

        Returns:
            npt.NDArray: Permittivity tensor.
        """

    def get_tensor(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Gets the permittivity tensor of the material for wavelength 'lbda'.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        return self.get_tensor_fraction(lbda, self.fraction)


class VCAMaterial(MixtureMaterial):
    r"""Mixture Material approximated with a simple virtual crystal like average.

    .. math::
       \varepsilon_\text{eff} = (1 - f) \varepsilon_h + f \varepsilon_g

    where:

    * :math:`\varepsilon_\text{eff}` is the effective permittivity of host/mixture material,
    * :math:`\varepsilon_h` is the permittivity of the host mixture material,
    * :math:`\varepsilon_g` is the permittivity of the guest mixture material and
    * :math:`f` is the volume fraction of material a in the guest material.
    """

    def get_tensor_fraction(self, lbda: npt.ArrayLike, fraction: float) -> npt.NDArray:
        """Gets the permittivity tensor of the marterial for wavelength 'lbda',
        while overwriting the set fraction.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).
            fraction (float): Fraction of the guest material used for evaluation. (Range 0 - 1).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        epsilon = (
            self.host_material.get_tensor(lbda) * (1 - fraction)
            + self.guest_material.get_tensor(lbda) * fraction
        )
        return epsilon


class LooyengaEMA(MixtureMaterial):
    r"""Mixture Material approximated with Looyenga's formula.
    Valid for materials with small contrast.

    .. math::
       \varepsilon_\text{eff} = ((1 - f) \varepsilon_h^{1/3} + f \varepsilon_g^{1/3})^3

    where:

    * :math:`\varepsilon_\text{eff}` is the effective permittivity of host/mixture material,
    * :math:`\varepsilon_h` is the permittivity of the host mixture material,
    * :math:`\varepsilon_g` is the permittivity of the guest mixture material and
    * :math:`f` is the volume fraction of material a in the guest material.

    References:
        Looyenga, H. (1965). Physica, 31(3), 401–406.
    """

    def get_tensor_fraction(self, lbda: npt.ArrayLike, fraction: float) -> npt.NDArray:
        """Gets the permittivity tensor of the material for wavelength 'lbda',
        while overwriting the set fraction.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).
            fraction (float): Fraction of the guest material used for evaluation. (Range 0 - 1).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        epsilon = (
            self.host_material.get_tensor(lbda) ** (1 / 3) * (1 - fraction)
            + self.guest_material.get_tensor(lbda) ** (1 / 3) * fraction
        ) ** 3
        return epsilon


class MaxwellGarnettEMA(MixtureMaterial):
    r"""Mixture Material approximated with the Maxwell Garnett formula.
    It is valid for spherical inclusions with small volume fraction.

    .. math::
       \varepsilon_\text{eff} = \varepsilon_h \frac{2f(\varepsilon_g - \varepsilon_h)
       + \varepsilon_g + 2\varepsilon_h}
       {2\varepsilon_h + \varepsilon_g - f(\varepsilon_g - \varepsilon_h)}

    where:

    * :math:`\varepsilon_\text{eff}` is the effective permittivity of host/mixture material,
    * :math:`\varepsilon_h` is the permittivity of the host mixture material,
    * :math:`\varepsilon_g` is the permittivity of the guest mixture material and
    * :math:`f` is the volume fraction of material a in the guest material.
    """

    def get_tensor_fraction(self, lbda: npt.ArrayLike, fraction: float) -> npt.NDArray:
        """Gets the permittivity tensor of the material for wavelength 'lbda',
        while overwriting the set fraction.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).
            fraction (float): Fraction of the guest material used for evaluation. (Range 0 - 1).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        e_h = self.host_material.get_tensor(lbda)
        e_g = self.guest_material.get_tensor(lbda)

        # Catch calculation warnings
        old_settings = np.geterr()
        np.seterr(invalid="ignore")

        maxwell_garnett = (
            e_h
            * (2 * fraction * (e_g - e_h) + e_g + 2 * e_h)
            / (2 * e_h + e_g - fraction * (e_g - e_h))
        )

        # Reset numpy settings
        np.seterr(**old_settings)

        epsilon = np.where(np.logical_and(e_h == 0, e_g == 0), e_h, maxwell_garnett)
        return epsilon


class BruggemanEMA(MixtureMaterial):
    r"""Mixture Material approximated with the Bruggeman formula
    for spherical inclusions.

    Returns one of the two analytical solutions to this quadratic equation:

    .. math::
       2 \varepsilon_\text{eff}^2 +
       \varepsilon_\text{eff} [(3f - 2) \varepsilon_a
       + (1 - 3f)\varepsilon_b] - \varepsilon_a \cdot \varepsilon_b = 0

    where :math:`\varepsilon_\text{eff}` is the effective permittivity of host/mixture material,
    :math:`\varepsilon_a` is the permittivity of the first mixture material,
    :math:`\varepsilon_b` is the permittivity of the second mixture material
    and :math:`f` is the volume fraction of material a in the material b.

    References:
        * Josef Humlicek in Ellipsometry at the Nanoscale, Springer-Verlag Berlin Heidelberg, 2013
    """

    def get_tensor_fraction(self, lbda: npt.ArrayLike, fraction: float) -> npt.NDArray:
        """Gets the permittivity tensor of the material for wavelength 'lbda',
        while overwriting the set fraction.

        Args:
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).
            fraction (float): Fraction of the guest material used for evaluation. (Range 0 - 1).

        Returns:
            npt.NDArray: Permittivity tensor.
        """
        e_h = self.host_material.get_tensor(lbda)
        e_g = self.guest_material.get_tensor(lbda)
        f = fraction

        # fmt: off
        root1 = 3*e_g*f/4 - e_g/4 - 3*e_h*f/4 + e_h/2 - sqrt(
            9*e_g**2*f**2 - 6*e_g**2*f + e_g**2 - 18*e_g*e_h*f**2 +
            18*e_g*e_h*f + 4*e_g*e_h + 9*e_h**2*f**2 - 12*e_h**2*f + 4*e_h**2)/4
        root2 = 3*e_g*f/4 - e_g/4 - 3*e_h*f/4 + e_h/2 + sqrt(
            9*e_g**2*f**2 - 6*e_g**2*f + e_g**2 - 18*e_g*e_h*f**2 +
            18*e_g*e_h*f + 4*e_g*e_h + 9*e_h**2*f**2 - 12*e_h**2*f + 4*e_h**2)/4
        # fmt: on

        return self.jansson_algorithm(e_h, e_g, root1, root2)

    @staticmethod
    def jansson_algorithm(
        e_h: npt.ArrayLike,
        e_g: npt.ArrayLike,
        root1: npt.ArrayLike,
        root2: npt.ArrayLike,
    ):
        """Use the algorithm proposed by Jansson and Arwin to find the correct root of
        the solution to the Bruggeman formula.

        References:
            * Jansson R. , Arwin H. (1994) Optics Communications, 106, 4-6, 133-138,
              https://doi.org/10.1016/0030-4018(94)90309-3.

        Args:
            e_h (npt.ArrayLike): Dielectric tensor of host material.
            e_g (npt.ArrayLike): Dielectric tensor of host material.
            root1 (npt.ArrayLike): Solution 1 for dielectric tensor of mixture.
            root2 (npt.ArrayLike): Solution 2 for dielectric tensor of mixture.

        Returns:
            npt.NDArray: Physically correct permittivity tensor for the mixture.
        """

        # Catch calculation warnings
        old_settings = np.geterr()
        np.seterr(invalid="ignore", divide="ignore")

        z0 = (
            e_h
            * e_g
            * (np.conj(e_h) - np.conj(e_g))
            / (np.conj(e_h) * e_g - e_h * np.conj(e_g))
        )
        scaling_factor = np.conj(e_g - e_h) / np.abs(e_g - e_h)

        # Reset numpy settings
        np.seterr(**old_settings)

        # Find indices for the three cases
        mask_equal = np.nonzero(np.isnan(z0.real))
        mask_straight = np.nonzero(np.isinf(z0.real))
        mask_general = np.nonzero(
            np.logical_not(np.logical_or(np.isnan(z0.real), np.isinf(z0.real)))
        )

        def check_straight_line():
            def w(z):
                return np.where(
                    z0[mask_straight].real == np.inf,
                    z[mask_straight] * scaling_factor[mask_straight],
                    -1 * z[mask_straight] * scaling_factor[mask_straight],
                )

            return np.where(
                np.logical_and(
                    w(e_h).real < w(root1).real, w(root1).real < w(e_g).real
                ),
                root1[mask_straight],
                root2[mask_straight],
            )

        def check_general_case():
            def zeta(z):
                return (
                    (z[mask_general] - z0[mask_general])
                    / np.abs(z0[mask_general])
                    * scaling_factor[mask_general]
                )

            zeta_1, zeta_2, zeta_root1 = np.where(
                np.logical_and(zeta(e_h).imag > 0, zeta(e_g).imag > 0),
                (zeta(e_h), zeta(e_g), zeta(root1)),
                (-zeta(e_h), -zeta(e_g), -zeta(root1)),
            )

            return np.where(
                np.logical_and(
                    np.abs(zeta_root1 <= 1),
                    zeta_root1.imag >= np.imag((zeta_1 + zeta_2) / 2),
                ),
                root1[mask_general],
                root2[mask_general],
            )

        # Create new array and write correct values into it
        correct_root = np.full_like(e_h, np.nan)
        correct_root[mask_equal] = e_h[mask_equal]
        correct_root[mask_straight] = check_straight_line()
        correct_root[mask_general] = check_general_case()

        return correct_root
