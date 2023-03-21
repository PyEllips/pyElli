"""Tests for a TiO2/SiO2/Si reference layer"""
from __future__ import unicode_literals

from pytest import fixture

from fixtures import datadir  # pylint: disable=unused-import
import elli


@fixture
# pylint: disable=redefined-outer-name
def nexus_psi_delta_file(datadir):
    """
    Fixture which returns the nexus file containting the psi / delta measurement data.
    """
    return datadir / "ellips.test.nxs"


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_nxs(nexus_psi_delta_file):
    """Psi/delta NeXus file is read w/o errors"""
    elli.read_nexus_psi_delta(nexus_psi_delta_file)


# pylint: disable=redefined-outer-name
def test_reading_and_conv_to_rho(nexus_psi_delta_file):
    """Rho values are read from Psi / Delta file"""
    elli.read_nexus_rho(nexus_psi_delta_file)
