"""Calculate kramers-kronig-relation according to Maclaurin's formula"""
# pylint: disable=invalid-name
from typing import Callable
import numpy as np


def _integrate_im(im: np.ndarray, x: np.ndarray, x_i: float) -> np.ndarray:
    """Calculate the discrete imaginary sum (integral) for the kkr.

    Args:
        im (numpy.ndarray): The imaginary values from which to calculate.
        x (numpy.ndarray): The x-axis on which to calculate.
        x_i (float): The current point around which to integrate.

    Returns:
        numpy.ndarray: The integral sum
    """
    return np.sum(x * im / (x**2 - x_i**2))


def _integrate_im_reciprocal(im: np.ndarray, x: np.ndarray, x_i: float) -> np.ndarray:
    """Calculate the discrete imaginary sum (integral) for the kkr.
    This formulation uses an 1/x axis to transform a wavelength axis.

    Args:
        im (numpy.ndarray): The imaginary values from which to calculate.
        x (numpy.ndarray): The reciprocal x-axis on which to calculate.
        x_i (float): The current point around which to integrate.

    Returns:
        numpy.ndarray: The integral sum
    """
    return np.sum(im / (x - x**3 / x_i**2))


def _integrate_re(re: np.ndarray, x: np.ndarray, x_i: float) -> np.ndarray:
    """Calculate the discrete real sum (integral) for the kkr.

    Args:
        re (numpy.ndarray): The real values from which to calculate.
        x (numpy.ndarray): The x-axis on which to calculate.
        x_i (float): The current point around which to integrate.

    Returns:
        numpy.ndarray: The real sum
    """
    return np.sum(x_i * re / (x**2 - x_i**2))


def _integrate_re_reciprocal(re: np.ndarray, x: np.ndarray, x_i: float) -> np.ndarray:
    """Calculate the discrete real sum (integral) for the kkr.
    This formulation uses an 1/x axis to transform a wavelength axis.

    Args:
        re (numpy.ndarray): The real values from which to calculate.
        x (numpy.ndarray): The reciprocal x-axis on which to calculate.
        x_i (float): The current point around which to integrate.

    Returns:
        numpy.ndarray: The real sum
    """
    return np.sum(re / (x_i - x**2 / x_i))


def _calc_kkr(
    t: np.ndarray,
    x: np.ndarray,
    trafo: Callable[[np.ndarray, np.ndarray, float], np.ndarray],
) -> np.ndarray:
    """Calculates the kramers-kronig relation
    according to Maclaurin's formula.

    Args:
        t (np.ndarray): The y-axis on which to transform.
        x (np.ndarray): The x-axis on which to transform.
        trafo (Callable[[np.ndarray, np.ndarray, float], np.ndarray]):
            The transformation function.

    Raises:
        ValueError: y and x axis must have the same length.

    Returns:
        np.ndarray: The kkr transformed y-axis
    """
    if len(t) != len(x):
        raise ValueError(
            "y- and x-axes arrays must have the same length, "
            f"but have lengths {len(t)} and {len(x)}."
        )

    integral = np.zeros(len(t))
    interval = np.diff(x, prepend=x[1] - x[0])
    odd_y, odd_x = t[1::2], x[1::2]
    even_y, even_x = t[::2], x[::2]
    for i, x_i in enumerate(x):
        if i % 2 == 0:
            integral[i] = trafo(odd_y, odd_x, x_i)
        else:
            integral[i] = trafo(even_y, even_x, x_i)

    return 4 / np.pi * interval * integral


def re2im(re: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Calculates the kramers-kronig relation from the
    real to imaginary part
    according to Maclaurin's formula.

    Args:
        re (numpy.ndarray): The real values to transform.
        x (numpy.ndarray): The axis on which to transform.

    Returns:
        numpy.ndarray: The transformed imaginary part.
    """
    return _calc_kkr(re, x, _integrate_re)


def im2re(im: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Calculates the kramers-kronig relation from the
    imaginary to real part
    according to Maclaurin's formula.

    Args:
        im (numpy.ndarray): The imaginary values to transform.
        x (numpy.ndarray): The axis on which to transform.

    Returns:
        numpy.ndarray: The transformed real part.
    """
    return _calc_kkr(im, x, _integrate_im)


def re2im_reciprocal(re: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Calculates the kramers-kronig relation from the
    real to imaginary part
    according to Maclaurin's formula.
    This function assumes a reciprocal x-axis, e.g. wavelength in spectroscopy.

    Args:
        re (numpy.ndarray): The real values to transform.
        x (numpy.ndarray): The reciprocal axis on which to transform.

    Returns:
        numpy.ndarray: The transformed imaginary part.
    """
    return _calc_kkr(re, x, _integrate_re_reciprocal)


def im2re_reciprocal(im: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Calculates the kramers-kronig relation from the
    imaginary to real part
    according to Maclaurin's formula.
    This function assumes a reciprocal x-axis, e.g. wavelength in spectroscopy.

    Args:
        im (numpy.ndarray): The imaginary values to transform.
        x (numpy.ndarray): The reciprocal axis on which to transform.

    Returns:
        numpy.ndarray: The transformed real part.
    """
    return _calc_kkr(im, x, _integrate_im_reciprocal)
