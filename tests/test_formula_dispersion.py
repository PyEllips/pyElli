"""Tests for the formula dispersion"""
import numpy as np
from numpy.testing import assert_array_almost_equal

from elli.dispersions import Sellmeier
from elli.dispersions.formula import FormulaDispersion


def test_sellmeier():
    """The formula dispersion reproduces the sellmeier formula"""
    lbda = np.linspace(400, 1500, 500)
    rep_params = {"A": [1, 1, 1], "B": [0.1, 0.1, 0.1]}

    sellmeier = Sellmeier()
    for A, B in zip(*rep_params.values()):
        sellmeier.add(A, B)

    formula = "eps = 1 + sum[A * (lbda * 1e-3)**2 / ((lbda * 1e-3)  ** 2 - B)]"
    formula_disp = FormulaDispersion(formula, "lbda", {}, rep_params)

    assert_array_almost_equal(
        sellmeier.get_dielectric(lbda), formula_disp.get_dielectric(lbda)
    )
