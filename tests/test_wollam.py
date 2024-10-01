"""Tests for reading woollam"""

import numpy as np
import pytest
import xarray as xr
from fixtures import datadir  # pylint: disable=unused-import

import elli


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_woollam(datadir):
    """Psi/delta Wollam file is read w/o errors"""
    data_wvase = elli.read_woollam_psi_delta(datadir / "wvase_example.dat")
    data_cease = elli.read_woollam_psi_delta(datadir / "complete_ease_example.dat")

    assert len(data_wvase) == 2
    assert len(data_cease) == 2

    assert len(data_wvase.Wavelength) == 181
    assert len(data_cease.Wavelength) == 1088

    np.testing.assert_array_equal(data_wvase.Angle_of_Incidence, [65, 70, 75])
    np.testing.assert_array_equal(data_cease.Angle_of_Incidence, [50, 60, 70])


# pylint: disable=redefined-outer-name
def test_reading_and_conv_to_woollam(datadir):
    """Rho values are calculated from Psi / Delta file"""
    data_wvase = elli.read_woollam_rho(datadir / "wvase_example.dat")
    data_cease = elli.read_woollam_rho(datadir / "complete_ease_example.dat")

    assert isinstance(data_wvase, xr.DataArray)
    assert isinstance(data_cease, xr.DataArray)

    assert len(data_wvase.Wavelength) == 181
    assert len(data_cease.Wavelength) == 1088

    np.testing.assert_array_equal(data_wvase.Angle_of_Incidence, [65, 70, 75])
    np.testing.assert_array_equal(data_cease.Angle_of_Incidence, [50, 60, 70])


# pylint: disable=redefined-outer-name
def test_raises_not_implemented_for_tan_cos_format(datadir):
    """Raises error when a wvase Tan(Psi)/Cos(Delta) file is presented"""

    with pytest.raises(NotImplementedError):
        elli.read_woollam_psi_delta(datadir / "wvase_trig.dat")
