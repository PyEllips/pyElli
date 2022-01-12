"""Testing cases for the dispersion law factory class."""
import pytest
import elli

def test_correct_object_generation():
    """Factory class creates a correct object"""
    factory_disp_less = elli.DispersionFactory.get_dispersion('DispersionLess', n=1.5)

    assert isinstance(factory_disp_less, elli.DispersionLess)
    assert factory_disp_less.n == 1.5

def test_correct_object_generation_with_short_identifier():
    """Factory class creates a correct object when called with a short identifier"""
    for test_name in ['less', 'LESS', 'LeSs', 'dispersion_less',
                      'DispersionLess', 'dispersION_LESS', 'DISPERSIONLESS',
                       'DISPERSION_LESS', 'DISPerSIONLESS', '   dispersion_less   ']:
        print(test_name)
        factory_disp_less = elli.DispersionFactory.get_dispersion_short(test_name, n=1.5)
        assert isinstance(factory_disp_less, elli.DispersionLess)
        assert factory_disp_less.n == 1.5

def test_error_on_not_existing_class():
    """Raises an error if dispersion does not exist."""
    with pytest.raises(ValueError):
        elli.DispersionFactory.get_dispersion('DispersionNotExisting', n=1000)

def test_error_on_bad_class():
    """Raises an error if a bad class is requested."""
    for bad_class in ['DispersionFactory', 'DispersionLaw', 'DispersionSum']:
        with pytest.raises(ValueError):
            elli.DispersionFactory.get_dispersion(bad_class)
