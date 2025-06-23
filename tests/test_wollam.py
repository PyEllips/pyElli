"""Tests for reading woollam"""

import pytest
from fixtures import datadir  # pylint: disable=unused-import

import elli


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_woollam(datadir):
    """Psi/delta Spectraray file is read w/o errors"""
    data_wvase = elli.read_woollam_psi_delta(datadir / "wvase_example.dat")
    data_wvase_wo_dpolE = elli.read_woollam_psi_delta(
        datadir / "wvase_example_wo_dpolE.dat"
    )
    data_cease = elli.read_woollam_psi_delta(datadir / "complete_ease_example.dat")

    assert data_wvase.shape == (542, 2)
    assert data_wvase_wo_dpolE.shape == (542, 2)
    assert data_cease.shape == (3263, 2)


# pylint: disable=redefined-outer-name
def test_reading_and_conv_to_woollam(datadir):
    """Rho values are read from Psi / Delta file"""
    data_wvase = elli.read_woollam_rho(datadir / "wvase_example.dat")
    data_cease = elli.read_woollam_rho(datadir / "complete_ease_example.dat")

    assert data_wvase.shape == (542,)
    assert data_cease.shape == (3263,)


# pylint: disable=redefined-outer-name
def test_raises_not_implemented_for_tan_cos_format(datadir):
    """Raises error when a wvase Tan(Psi)/Cos(Delta) file is presented"""

    with pytest.raises(NotImplementedError):
        elli.read_woollam_psi_delta(datadir / "wvase_trig.dat")
