"""Tests for the formula dispersion"""
import numpy as np
from numpy.testing import assert_array_almost_equal
import pytest

from elli.dispersions import Sellmeier, Formula
from elli.dispersions.cauchy import Cauchy
from elli.dispersions.formula import FormulaIndex


@pytest.mark.parametrize(
    "ref_model, formula_model, formula, single_params, rep_params",
    [
        (
            Sellmeier,
            Formula,
            "eps = 1 + sum[A * (lbda * 1e-3)**2 / ((lbda * 1e-3)  ** 2 - B)]",
            {},
            {"A": [1, 1, 1], "B": [0.1, 0.1, 0.1]},
        ),
        (
            Cauchy,
            FormulaIndex,
            (
                "n = n0 + 1e2 * n1 / lbda ** 2 + 1e7 * n2 / lbda ** 4 + "
                "1j * (k0 + 1e2 * k1 / lbda ** 2 + 1e7 * k2 / lbda ** 4)"
            ),
            {"n0": 1.5, "n1": 1, "n2": 1, "k0": 1, "k1": 1, "k2": 1},
            {},
        ),
    ],
)
def test_formula_reproduces_predefined(
    ref_model, formula_model, formula, single_params, rep_params
):
    """The formula dispersion reproduces other dispersion models"""
    lbda = np.linspace(400, 1500, 500)

    disp = ref_model(**single_params)
    for params in zip(*rep_params.values()):
        disp.add(*params)

    formula_disp = formula_model(formula, "lbda", single_params, rep_params)

    assert_array_almost_equal(
        disp.get_dielectric(lbda), formula_disp.get_dielectric(lbda)
    )
