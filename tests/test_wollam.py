"""Tests for reading woollam"""
from __future__ import unicode_literals

import pytest

from fixtures import datadir  # pylint: disable=unused-import
import elli


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_woollam(datadir):
    """Psi/delta Spectraray file is read w/o errors"""
    elli.read_woollam_psi_delta(datadir / "wvase_example.dat")
    elli.read_woollam_psi_delta(datadir / "complete_ease_example.dat")


# pylint: disable=redefined-outer-name
def test_reading_and_conv_to_woollam(datadir):
    """Rho values are read from Psi / Delta file"""
    elli.read_woollam_rho(datadir / "wvase_example.dat")
    elli.read_woollam_rho(datadir / "complete_ease_example.dat")
