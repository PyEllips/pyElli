"""Tests the importing from the refractiveindex.info database."""

import elli


def test_database_parsing():
    """Test if the refractive index.info parser works."""
    RII = elli.DatabaseRII()