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
UnitConversion = {
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

CONV_NM_EV = sc.speed_of_light * sc.value('Planck constant in eV/Hz') * 1e9

def lambda2E(value, unit='nm'):
    '''Returns the Energy in eV of the given wavelength in [unit] (default 'nm')'''
    return CONV_NM_EV / (value * UnitConversion[unit] / UnitConversion['nm'])


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
          np.tile(0, i), -Kx * eps[:, 0, 2] / eps[:, 2, 2]]])
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


def hs_propagator_Pade(Delta, h, k0):
    """Returns propagator with Padé approximation.

    The diagonal Padé approximant of any order is symplectic, i.e.
    P_hs_Pade(h)·P_hs_Pade(-h) = 1.
    Such property may be suitable for use with Z. Lu's method.
    """
    mats = 1j * h * np.einsum('nij,n->nij', Delta, k0)

    if settings['ExpmBackend'] == 'scipy':
        P_hs_Pade = [scipy.linalg.expm(mat) for mat in mats]

    elif settings['ExpmBackend'] == 'tensorflow':
        t = tf.convert_to_tensor(np.asarray(mats, dtype=np.complex64))
        texp = tf.linalg.expm(t)
        P_hs_Pade = np.array(texp)

    elif settings['ExpmBackend'] == 'pytorch':
        t = torch.from_numpy(mats)
        texp = torch.matrix_exp(t)
        P_hs_Pade = texp.numpy()

    else:
        raise ValueError("Wrong expmBackend configuration.")

    return P_hs_Pade
