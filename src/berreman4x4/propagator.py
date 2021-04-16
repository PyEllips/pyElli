# Encoding: utf-8
import numpy as np
import scipy.linalg

TF_IMPORTED = True
try:
    import tensorflow as tf
except ImportError:
    TF_IMPORTED = False


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
    P_hs_lin = np.identity(4) + 1j * h * np.swapaxes(k0 * np.swapaxes(Delta, 0, 2), 0, 2)
    return P_hs_lin


def hs_propagator_Pade(Delta, h, k0):
    """Returns propagator with Padé approximation.

    The diagonal Padé approximant of any order is symplectic, i.e.
    P_hs_Pade(h)·P_hs_Pade(-h) = 1.
    Such property may be suitable for use with Z. Lu's method.
    """
    mats = 1j * h * np.swapaxes(k0 * np.swapaxes(Delta, 0, 2), 0, 2)

    if TF_IMPORTED:
        t = tf.convert_to_tensor(mats, dtype=tf.complex64)
        texp = tf.linalg.expm(t)
        P_hs_Pade = np.array(texp)
    else:
        P_hs_Pade = [scipy.linalg.expm(mat) for mat in mats]

    return P_hs_Pade
