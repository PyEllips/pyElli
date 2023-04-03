"""Tests for the result class"""
import numpy as np
from pytest import fixture, raises
import elli


@fixture
def result():
    """Generate a pyElli result object"""
    Si = elli.db.RII().get_mat("Si", "Aspnes")
    SiO2 = elli.Cauchy(1.452, 36.0).get_mat()
    structure = elli.Structure(elli.AIR, [elli.Layer(SiO2, 500)], Si)

    return structure.evaluate(np.linspace(250, 800), 70, solver=elli.Solver2x2)


def test_delta_range_conversion(result):
    """Checks correct delta range conversion"""
    assert (
        all(result.delta > -180) and all(result.delta < 180) and any(result.delta < 0)
    )

    result.as_delta_range(0, 360)
    assert all(result.delta > 0) and all(result.delta < 360)

    result.as_delta_range(0, 180)
    assert all(result.delta > 0) and all(result.delta < 180)

    result.as_delta_range(-180, 180)
    assert (
        all(result.delta > -180) and all(result.delta < 180) and any(result.delta < 0)
    )


def test_delta_range_error_on_invalid_range(result):
    """Checks raising of errors on invalid range or type."""
    with raises(TypeError):
        result.as_delta_range("hallo", "welt")

    with raises(ValueError):
        result.as_delta_range(20, 180)
