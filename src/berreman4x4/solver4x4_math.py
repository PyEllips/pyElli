# Encoding: utf-8
import numpy as np
from numpy.lib.scimath import sqrt
from scipy.linalg import expm
import scipy.constants as sc

from .math import unitConversion

try:
    import tensorflow as tf
except ImportError:
    pass

try:
    import torch
except ImportError:
    pass


def TransitionMatrixHalfspace(Kx, epsilon):
    """Returns transition matrix L.

    'Kx' : reduced wavenumber in the x direction, Kx = kx/k0
    'k0' : wavenumber in vacuum, k0 = ω/c

    Sort eigenvectors of the Delta matrix according to propagation
    direction first, then according to $y$ component.

    Returns eigenvectors ordered like (s+,s-,p+,p-)
    """
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


def TransitionMatrixIsoHalfspace(Kx, epsilon, inv=False):
    """Returns transition matrix L.

    'Kx' : Reduced wavenumber
    'k0' : wavenumber in vacuum
    'inv' : if True, returns inverse transition matrix L^-1

    Returns : transition matrix L
    """
    nx = sqrt(epsilon[:, 0, 0])
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
                              [0, 0, 0, 0]], dtype=np.complex128), (i, 1, 1))
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
                              [0, 0, 0, 0]], dtype=np.complex128), (i, 1, 1))
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

#
# def getPowerTransmissionCorrection(self, Kx, k0):
#     """Returns correction coefficient for power transmission
#
#     The power transmission coefficient is the ratio of the 'z' components
#     of the Poynting vector:       T = P_t_z / P_i_z
#     For isotropic media, we have: T = kb'/kf' |t_bf|^2
#     The correction coefficient is kb'/kf'
#
#     Note : For the moment it is only meaningful for isotropic half spaces.
#     """
#     Kzf = self.frontHalfSpace.get_Kz_from_Kx(Kx, k0)
#     if isinstance(self.backHalfSpace, IsotropicHalfSpace):
#         Kzb = self.backHalfSpace.get_Kz_from_Kx(Kx, k0)
#         return Kzb.real / Kzf.real
#     else:
#         return None


def buildDeltaMatrix(Kx, eps):
    """Returns Delta matrix for given permittivity and reduced wave number.

    'Kx' : reduce wave number, Kx = kx/k0
    'eps' : permittivity tensor

    Returns : Delta 4x4 matrix, generator of infinitesimal translations
    """
    if np.shape(Kx) == ():
        i = 1
    else:
        i = np.shape(Kx)[0]

    Delta = np.array(
        [[-Kx * eps[:, 2, 0] / eps[:, 2, 2], -Kx * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), np.tile(1, i) - Kx ** 2 / eps[:, 2, 2]],
         [np.tile(0, i), np.tile(0, i), np.tile(-1, i), np.tile(0, i)],
         [eps[:, 1, 2] * eps[:, 2, 0] / eps[:, 2, 2] - eps[:, 1, 0],
          Kx ** 2 - eps[:, 1, 1] + eps[:, 1, 2] * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), Kx * eps[:, 1, 2] / eps[:, 2, 2]],
         [eps[:, 0, 0] - eps[:, 0, 2] * eps[:, 2, 0] / eps[:, 2, 2],
          eps[:, 0, 1] - eps[:, 0, 2] * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), -Kx * eps[:, 0, 2] / eps[:, 2, 2]]], dtype=np.complex128)
    Delta = np.moveaxis(Delta, 2, 0)
    return Delta


def hs_propagator_lin(Delta, h, k0):
    """Returns propagator with linear approximation.

    'Delta' : Delta matrix of the homogeneous material
    'h' : thickness of the homogeneous slab
    'k0' : wave vector in vacuum, k0 = ω/c

    Returns : propagator matrix

    The exact propagator is: P_hs = exp(i h k0 Δ)
    """
    P_hs_lin = np.identity(4) + 1j * h * np.einsum('nij,n->nij', Delta, k0)
    return P_hs_lin


def hs_propagator_pade_scipy(Delta, h, lbda):
    """Returns propagator with Padé approximation.

    'Delta' : Delta matrix of the homogeneous material
    'h' : thickness of the homogeneous slab
    'k0' : wave vector in vacuum, k0 = ω/c

    Returns : propagator matrix

    The diagonal Padé approximant of any order is symplectic, i.e.
    P_hs_Pade(h)·P_hs_Pade(-h) = 1.
    Such property may be suitable for use with Z. Lu's method.
    """
    k0 = 2 * sc.pi / unitConversion(lbda)

    mats = 1j * h * np.einsum('nij,n->nij', Delta, k0)

    P_hs_Pade = [expm(mat) for mat in mats]

    return P_hs_Pade


def hs_propagator_pade_tf(Delta, h, lbda):
    """Returns propagator with Padé approximation.

    'Delta' : Delta matrix of the homogeneous material
    'h' : thickness of the homogeneous slab
    'k0' : wave vector in vacuum, k0 = ω/c

    Returns : propagator matrix

    The diagonal Padé approximant of any order is symplectic, i.e.
    P_hs_Pade(h)·P_hs_Pade(-h) = 1.
    Such property may be suitable for use with Z. Lu's method.
    """
    k0 = 2 * sc.pi / unitConversion(lbda)

    mats = 1j * h * np.einsum('nij,n->nij', Delta, k0)

    t = tf.convert_to_tensor(np.asarray(mats, dtype=np.complex64))
    texp = tf.linalg.expm(t)
    P_hs_Pade = np.array(texp, dtype=np.complex128)

    return P_hs_Pade


def hs_propagator_pade_torch(Delta, h, lbda):
    """Returns propagator with Padé approximation.

    'Delta' : Delta matrix of the homogeneous material
    'h' : thickness of the homogeneous slab
    'k0' : wave vector in vacuum, k0 = ω/c

    Returns : propagator matrix

    The diagonal Padé approximant of any order is symplectic, i.e.
    P_hs_Pade(h)·P_hs_Pade(-h) = 1.
    Such property may be suitable for use with Z. Lu's method.
    """
    k0 = 2 * sc.pi / unitConversion(lbda)

    mats = 1j * h * np.einsum('nij,n->nij', Delta, k0)

    t = torch.from_numpy(mats)
    texp = torch.matrix_exp(t)
    P_hs_Pade = np.asarray(texp.numpy(), dtype=np.complex128)

    return P_hs_Pade