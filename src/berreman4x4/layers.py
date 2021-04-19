# Encoding: utf-8
import numpy as np
import scipy.constants as sc

from .math import hs_propagator_lin, hs_propagator_Pade, buildDeltaMatrix
from .utils import UnitConversion


class Layer:
    """A very general layer (abstract class).

    Method that should be implemented in derived classes:
    * getPropagationMatrix(Kx, k0, inv) : returns propagator
      'Kx' : reduced wavenumber along x
      'k0' : wavenumber in vacuum
      'inv': boolean, if True, the propagator is from back to front.
    """

    def __init__(self):
        """Creates a new layer -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def getPermittivityProfile(self, lbda):
        """Returns permittivity tensor profile."""
        raise NotImplementedError("Should be implemented in derived classes")

    def getPropagationMatrix(self, Kx, k0, inv):
        """Returns propagation matrix P for this layer."""
        raise NotImplementedError("Should be implemented in derived classes")


class MaterialLayer(Layer):
    """A layer made of one material (abstract class).

    The material may be a Material or an InhomogeneousMaterial object.
    The first is a homogeneous material, the second is inhomogeneous.
    """

    material = None     # Material making the layer

    def setMaterial(self, material):
        """Defines the material for this layer. """
        self.material = material


class HomogeneousLayer(MaterialLayer):
    """Homogeneous layer of dielectric material."""

    h = None  # Thickness of the layer
    material = None         # Material object
    hs_propagator = None    # Function used for the propagator calculation

    def __init__(self, material, h, unit='nm', hs_method="Padé"):
        """New homogeneous layer of material 'material', with thickness 'h'

        'hs_method': see setMethod()
        """
        self.setMaterial(material)
        self.setMethod(hs_method)
        self.setThickness(h, unit)

    def setThickness(self, h, unit='nm'):
        """Defines the thickness of this homogeneous layer."""
        self.h = h * UnitConversion[unit]

    def setMethod(self, hs_method):
        """Defines how the homogeneous slab propagator is calculated.

        "linear" -> first order approximation of exp()
        "Padé"   -> Padé approximation of exp()
        """
        if hs_method == "linear":
            self.hs_propagator = hs_propagator_lin
        elif hs_method == "Padé":
            self.hs_propagator = hs_propagator_Pade
        else:
            raise NotImplementedError("Method " + hs_method +
                                      " not available for propagator calculation")

    def getPermittivityProfile(self, lbda, unit='m'):
        """Returns permittivity tensor profile.

        Returns a list containing one tuple: [(h, epsilon)]
        """
        return [(self.h, self.material.getTensor(lbda, unit))]

    def getPropagationMatrix(self, Kx, k0, inv=False):
        """Returns propagation matrix P

        Psi(z+h) = P * Psi(z)
        P = exp(i h k0 Delta h), where 'exp' is the matrix exponential.

        'Kx' : reduced wavenumber along x
        'k0' : vacuum wavenumber
        'inv' : returns the inverse matrix, BP = exp(-i h k0 Delta)
        """
        epsilon = self.material.getTensor(2*sc.pi/k0, 'm')
        Delta = buildDeltaMatrix(Kx, epsilon)
        if inv:
            h = -self.h
        else:
            h = self.h
        return self.hs_propagator(Delta, h, k0)

    def getDeltaMatrix(self, Kx, k0):
        """Returns Delta matrix of the homogeneous layer."""
        epsilon = self.material.getTensor(2*sc.pi/k0, 'm')
        Delta = buildDeltaMatrix(Kx, epsilon)
        return Delta


class HomogeneousIsotropicLayer(HomogeneousLayer):
    """Homogeneous Isotropic Layer.

    Must be made of an isotropic material.

    Provides function get_QWP_thickness(lbda) returning the thickness of a
    Quarter Wave Plate at wavelength 'lbda'.

    Can be created with parameter h = ("QWP", 1000), see method setThickness().
    """

    def setThickness(self, h, unit='nm'):
        """Defines the thickness of this homogeneous isotropic layer.

        If h is a tuple ('QWP', lbda), the thickness 'h' in (nm) is calculated for a
        quarter-wave plate at wavelength 'lbda'.
        """
        # Special case when a quarter-wave plate is requested
        if isinstance(h, tuple):
            (name, lbda) = h
            if name == "QWP":
                h = self.get_QWP_thickness(lbda, unit)
            else:
                raise ValueError("Thickness not correctly defined.")
        self.h = h * UnitConversion[unit]

    def get_QWP_thickness(self, lbda, unit='nm'):
        """Return the thickness of a Quater Wave Plate at wavelength 'lbda' (nm)."""
        nr = np.real(self.material.getRefractiveIndex(lbda, unit)[0, 0, 0])
        return lbda / (4.*nr)


#########################################################
# Inhomogeneous layers...

class InhomogeneousLayer(MaterialLayer):
    """Inhomogeneous layer.

    Must be fabricated with an InhomogemeousMaterial object.
    """

    material = None  # InhomogemeousMaterial object

    # Method used to decompose the inhomogeneous layer into homogeneous slabs:
    getSlicePropagator = None
    # Method used to calculate the propagator of a homogeneous slab:
    hs_propagator = None

    def __init__(self, material=None, evaluation="midpoint", hs_method="Padé"):
        """Creates an inhomogeneous layer.

        'material' : InhomogemeousMaterial object

        The propagation matrix is evaluated depending on parameters
        'evaluation', 'hs_method' see setMethod().
        """
        self.setMaterial(material)
        self.setMethod(evaluation, hs_method)

    def setMethod(self, evaluation, hs_method):
        """Defines the calculation method.

        The propagator for the inhomogeneous layer is decomposed and evaluated
        depending on parameter 'evaluation':
        "midpoint"   -> Evaluation of Δ(z) at midpoint.
        "symplectic" -> Z. Lu's symplectic method with three evaluation points.

        The propagator for a thin and homogeneous slice is calculated according
        to arguement 'hs_method':
        "linear" -> first order approximation of exp()
        "Padé"   -> Padé approximation of exp()

        The symplectic method requires P(h)·P(-h) = Id, which is true for
        the "Padé" approximation.

        The error on the propagator for an inhomogeneous thin slice due to the
        replacement by a homogeneous slice is O(h^3) in the midpoint method and
        O(h^5) in the symplectic method. A Padé approximant of order q gives an
        approximation of the propagator to order O(h^(2q)). Consequently, q = 3
        should be a good enough for the syplectic method.
        """
        if evaluation == "midpoint":
            self.getSlicePropagator = self.getSlicePropagator_mid
            if hs_method == "linear":
                self.hs_propagator = hs_propagator_lin
            elif hs_method == "Padé":
                self.hs_propagator = hs_propagator_Pade
            else:
                raise NotImplementedError("Method " + hs_method +
                                          " not available for midpoint evaluation")
        elif evaluation == "symplectic":
            self.getSlicePropagator = self.getSlicePropagator_sym
            if hs_method == "Padé":
                self.hs_propagator = hs_propagator_Pade
            else:
                raise NotImplementedError("Method " + hs_method +
                                          " not available for symplectic evaluation")

    def getPermittivityProfile(self, lbda, unit='m'):
        """Returns permittivity tensor profile.

        Tensor is evaluated in the middle of each slice.
        Returns list [(h1, epsilon1), (h2, epsilon2), ... ]
        """
        z = self.material.getSlices()
        h = np.diff(z)
        zmid = (z[:-1] + z[1:]) / 2.
        tensor = [self.material.getTensor(z, lbda, unit) for z in zmid]
        return list(zip(h, tensor))

    def getPropagationMatrix(self, Kx, k0, inv=False):
        """Returns propagation matrix P."""
        z = self.material.getSlices()
        if inv:
            z = z[::-1]
        P_tot = np.identity(4)
        for i in range(len(z)-1):
            P = self.getSlicePropagator(z[i+1], z[i], Kx, k0)
            P_tot = P @ P_tot
        return P_tot

    def getSlicePropagator_mid(self, z2, z1, Kx, k0):
        """Returns propagation matrix P(z2,z1) for a thin slice.

        Evaluates the Delta Matrix at midpoint between z1 and z2. The
        resulting global error is O(h^2).

        Note: The propagation matrix is calculated with one of the
        hs_propagator_*() functions, pointed by the attribute
        InhomogeneousLayer.midpoint_hs_propagator().
        """
        epsilon = self.material.getTensor((z1+z2)/2., 2*sc.pi/k0, 'm')
        Delta = buildDeltaMatrix(Kx, epsilon)
        P = self.hs_propagator(Delta, z2-z1, k0)
        return P

    # Coefficients from Z. Lu's article for the sympletic method
    s = 2.**(1./3)
    b1 = 1./(2-s)
    b2 = -s/(2-s)
    t1 = 1./(2*(2-s))
    t2 = 1./2
    t3 = 1./2 - (s-1)/(2*(2-s))

    def getSlicePropagator_sym(self, z2, z1, Kx, k0):
        """Returns propagation matrix P_sym(z2,z1) for a thin slice.

        Uses Z. Lu's symplectic method, leading to a global error in O(h^4).

        Note : We have P_sym(z2,z1) P_sym(z1,z2) = Id. This can be
        demonstrated by the relations z1 + t1 h = z2 - t3 h and
        z1 + t2 h = z2 - t2 h.
        """
        h = z2 - z1
        epsilon1 = self.material.getTensor(z1+self.t1*h, 2*sc.pi/k0, 'm')
        epsilon2 = self.material.getTensor(z1+self.t2*h, 2*sc.pi/k0, 'm')
        epsilon3 = self.material.getTensor(z1+self.t3*h, 2*sc.pi/k0, 'm')
        Delta1 = buildDeltaMatrix(Kx, epsilon1)
        Delta2 = buildDeltaMatrix(Kx, epsilon2)
        Delta3 = buildDeltaMatrix(Kx, epsilon3)
        P1 = self.hs_propagator(Delta1, self.b1*h, k0)
        P2 = self.hs_propagator(Delta2, self.b2*h, k0)
        P3 = self.hs_propagator(Delta3, self.b1*h, k0)
        return P1 @ P2 @ P3


#########################################################
# Repeated layers...

class RepeatedLayers(Layer):
    """Repetition of a structure."""

    n = None        # Number of repetitions
    before = None   # additionnal layers before the first period
    after = None    # additionnal layers after the last period
    layers = None   # layers to repeat

    def __init__(self, layers=None, n=2, before=0, after=0):
        """Repeated structure of layers

        'layers' : list of the repeated layers
        'n' : number of repetitions
        'before', 'after' : see method setRepetition()
        """
        self.setRepetition(n, before, after)
        self.setLayers(layers)

    def setRepetition(self, n,  before=0, after=0):
        """Defines the number of repetitions.

        'n' : number of repetitions
        'before' : number of additionnal layers before the first period
        'after' : number of additionnal layers after the last period

        Example : For layers [1,2,3] with n=2, before=1 and after=0, the
        structure will be 3123123.
        """
        self.n = n
        self.before = before
        self.after = after

    def setLayers(self, layers):
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPermittivityProfile(self, lbda, unit='m'):
        """Returns permittivity tensor profile.

        Returns list of tuples [(h1, epsilon1), (h2, epsilon2), ... ]
        """
        layers = sum([L.getPermittivityProfile(lbda, unit) for L in self.layers], [])
        if self.before > 0:
            before = layers[-self.before:]
        else:
            before = []
        return before + self.n * layers + layers[:self.after]

    def getPropagationMatrix(self, Kx, k0, inv=False):
        """Returns propagation matrix P for the repeated layers."""
        P_list = [L.getPropagationMatrix(Kx, k0, inv) for L in self.layers]
        P_period = P_before = np.identity(4)
        i_after = self.after
        i_before = len(P_list) - self.before
        if inv:
            for (i, P) in enumerate(P_list):
                if i == i_after:
                    P_after = P_period
                P_period = P_period @ P
                if i >= i_before:
                    P_before = P_before @ P
            return P_before @ np.linalg.matrix_power(P_period, self.n) @ P_after
        else:
            for (i, P) in enumerate(P_list):
                if i == i_after:
                    P_after = P_period
                P_period = P @ P_period
                if i >= i_before:
                    P_before = P @ P_before
            return P_after @ np.linalg.matrix_power(P_period, self.n) @ P_before
