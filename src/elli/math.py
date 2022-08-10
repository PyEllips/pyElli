# Encoding: utf-8
import numpy as np
import numpy.typing as npt
import scipy.linalg
import scipy.constants as sc

# base vectors
e_x = np.array([1, 0, 0]).reshape((3,))
e_y = np.array([0, 1, 0]).reshape((3,))
e_z = np.array([0, 0, 1]).reshape((3,))


def lambda2E(lbda: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts wavelength values to energy values.

    .. math::
        E = c \cdot \hbar / \boldsymbol{\lambda}

    Args:
        lbda (npt.ArrayLike): Single value or array of wavelengths in nm.

    Returns:
        npt.ArrayLike: Energy in eV.
    """
    return sc.speed_of_light * sc.value("Planck constant in eV/Hz") / (lbda * 1e-9)


def E2lambda(E: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts energy values to wavelength values.

    .. math::
        \lambda = c \cdot \hbar / \boldsymbol{E}

    Args:
        lbda (npt.ArrayLike): Single value or array of energies in eV.

    Returns:
        npt.ArrayLike: Wavelength in nm.
    """
    return (sc.speed_of_light * sc.value("Planck constant in eV/Hz") / E) * 1e-9


def freq2E(f: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts frequency values to energy values.

    .. math::
        E = \boldsymbol{f} \cdot \hbar

    Args:
        f (npt.ArrayLike): Single value or array of frequencies in Hz.

    Returns:
        npt.ArrayLike: Energy in eV.
    """
    return f * sc.value("Planck constant in eV/Hz")


def E2freq(E: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts energy values to frequency values.

    .. math::
        f = \boldsymbol{E} / \hbar

    Args:
        E (npt.ArrayLike): Single value or array of energies in eV.

    Returns:
        npt.ArrayLike: Frequency in Hz.
    """
    return E / sc.value("Planck constant in eV/Hz")


def freq2lambda(f: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts frequency values to wavelength values.

    .. math::
        \lambda = c / \boldsymbol{f}

    Args:
        f (npt.ArrayLike): Single value or array of frequencies in Hz.

    Returns:
        npt.ArrayLike: Wavelength in nm.
    """
    return (sc.speed_of_light / f) * 1e-9


def lambda2freq(lbda: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts wavelength values to frequency values.

    .. math::
        f = c / \boldsymbol{\lambda}

    Args:
        lbda (npt.ArrayLike): Single value or array of wavelengths in nm.

    Returns:
        npt.ArrayLike: Frequencies in Hz.
    """
    return sc.speed_of_light / (lbda * 1e-9)


def lambda2wnum(lbda: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts wavelength values to wavenumber values.

    .. math::
        \tilde{\nu} = 1 / \boldsymbol{\lambda}

    Args:
        lbda (npt.ArrayLike): Single value or array of wavelengths in nm.

    Returns:
        npt.ArrayLike: Wavenumbers in :math:`\text{cm}^{-1}`.
    """
    return 1 / (lbda * 1e-7)


def wnum2lambda(wnum: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts wavenumber values to wavelength values.

    .. math::
        \lambda = 1 / \boldsymbol{\tilde{\nu}}

    Args:
        wnum (npt.ArrayLike): Single value or array of wavenumbers in :math:`\text{cm}^{-1}`.

    Returns:
        npt.ArrayLike: Wavelengths in Hz.
    """
    return 1 / (wnum * 1e7)


#########################################################
# Rotations


def rotation_euler(p: float, n: float, r: float) -> npt.NDArray:
    """Returns rotation matrix defined by Euler angles p, n, r.

    Successive rotations : z,x',z'
    Note : The inverse rotation is -r, -n, -p

    Args:
        p (float): precession angle, 1st rotation, around z (0..360°).
        n (float): nutation angle, 2nd rotation, around x' (0..180°).
        r (float): 3rd rotation, around z' (0..360°).

    Returns:
        npt.NDArray: rotation matrix :math:`M_R`
    """
    p = np.deg2rad(p)
    n = np.deg2rad(n)
    r = np.deg2rad(r)

    c1 = np.cos(p)
    s1 = np.sin(p)
    c2 = np.cos(n)
    s2 = np.sin(n)
    c3 = np.cos(r)
    s3 = np.sin(r)

    return np.array(
        [
            [c1 * c3 - s1 * c2 * s3, -c1 * s3 - s1 * c2 * c3, s1 * s2],
            [s1 * c3 + c1 * c2 * s3, -s1 * s3 + c1 * c2 * c3, -c1 * s2],
            [s2 * s3, s2 * c3, c2],
        ]
    )


def rotation_v(v: npt.ArrayLike) -> npt.NDArray:
    r"""Returns rotation matrix defined by a rotation vector v.

    The calculation is made with the matrix exponential
    :math:`M_R = \exp(W)`, with :math:`W_{ij} = - ε_{ijk} V_{k}`,
    where :math:`ε_{ijk}` is the Levi-Civita antisymmetric tensor.
    If V is separated in a unit vector v and a magnitude θ, V = θ·v, with
    θ = ∥V∥, the calculation of the matrix exponential is avoided, and only
    sin(θ) and cos(θ) are needed instead.

    Note : The inverse rotation is -v

    Args:
        v (npt.ArrayLike): rotation vector (list or array)

    Returns:
        npt.NDArray: rotation matrix :math:`M_R`
    """
    # fmt: off
    m_w = np.array([[0,     -v[2], v[1]],
                  [v[2],  0,     -v[0]],
                  [-v[1], v[0],  0]])
    # fmt: on

    return scipy.linalg.expm(m_w)


def rotation_v_theta(v: npt.ArrayLike, theta: float) -> npt.NDArray:
    """Returns rotation matrix defined by a unit rotation vector and an angle.

    Notes : The inverse rotation is (v,-theta)

    Args:
        v (npt.ArrayLike): unit vector orienting the rotation (list or array)
        theta (float): rotation angle around v in degrees

    Returns:
        npt.NDArray: rotation matrix :math:`M_R`
    """
    # fmt: off
    m_w = np.array([[0,     -v[2], v[1]],
                  [v[2],  0,     -v[0]],
                  [-v[1], v[0],  0]])
    # fmt: on

    return (
        np.identity(3)
        + m_w * np.sin(np.deg2rad(theta))
        + np.linalg.matrix_power(m_w, 2) * (1 - np.cos(np.deg2rad(theta)))
    )
