"""Test kramers kronig relations"""
import numpy as np
from numpy.testing import assert_array_almost_equal
import elli
from elli.kkr import im2re


def test_tauc_lorentz():
    """Test whether the kkr reproduces the analytical expression of Tauc-Lorentz"""
    lbda = np.linspace(1e-2, 2000, 2000)
    g = elli.TaucLorentz(Eg=5).add(A=20, E=8, C=5)
    assert_array_almost_equal(
        im2re(g.get_dielectric(lbda).imag, lbda),
        g.get_dielectric(lbda).real,
        decimal=6,
    )


def test_gauss():
    """KKR reproduces the analytical epxression of gaussian."""
    lbda = np.linspace(1e-2, 2000, 2000)
    g = elli.Gaussian().add(A=10, E=8, sigma=5)
    assert_array_almost_equal(
        im2re(g.get_dielectric(lbda).imag, lbda), g.get_dielectric(lbda).real, decimal=1
    )
