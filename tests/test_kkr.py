"""Test kramers kronig relations"""
import numpy as np
from numpy.testing import assert_array_almost_equal
import elli
from elli.kkr import im2re, im2re_reciprocal


def test_tauc_lorentz():
    """Test whether the kkr reproduces the analytical expression of Tauc-Lorentz"""
    lbda = np.linspace(1e-2, 2000, 2000)
    g = elli.TaucLorentz(Eg=5).add(A=20, E=8, C=5)
    assert_array_almost_equal(
        im2re_reciprocal(g.get_dielectric(lbda).imag, lbda),
        g.get_dielectric(lbda).real,
        decimal=6,
    )


def test_tauc_lorentz_energy():
    """Test whether the kkr in non reciprocal formulation reproduces the analyitical expression
    of Tauc-Lorentz"""
    energy = np.linspace(0, 10, 5000)
    amp = 20
    osc_energy = 5
    gamma = 0.1
    lorentz = amp / (osc_energy**2 - energy**2 - 1j * gamma * energy)

    assert_array_almost_equal(
        im2re(lorentz.imag, energy)[10:], lorentz.real[10:], decimal=2
    )


def test_lorentz():
    """Test whether the kkr reproduces the analyitical expression of a Lorentz oscillator"""
    lbda = np.linspace(1e-2, 5000, 5000)
    g = elli.LorentzEnergy().add(A=20, E=5, gamma=5)
    assert_array_almost_equal(
        1 + im2re_reciprocal(g.get_dielectric(lbda).imag, lbda)[:-1000],
        g.get_dielectric(lbda).real[:-1000],
        decimal=2,
    )


def test_gauss():
    """KKR reproduces the analytical epxression of gaussian."""
    lbda = np.linspace(1e-2, 5000, 5000)
    g = elli.Gaussian().add(A=10, E=8, sigma=5)
    assert_array_almost_equal(
        im2re_reciprocal(g.get_dielectric(lbda).imag, lbda)[:-1000],
        g.get_dielectric(lbda).real[:-1000],
        decimal=2,
    )
