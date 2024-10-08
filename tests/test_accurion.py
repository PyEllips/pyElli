"""Tests for reading accurion files"""

import numpy as np
import pytest
from fixtures import datadir  # pylint: disable=unused-import

import elli


# pylint: disable=redefined-outer-name
def test_reading_of_psi_delta_woollam(datadir):
    """Psi/delta Accurion file is read w/o errors"""
    data = elli.read_accurion_psi_delta(
        datadir / "Si3N4_on_4inBF33_W02_20240903-150451.ds.dat"
    )

    assert len(data.Wavelength) == 57
    np.testing.assert_array_equal(data.Angle_of_Incidence, [40, 50])
