# Encoding: utf-8
import numpy as np
import scipy.constants as sc
from numpy.lib.scimath import sqrt

from .math import buildDeltaMatrix

class HalfSpace:
    """Homogeneous half-space with arbitrary permittivity.

    A HalfSpace must provide this method:
    * getTransitionMatrix(k0, Kx) : return transition matrix
    """

    material = None  # Material object

    def __init__(self, material):
        """Create a homogeneous half-space of the given material."""
        self.setMaterial(material)

    def setMaterial(self, material):
        """Defines the material for this half-space."""
        self.material = material

    def getTransitionMatrix(self, Kx, k0):
        """Returns transition matrix L.

        'Kx' : reduced wavenumber in the x direction, Kx = kx/k0
        'k0' : wavenumber in vacuum, k0 = ω/c

        Sort eigenvectors of the Delta matrix according to propagation
        direction first, then according to $y$ component.

        Returns eigenvectors ordered like (s+,s-,p+,p-)
        """
        epsilon = self.material.getTensor(2*sc.pi/k0, unit='m')
        Delta = buildDeltaMatrix(Kx, epsilon)

        q, Psi = np.linalg.eig(Delta)

        # Sort according to z propagation direction, highest Re(q) first
        i = np.argsort(-np.real(q))

        q = np.take_along_axis(q, i, axis=-1)
        Psi = np.take_along_axis(Psi, i[:, np.newaxis, :], axis=-1)
        # Result should be (+,+,-,-)

        # For each direction, sort according to Ey component, highest Ey first
        i1 = np.argsort(-np.abs(Psi[:, 1, :2]))
        i2 = 2 + np.argsort(-np.abs(Psi[:, 1, 2:]))
        i = np.hstack((i1, i2))
        # Result should be (s+,p+,s-,p-)

        # Reorder
        i[:, [1, 2]] = i[:, [2, 1]]

        q = np.take_along_axis(q, i, axis=-1)
        Psi = np.take_along_axis(Psi, i[:, np.newaxis, :], axis=-1)
        # Result should be(s+,s-,p+,p-)

        # Adjust Ey in ℝ⁺ for 's', and Ex in ℝ⁺ for 'p'
        E = np.hstack((Psi[:, 1, :2], Psi[:, 0, 2:]))

        nE = np.abs(E)
        c = np.ones_like(E)
        i = (nE != 0.0)
        c[i] = E[i]/nE[i]

        Psi = Psi * c[:, np.newaxis, :]

        # Normalize so that Ey = c1 + c2, analog to Ey = Eis + Ers
        # For an isotropic half-space, this should return the same matrix
        # as IsotropicHalfSpace
        c = Psi[:, 1, 0] + Psi[:, 1, 1]
        np.where(np.abs(c) == 0, 1, c)

        Psi = 2 * Psi / c[:, np.newaxis, np.newaxis]

        return Psi


class IsotropicHalfSpace(HalfSpace):
    """Homogeneous Isotropic HalfSpace.

    * Provides transition matrix L and the inverse.

      Can be equally used for the front half-space (Φ = Φi) or for the back
      half-space (Φ = Φt).

    * Provides relations between incidence angle Φ and reduced wave vector Kx.

      As detailed in the documentation, 'Φ' is the angle of the plane wave
      traveling to the right (angle measured with respect to z axis and
      oriented by y). The angle of the wave traveling to the left is '-Φ'.
    """

    def get_Kx_from_Phi(self, Phi, k0):
        """Returns the value of Kx.

        'Phi' : incidence angle of the wave (radians)
        'k0'  : wavenumber in vacuum

        As detailed in the documentation, 'Phi' is the angle of the wave
        traveling to the right with respect to the horizontal.

        kx = n k0 sin(Φ) : Real and constant throughout the structure.
                           If n ∈ ℂ, then Φ ∈ ℂ
        Kx = kx/k0 = n sin(Φ) : Reduced wavenumber.
        """

        nx = self.material.getRefractiveIndex(2*sc.pi/k0, unit='m')[:, 0, 0]
        Kx = nx * np.sin(Phi * sc.pi / 180)
        return Kx

    def get_Kz_from_Kx(self, Kx, k0):
        """Returns the value of Kz in the half-space, function of Kx

        'Kx' : Reduced wavenumber,      Kx = kx/k0 = n sin(Φ)
        'k0' : wavenumber in vacuum,    kx = n k0 sin(Φ)

        Returns : reduced wave number Kz = kz/k0
        """
        # Not vectorized. Could be?
        # Test type(Kz2)
        nx = self.material.getRefractiveIndex(2*sc.pi/k0, unit='m')[:, 0, 0]
        Kz2 = nx**2 - Kx**2
        return sqrt(complex(Kz2))

    def get_Phi_from_Kx(self, Kx, k0):
        """Returns the value of angle Phi according to the value of Kx.

        'Kx' : Reduced wavenumber,      Kx = kx/k0 = n sin(Φ)
        'k0' : wavenumber in vacuum,    kx = n k0 sin(Φ)

        Returns : angle Phi in radians.
        """
        # May be vectorized when I have time?
        nx = self.material.getRefractiveIndex(2*sc.pi/k0, unit='m')[:, 0, 0]
        sin_Phi = Kx/nx
        Phi = 180 * np.arcsin(sin_Phi) / sc.pi
        return Phi

    def getTransitionMatrix(self, Kx, k0, inv=False):
        """Returns transition matrix L.

        'Kx' : Reduced wavenumber
        'k0' : wavenumber in vacuum
        'inv' : if True, returns inverse transition matrix L^-1

        Returns : transition matrix L
        """
        nx = self.material.getRefractiveIndex(2*sc.pi/k0, unit='m')[:, 0, 0]
        sin_Phi = Kx/nx
        cos_Phi = sqrt(1 - sin_Phi**2)

        if np.shape(Kx) == ():
            i = 1
        else:
            i = np.shape(Kx)[0]

        if inv:
            L = np.tile(np.array([[0, 1, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]], dtype=complex), (i, 1, 1))
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [1, 0, 0, 0],
                                   [1, 0, 0, 0]]), (i, 1, 1)) / cos_Phi[:, None, None]
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 1],
                                   [0, 0, 0, -1]]), (i, 1, 1)) / nx[:, None, None]
            L += np.tile(np.array([[0, 0, -1, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0]]), (i, 1, 1)) / cos_Phi[:, None, None] / nx[:, None, None]
            return 0.5 * L
            #   np.array(
            # [[0, 1, -1/(nx*cos_Phi),  0],
            #  [0, 1,  1/(nx*cos_Phi),  0],
            #  [1/cos_Phi, 0,  0,  1/nx],
            #  [1/cos_Phi, 0,  0, -1/nx]])
        else:
            L = np.tile(np.array([[0, 0, 0, 0],
                                  [1, 1, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]], dtype=complex), (i, 1, 1))
            L += np.tile(np.array([[0, 0, 1, 1],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0]]), (i, 1, 1)) * cos_Phi[:, None, None]
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 1, -1]]), (i, 1, 1)) * nx[:, None, None]
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [-1, 1, 0, 0],
                                   [0, 0, 0, 0]]), (i, 1, 1)) * cos_Phi[:, None, None] * nx[:, None, None]
            return L
            # np.array(
            # [[0, 0, cos_Phi, cos_Phi],
            #  [1, 1, 0, 0],
            #  [-nx*cos_Phi, nx*cos_Phi, 0, 0],
            #  [0, 0, nx, -nx]])
