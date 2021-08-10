# Encoding: utf-8
import numpy as np
import scipy.linalg
import scipy.constants as sc

from .settings import settings

try:
    import tensorflow as tf
except ImportError:
    pass

try:
    import torch
except ImportError:
    pass


# base vectors
e_x = np.array([1, 0, 0]).reshape((3,))
e_y = np.array([0, 1, 0]).reshape((3,))
e_z = np.array([0, 0, 1]).reshape((3,))


# Unit factors
unitFactors = {
    'm': 1,
    'cm': 1e-2,
    'mm': 1e-3,
    'µm': 1e-6,
    'um': 1e-6,
    'nm': 1e-9,
    'A': 1e-10,
    'Å': 1e-10,
    'pm': 1e-12
}

CONV_M_EV = sc.speed_of_light * sc.value('Planck constant in eV/Hz')


def lambda2E(value):
    '''Returns the Energy in eV of the given wavelength in [unit] (default 'nm')'''
    return CONV_M_EV / unitConversion(value)


def unitConversion(tup):
    '''Returns the wavelength in m for a given value with [unit] (default 'nm')
    Takes a tupel (wavelength, unitString).
    If only a wavelength is given it asumes 'nm' as unit.
    '''
    if type(tup) == tuple:
        (value, unit) = tup
        return value * unitFactors[unit]
    else:
        return tup * unitFactors['nm']


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
          np.tile(0, i), np.tile(1, i) - Kx**2 / eps[:, 2, 2]],
         [np.tile(0, i), np.tile(0, i), np.tile(-1, i), np.tile(0, i)],
         [eps[:, 1, 2] * eps[:, 2, 0] / eps[:, 2, 2] - eps[:, 1, 0],
          Kx**2 - eps[:, 1, 1] + eps[:, 1, 2] * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), Kx * eps[:, 1, 2] / eps[:, 2, 2]],
         [eps[:, 0, 0] - eps[:, 0, 2] * eps[:, 2, 0] / eps[:, 2, 2],
          eps[:, 0, 1] - eps[:, 0, 2] * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), -Kx * eps[:, 0, 2] / eps[:, 2, 2]]], dtype=settings['dtype'])
    Delta = np.moveaxis(Delta, 2, 0)
    return Delta


def hs_propagator(Delta, h, k0, method="linear"):
    """Returns propagator for homogeneous slab of thickness h.

    'Delta' : Delta matrix of the homogeneous material
    'h' : thickness of the homogeneous slab
    'k0' : wave vector in vacuum, k0 = ω/c

    Returns : propagator matrix, exact or approximated, depending on the
    value of the 'method' parameter.

    The exact propagator is: P_hs = exp(i h k0 Δ)

    This function is a prototype and mainly useful for this docstring.
    Calculation is performed by function hs_propagator_xxxxx(), depending on
    the value of 'method':
        "linear" -> first order approximation of exp()
        "Padé"   -> Padé approximation of exp()
    """
    if method == "linear":
        return hs_propagator_lin(Delta, h, k0)
    elif method == "Padé":
        return hs_propagator_Pade(Delta, h, k0)


def hs_propagator_lin(Delta, h, k0):
    """Returns propagator with linear approximation."""
    P_hs_lin = np.identity(4) + 1j * h * np.einsum('nij,n->nij', Delta, k0)
    return P_hs_lin


def hs_propagator_Pade(Delta, h, lbda):
    """Returns propagator with Padé approximation.

    The diagonal Padé approximant of any order is symplectic, i.e.
    P_hs_Pade(h)·P_hs_Pade(-h) = 1.
    Such property may be suitable for use with Z. Lu's method.
    """
    k0 = 2*sc.pi / unitConversion(lbda)

    mats = 1j * h * np.einsum('nij,n->nij', Delta, k0)

    if settings['ExpmBackend'] == 'scipy':
        P_hs_Pade = [scipy.linalg.expm(mat) for mat in mats]

    elif settings['ExpmBackend'] == 'tensorflow':
        t = tf.convert_to_tensor(np.asarray(mats, dtype=np.complex64))
        texp = tf.linalg.expm(t)
        P_hs_Pade = np.array(texp, dtype=settings['dtype'])

    elif settings['ExpmBackend'] == 'pytorch':
        t = torch.from_numpy(mats)
        texp = torch.matrix_exp(t)
        P_hs_Pade = np.asarray(texp.numpy(), dtype=settings['dtype'])

    else:
        raise ValueError("Wrong expmBackend configuration.")

    return P_hs_Pade

#########################################################
# Rotations

def rotation_Euler(angles):
    """Returns rotation matrix defined by Euler angles (p,n,r)

    'angles' : tuple (p,n,r)

    Returns : rotation matrix M_R.
    If A is an initial vector,  B = M_R * A is the rotated vector

    Successive rotations : z,x',z'
        p = precession angle, 1st rotation, around z (0..2π)
        n = nutation angle, 2nd rotation, around x' (0..π)
        r = 3rd rotation, around z' (0..2π)

    Euler rotation for the coordinates is Rz(p)·Rx(n)·Rz(r),
    where Rj(θ) is the matrix rotation for the coordinates.
    (see for example Fujiwara, p. 217)

    Note : The inverse rotation is (-r,-n,-p)
    """
    (p, n, r) = np.deg2rad(angles)
    c1 = np.cos(p)
    s1 = np.sin(p)
    c2 = np.cos(n)
    s2 = np.sin(n)
    c3 = np.cos(r)
    s3 = np.sin(r)
    return np.array([[c1*c3-s1*c2*s3, -c1*s3-s1*c2*c3,  s1*s2],
                     [s1*c3+c1*c2*s3, -s1*s3+c1*c2*c3, -c1*s2],
                     [s2*s3,           s2*c3,           c2]])


def rotation_V(V):
    """Returns rotation matrix defined by a rotation vector V

    'V' : rotation vector (list or array)

    Returns : rotation matrix M_R
    If A is an initial vector,  B = M_R * A is the rotated vector

    The calculation is made with the matrix exponential
    M_R = exp(W), with W_{ij} = - ε_{ijk} V_{k},
    where ε_{ijk} is the Levi-Civita antisymmetric tensor.
    If V is separated in a unit vector v and a magnitude θ, V = θ·v, with
    θ = ∥V∥, the calculation of the matrix exponential is avoided, and only
    sin(θ) and cos(θ) are needed instead.

    Note : The inverse rotation is -V
    """
    W = np.array([[0,      -V[2],  V[1]],
                  [V[2],   0,      -V[0]],
                  [-V[1],  V[0],   0]])
    return scipy.linalg.expm(W)


def rotation_v_theta(v, theta):
    """Returns rotation matrix defined by a unit rotation vector and an angle

    'v' : unit vector orienting the rotation (list or array)
    'theta' : rotation angle around v in radians

    Returns : rotation matrix M_R.
    If A is an initial vector,  B = M_R * A is the rotated vector

    Notes : The inverse rotation is (v,-theta)
    """
    w = np.array([[0,      -v[2],  v[1]],
                  [v[2],   0,      -v[0]],
                  [-v[1],  v[0],   0]])
    return np.identity(3) + w * np.sin(np.deg2rad(theta)) \
        + np.linalg.matrix_power(w, 2) * (1 - np.cos(np.deg2rad(theta)))
