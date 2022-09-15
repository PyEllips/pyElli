"""Tests for a TiO2/SiO2/Si reference layer"""
from __future__ import unicode_literals

import os
from distutils import dir_util

import elli
from pytest import fixture


@fixture
def datadir(tmpdir, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir


@fixture
# pylint: disable=redefined-outer-name
def nexus_psi_delta_file(datadir):
    """
    Fixture which returns the nexus file containting the psi / delta measurement data.
    """
    return datadir.join("ellips.test.nxs")


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_nxs(nexus_psi_delta_file):
    """Psi/delta NeXus file is read w/o errors"""
    elli.read_nexus_psi_delta(nexus_psi_delta_file)


# pylint: disable=redefined-outer-name
def test_reading_and_conv_to_rho(nexus_psi_delta_file):
    """Rho values are read from Psi / Delta file"""
    elli.read_nexus_rho(nexus_psi_delta_file)
