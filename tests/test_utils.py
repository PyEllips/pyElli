"""Tests for the utils file"""

from pytest import raises

import elli


def test_delta_range_errors():
    """Checks raising of errors on invalid range or type."""
    with raises(TypeError):
        elli.DeltaRange("hallo", "welt")

    with raises(ValueError):
        elli.DeltaRange(20, 180)

    with raises(ValueError):
        elli.DeltaRange(0, 720)

    with raises(ValueError):
        elli.DeltaRange(360, 0)
