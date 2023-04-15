"""Tests for the formula dispersion"""
import numpy as np
from numpy.testing import assert_array_almost_equal
import pytest

from elli.dispersions import Sellmeier, Formula
from elli.dispersions.cauchy import Cauchy
from elli.dispersions.formula import FormulaIndex


@pytest.mark.parametrize(
    "ref_model, formula_model, formula, single_params, rep_params, unit",
    [
        (
            Sellmeier,
            Formula,
            "eps = 1 + sum[A * (lbda * 1e-3)**2 / ((lbda * 1e-3)  ** 2 - B)]",
            {},
            {"A": [1, 1, 1], "B": [0.1, 0.1, 0.1]},
            "nm",
        ),
        (
            Sellmeier,
            Formula,
            "eps = 1 + sum[A * lbda**2 / (lbda** 2 - B)]",
            {},
            {"A": [1, 1, 1], "B": [0.1, 0.1, 0.1]},
            "micrometer",
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
            "nm",
        ),
    ],
)
def test_formula_reproduces_predefined(
    ref_model, formula_model, formula, single_params, rep_params, unit
):
    """The formula dispersion reproduces other dispersion models"""
    lbda = np.linspace(400, 1500, 500)

    disp = ref_model(**single_params)
    for params in zip(*rep_params.values()):
        disp.add(*params)

    formula_disp = formula_model(formula, "lbda", single_params, rep_params, unit)

    assert_array_almost_equal(
        disp.get_dielectric(lbda), formula_disp.get_dielectric(lbda)
    )


def test_formula_fails_on_wrong_repr():
    """The formula dispersion fails when it is tried to be
    initialized with the wrong represenation"""

    with pytest.raises(ValueError):
        Formula("n = 1", "", {}, {})

    with pytest.raises(ValueError):
        FormulaIndex("eps = 1", "", {}, {})
