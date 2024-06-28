"""Test adding of dispersions"""

import numpy as np
import pytest
from elli import Cauchy, Sellmeier
from elli.dispersions.base_dispersion import DispersionSum, IndexDispersionSum
from elli.dispersions.table_epsilon import TableEpsilon
from numpy.testing import assert_array_almost_equal


def test_adding_index_dispersion():
    """Test correct adding of index based dispersions"""
    index_dispersion_sum = Cauchy() + Cauchy()

    assert_array_almost_equal(
        index_dispersion_sum.get_dielectric(),
        (Cauchy().get_refractive_index() * 2) ** 2,
    )


def test_fail_on_adding_index_and_diel_dispersion():
    """Test whether the adding fails for an index based and dielectric dispersion"""

    with pytest.raises(TypeError) as sum_err:
        _ = Sellmeier() + Cauchy()

    assert (
        "Cannot add refractive index and dielectric function based dispersions."
        in str(sum_err.value)
    )


@pytest.mark.parametrize(
    "dispersions",
    [
        (DispersionSum(Sellmeier(), Sellmeier()), Cauchy()),
        (IndexDispersionSum(Cauchy(), Cauchy()), Sellmeier()),
        (
            DispersionSum(Sellmeier(), Sellmeier()),
            IndexDispersionSum(Cauchy(), Cauchy()),
        ),
        (Sellmeier(), Cauchy()),
    ],
)
def test_fail_on_adding_index_and_diel_dispersion_sum(dispersions):
    """Adding of index based and diel based dispersion sums fails"""

    with pytest.raises(TypeError):
        _ = dispersions[0] + dispersions[1]

    with pytest.raises(TypeError):
        _ = dispersions[1] + dispersions[0]


def test_fail_on_adding_index_and_diel_dispersion_as_args():
    """
    The adding of dispersion fails for an index based and dielectric dispersion
    when provided as args to DispersionSum
    """
    with pytest.raises(TypeError) as sum_err:
        DispersionSum(Sellmeier(), Cauchy())

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


def test_flat_dispersion_on_adding_with_dispersion_sum():
    """
    DispersionSum is kept flat even when a mixture of
    Dispersions and DispersionSums are added
    """
    dispersion_sum = (
        Sellmeier()
        + DispersionSum(DispersionSum(Sellmeier(), Sellmeier()), Sellmeier())
        + Sellmeier()
    )

    assert isinstance(dispersion_sum, DispersionSum)
    assert len(dispersion_sum.dispersions) == 5

    for disp in dispersion_sum.dispersions:
        assert isinstance(disp, Sellmeier)

    assert_array_almost_equal(
        dispersion_sum.get_dielectric_df().values,
        5 * Sellmeier().get_dielectric_df().values,
    )


def test_multiple_dispersion_sum_args():
    """Multiple Dispersions can be provided via the DispersionSum args"""
    dispersion_sum = DispersionSum(Sellmeier(), Sellmeier(), Sellmeier())

    assert isinstance(dispersion_sum, DispersionSum)
    assert len(dispersion_sum.dispersions) == 3

    for disp in dispersion_sum.dispersions:
        assert isinstance(disp, Sellmeier)

    assert_array_almost_equal(
        dispersion_sum.get_dielectric_df().values,
        3 * Sellmeier().get_dielectric_df().values,
    )


def test_nested_dispersion_sum_args():
    """
    DispersionSum is kept flat even for nested
    DispersionSum args
    """
    dispersion_sum = DispersionSum(
        DispersionSum(DispersionSum(Sellmeier(), Sellmeier()), Sellmeier()), Sellmeier()
    )

    assert isinstance(dispersion_sum, DispersionSum)
    assert len(dispersion_sum.dispersions) == 4

    for disp in dispersion_sum.dispersions:
        assert isinstance(disp, Sellmeier)

    assert_array_almost_equal(
        dispersion_sum.get_dielectric_df().values,
        4 * Sellmeier().get_dielectric_df().values,
    )


def test_flattening_of_dispersion_sum_args():
    """When a DispersionSum is passed via a DisperionSum arg it is flattened."""
    dispersion_sum = DispersionSum(Sellmeier(), DispersionSum(Sellmeier(), Sellmeier()))

    assert isinstance(dispersion_sum, DispersionSum)
    assert len(dispersion_sum.dispersions) == 3

    for disp in dispersion_sum.dispersions:
        assert isinstance(disp, Sellmeier)

    assert_array_almost_equal(
        dispersion_sum.get_dielectric_df().values,
        3 * Sellmeier().get_dielectric_df().values,
    )


def test_adding_of_float_to_tabular_epsilon_dispersion():
    """Tests correct adding of a float value to tabular dispersions"""

    table_eps = TableEpsilon(lbda=np.linspace(200, 1000, 801), epsilon=np.ones(801)) + 1

    assert_array_almost_equal(
        table_eps.get_dielectric(),
        np.ones(801) * 2,
    )


def test_adding_of_dispersion_function_and_table():
    """Dispersion function and table can be added"""

    table = TableEpsilon(lbda=np.linspace(200, 1000, 801), epsilon=np.ones(801))
    sellmeier = Sellmeier().add(1, 0.0001)

    assert_array_almost_equal(
        (table + sellmeier).get_dielectric(),
        table.get_dielectric() + sellmeier.get_dielectric(),
    )


def test_fail_on_adding_tabular_dispersions():
    """Adding two tabular dispersions should return an NotImplementedError"""

    with pytest.raises(NotImplementedError) as not_impl_err:
        _ = TableEpsilon(
            lbda=np.linspace(200, 1000, 801), epsilon=np.ones(801)
        ) + TableEpsilon(lbda=np.linspace(200, 1000, 801), epsilon=np.ones(801))

    assert (
        str(not_impl_err.value) == "Adding of tabular dispersions is not yet supported"
    )
