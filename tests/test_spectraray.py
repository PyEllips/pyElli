"""Tests for a TiO2/SiO2/Si reference layer"""

from __future__ import unicode_literals

import numpy as np
import pytest
from fixtures import datadir  # pylint: disable=unused-import

import elli


# pylint: disable=redefined-outer-name
def test_reading_spectraray(datadir):
    """Psi/delta Spectraray file is read w/o errors"""
    data = elli.read_spectraray(datadir / "Si_SiO2_theta_50_60_70.txt")

    assert len(data.Wavelength) == 2209
    np.testing.assert_array_equal(data.Angle_of_Incidence, [50.2, 60.2, 70.2])
