# Encoding: utf-8
import numpy as np
import numpy.typing as npt
import pandas as pd
import scipy.constants as sc
from numpy.lib.scimath import sqrt
from scipy.linalg import expm as scipy_expm


def calc_pseudo_diel(rho, angle: float, output: str = "eps") -> pd.DataFrame:
    """Calculates the pseudo dielectric function of a measurement from rho.

    Args:
        rho (pandas.DataFrame):
            Measurement DataFrame containing rho as complex number as column and wavelength as index
        angle (float): Angle of measurement in degree
        output (str, optional): Output format for dielectric function.
            'n': refractive index,
            'eps': Dielectric function as two-column pandas.DataFrame,
            'epsi': Dielectric function as imaginary number.
            Defaults to 'eps'.

    Returns:
        pandas.DataFrame: Frame containing the pseudo dielectric function or refractive index.
    """
    theta = angle * np.pi / 180
    eps = np.sin(theta) ** 2 * (1 + np.tan(theta) ** 2 * ((1 - rho) / (1 + rho)) ** 2)

    if output == "n":
        n = sqrt(eps)
        return pd.DataFrame({"n": n.real, "k": n.imag}, index=eps.index)

    if output == "epsi":
        return eps

    return pd.concat(
        {"ϵ1": eps.apply(lambda x: x.real), "ϵ2": eps.apply(lambda x: x.imag)}, axis=1
    )


def calc_rho(psi_delta: pd.DataFrame) -> pd.DataFrame:
    """Calculate rho from a Psi-Delta DataFrame.
    The Psi-Delta DataFrame should be structured as follows:

        :index: Wavelength
        :column 'Ψ': Psi from measurement
        :column 'Δ': Delta from measurement

    This format is as returned from SpectraRay.read_psi_delta_file(...).

    Args:
        psi_delta (pandas.DataFrame): DataFrame containing Psi+Delta Measurement data

    Returns:
        pandas.DataFrame: Frame containing rho as an imaginary number.
    """
    return psi_delta.apply(
        lambda x: np.tan(np.deg2rad(x["Ψ"])) * np.exp(-1j * np.deg2rad(x["Δ"])), axis=1
    )


def get_qwp_thickness(material: "Material", lbda: float) -> float:
    """Return the thickness of a material in nm for a quarter wave plate at wavelength 'lbda'.

    Args:
        material (Material): Material object of the quarter wave plate
        lbda (float): Wavelength (in nm) at which the quarter wave plate is calculated

    Returns:
        float: Thickness (in nm) of quarter wave plate
    """
    nr = np.real(material.get_refractive_index(lbda)[0, 0, 0])
    return lbda / (4.0 * nr)


# base vectors
E_X = np.array([1, 0, 0]).reshape((3,))
E_Y = np.array([0, 1, 0]).reshape((3,))
E_Z = np.array([0, 0, 1]).reshape((3,))


def conversion_wavelength_energy(value: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts wavelength values to energy values and vice versa.

    .. math::
        value_{\text{target}} = c \cdot \hbar / \boldsymbol{value}

    Args:
        value (npt.ArrayLike): Single value or array of wavelengths in nm or energy in eV.

    Returns:
        npt.ArrayLike: Energy in eV or wavelength in nm.
    """
    return sc.speed_of_light * sc.value("Planck constant in eV/Hz") / (value * 1e-9)


def conversion_frequency2energy(f: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts frequency values to energy values.

    .. math::
        E = \boldsymbol{f} \cdot \hbar

    Args:
        f (npt.ArrayLike): Single value or array of frequencies in Hz.

    Returns:
        npt.ArrayLike: Energy in eV.
    """
    return f * sc.value("Planck constant in eV/Hz")


def conversion_energy2frequency(E: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts energy values to frequency values.

    .. math::
        f = \boldsymbol{E} / \hbar

    Args:
        E (npt.ArrayLike): Single value or array of energies in eV.

    Returns:
        npt.ArrayLike: Frequency in Hz.
    """
    return E / sc.value("Planck constant in eV/Hz")


def conversion_wavelength_frequency(value: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts wavelength values to frequency values and vice versa.

    .. math::
        value_{\text{target}} = c / \boldsymbol{value}

    Args:
        value (npt.ArrayLike): Single value or array of wavelengths in nm or frequencies in Hz.

    Returns:
        npt.ArrayLike: Frequencies in Hz or wavelengths in nm.
    """
    return sc.speed_of_light / (value * 1e-9)


def conversion_wavelength_wavenumber(value: npt.ArrayLike) -> npt.ArrayLike:
    r"""Converts wavelength values to wavenumber values and vice versa.

    .. math::
        value_{\text{target}} = 1 / \boldsymbol{value}

    Args:
        value (npt.ArrayLike): Single value or array of wavelengths in nm
            or wavenumbers in :math:`\text{cm}^{-1}`.

    Returns:
        npt.ArrayLike: Wavenumbers in :math:`\text{cm}^{-1}` or wavelengths in nm.
    """
    return 1e7 / value


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

    return scipy_expm(m_w)


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
