"""Tests for reading woollam"""
from fixtures import datadir  # pylint: disable=unused-import
import elli


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_woollam(datadir):
    """Psi/delta Spectraray file is read w/o errors"""
    data_wvase = elli.read_woollam_psi_delta(datadir / "wvase_example.dat")
    data_cease = elli.read_woollam_psi_delta(datadir / "complete_ease_example.dat")

    assert data_wvase.shape == (542, 2)
    assert data_cease.shape == (3263, 2)


# pylint: disable=redefined-outer-name
def test_reading_and_conv_to_woollam(datadir):
    """Rho values are read from Psi / Delta file"""
    data_wvase = elli.read_woollam_rho(datadir / "wvase_example.dat")
    data_cease = elli.read_woollam_rho(datadir / "complete_ease_example.dat")

    assert data_wvase.shape == (542,)
    assert data_cease.shape == (3263,)
