"""Tests for a TiO2/SiO2/Si reference layer"""

from __future__ import unicode_literals

import pytest

from fixtures import datadir  # pylint: disable=unused-import
import elli


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_spetraray(datadir):
    """Psi/delta Spectraray file is read w/o errors"""
    elli.read_spectraray_psi_delta(datadir / "Si_SiO2_theta_50_60_70.txt")


# pylint: disable=redefined-outer-name
def test_reading_and_conv_to_spectraray(datadir):
    """Rho values are read from Psi / Delta file"""
    elli.read_spectraray_rho(datadir / "Si_SiO2_theta_50_60_70.txt")
