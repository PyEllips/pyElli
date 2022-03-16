"""Testing cases for the dispersion law factory class."""
import pytest
import elli


def test_correct_object_generation():
    """Factory class creates a correct object"""
    factory_disp_less = elli.DispersionFactory.get_dispersion(
        "ConstantRefractiveIndex", n=1.5
    )

    assert isinstance(factory_disp_less, elli.ConstantRefractiveIndex)
    assert factory_disp_less.single_params.get("n") == 1.5


def test_error_on_not_existing_class():
    """Raises an error if dispersion does not exist."""
    with pytest.raises(ValueError):
        elli.DispersionFactory.get_dispersion("DispersionNotExisting", n=1000)


def test_error_on_bad_class():
    """Raises an error if a bad class is requested."""
    for bad_class in ["DispersionFactory", "Dispersion", "DispersionSum"]:
        with pytest.raises(ValueError):
            elli.DispersionFactory.get_dispersion(bad_class)
