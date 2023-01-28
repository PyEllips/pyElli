"""Test adding of dispersions"""
import pytest
from numpy.testing import assert_array_almost_equal
from elli import Cauchy, Sellmeier
from elli.dispersions.base_dispersion import DispersionSum
from elli.dispersions.table_epsilon import TableEpsilon


def test_fail_on_adding_index_dispersion():
    """Test whether adding for an index based model fails"""
    cauchy_err_str = "Adding of index based dispersions is not supported yet"
    with pytest.raises(NotImplementedError) as sum_err:
        _ = Cauchy() + Cauchy()

    assert cauchy_err_str in str(sum_err.value)


def test_fail_on_adding_index_and_diel_dispersion():
    """Test whether the adding fails for an index based and dielectric dispersion"""

    for disp in [1, Sellmeier()]:
        with pytest.raises(TypeError) as sum_err:
            _ = disp + Cauchy()

        assert (
            "Cannot add refractive index and dielectric function based dispersions."
            in str(sum_err.value)
        )


def test_adding_of_diel_dispersions():
    """Test if dielectric dispersions are added correctly"""

    dispersion_sum = Sellmeier() + Sellmeier()

    assert isinstance(dispersion_sum, DispersionSum)
    assert len(dispersion_sum.dispersions) == 2

    for disp in dispersion_sum.dispersions:
        assert isinstance(disp, Sellmeier)

    assert_array_almost_equal(
        dispersion_sum.get_dielectric_df().values,
        2 * Sellmeier().get_dielectric_df().values,
    )


def test_flat_dispersion_sum_on_multiple_add():
    """Test whether the DispersionSum stays flat on multiple adds"""

    dispersion_sum = Sellmeier() + Sellmeier() + Sellmeier()

    assert isinstance(dispersion_sum, DispersionSum)
    assert len(dispersion_sum.dispersions) == 3

    for disp in dispersion_sum.dispersions:
        assert isinstance(disp, Sellmeier)

    assert_array_almost_equal(
        dispersion_sum.get_dielectric_df().values,
        3 * Sellmeier().get_dielectric_df().values,
    )


def test_adding_of_tabular_dispersions():
    """Tests correct adding of tabular dispersions"""

    with pytest.raises(NotImplementedError) as not_impl_err:
        _ = TableEpsilon() + 1

    assert (
        str(not_impl_err.value) == "Adding of tabular dispersions is not yet supported"
    )
