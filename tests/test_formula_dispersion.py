"""Tests for the formula dispersion"""

import numpy as np
from numpy.testing import assert_array_almost_equal
import pytest

from benchmark_formula_dispersion import structure as formula_structure
from benchmark_propagators_TiO2 import structure
import elli
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


def test_formula_against_predefined_model(structure, formula_structure):
    """A formula dispersion evaluates to the same values as a predefined model"""
    lbda = np.linspace(400, 800, 500)
    PHI = 70

    predefined4x4 = structure.evaluate(
        lbda, PHI, solver=elli.Solver4x4, propagator=elli.PropagatorExpm()
    )
    formula4x4 = formula_structure.evaluate(
        lbda, PHI, solver=elli.Solver4x4, propagator=elli.PropagatorExpm()
    )

    assert_array_almost_equal(predefined4x4.rho, formula4x4.rho)

    predefined2x2 = structure.evaluate(lbda, PHI, solver=elli.Solver2x2)
    formula2x2 = formula_structure.evaluate(lbda, PHI, solver=elli.Solver2x2)

    assert_array_almost_equal(predefined2x2.rho, formula2x2.rho)
