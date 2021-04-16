# Encoding: utf-8
import numpy as np
import scipy.linalg

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