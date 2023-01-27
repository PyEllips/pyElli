"""Test kramers kronig relations"""
import pytest
from elli import Cauchy


def test_fail_on_adding_cauchy():
    """Test whether the kkr reproduces the analytical expression of Tauc-Lorentz"""
    cauchy_err_str = (
        "The cauchy dispersion cannot be added to other dispersions. "
        "Try the Poles or Lorentz model instead."
    )
    with pytest.raises(ValueError) as sum_err:
        _ = Cauchy() + Cauchy()

    assert cauchy_err_str in str(sum_err.value)

    with pytest.raises(ValueError):
        _ = 1 + Cauchy()
