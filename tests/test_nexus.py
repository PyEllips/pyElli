"""Tests for a TiO2/SiO2/Si reference layer"""

from __future__ import unicode_literals

import pytest
from fixtures import datadir  # pylint: disable=unused-import

import elli


@pytest.mark.parametrize(
    "filename",
    ["ellips.test.nxs", "ellips_nx_opt.test.nxs"],
)
# pylint: disable=redefined-outer-name
def test_reading_nxs(datadir, filename):
    """Psi/delta NeXus file is read w/o errors"""
    elli.read_nexus(datadir / filename)
