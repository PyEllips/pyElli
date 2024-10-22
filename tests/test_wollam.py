"""Tests for reading woollam"""

import numpy as np
import pytest
import xarray as xr
from fixtures import datadir  # pylint: disable=unused-import

import elli


# pylint: disable=redefined-outer-name
def test_reading_woollam(datadir):
    """Psi/delta Wollam file is read w/o errors"""
    data_wvase = elli.read_woollam(datadir / "wvase_example.dat")
    data_cease = elli.read_woollam(datadir / "complete_ease_example.dat")

    assert len(data_wvase) == 3
    assert len(data_cease) == 3

    assert len(data_wvase.Wavelength) == 181
    assert len(data_cease.Wavelength) == 1088

    np.testing.assert_array_equal(data_wvase.Angle_of_Incidence, [65, 70, 75])
    np.testing.assert_array_equal(data_cease.Angle_of_Incidence, [50, 60, 70])


# pylint: disable=redefined-outer-name
def test_raises_not_implemented_for_tan_cos_format(datadir):
    """Raises error when a wvase Tan(Psi)/Cos(Delta) file is presented"""

    with pytest.raises(NotImplementedError):
        elli.read_woollam(datadir / "wvase_trig.dat")
