"""Tests the importing from the refractiveindex.info database."""

import elli
import numpy as np
import pytest


class TestRefractiveIndexInfo:
    """Test if the refractive index.info parser works."""

    RII = elli.db.RII()

    def test_get_mat(self):
        mat = self.RII.get_mat("Au", "Johnson")
        assert isinstance(mat, elli.IsotropicMaterial)

    def test_dispersion_error(self):
        with pytest.raises(ValueError):
            self.RII.load_dispersion("foo", "bar")

    def test_tabular_nk(self):
        disp = self.RII.load_dispersion("Au", "Johnson")  # tabular nk

        np.testing.assert_almost_equal(
            disp.get_refractive_index(310.7), 1.53 + 1j * 1.893, decimal=3
        )
        np.testing.assert_almost_equal(
            disp.get_refractive_index(1088), 0.27 + 1j * 7.150, decimal=3
        )

    def test_tabular_n(self):
        disp = self.RII.load_dispersion("Xe", "Koch")  # Tabular n

        np.testing.assert_almost_equal(
            disp.get_refractive_index(234.555), 1.00084664, decimal=6
        )
        np.testing.assert_almost_equal(
            disp.get_refractive_index(612.327), 1.00070157, decimal=6
        )

    def test_formula_1(self):
        disp = self.RII.load_dispersion("SrTiO3", "Dodge")  # Formula 1

        np.testing.assert_almost_equal(
            disp.get_refractive_index(500), 2.4743, decimal=4
        )
        np.testing.assert_almost_equal(
            disp.get_refractive_index(1000), 2.3160, decimal=4
        )

    def test_formula_2_tabular_k(self):
        disp = self.RII.load_dispersion("SCHOTT-BK", "N-BK7")  # Formula 2 + k

        np.testing.assert_almost_equal(
            disp.get_refractive_index(500), 1.5214 + 1j * 9.5781e-9, decimal=4
        )
        np.testing.assert_almost_equal(
            disp.get_refractive_index(1000), 1.5075 + 1j * 9.9359e-9, decimal=4
        )

    def test_formula_3(self):
        disp = self.RII.load_dispersion("HOYA-NbF", "NBF1")  # Formula 3

        np.testing.assert_almost_equal(
            disp.get_refractive_index(500), 1.7520 + 1j * 3.9809e-9, decimal=4
        )
        np.testing.assert_almost_equal(
            disp.get_refractive_index(1000), 1.7271 + 1j * 7.9617e-9, decimal=4
        )

    def test_formula_4(self):
        disp = self.RII.load_dispersion("AgCl", "Tilton")  # formula 4

        np.testing.assert_almost_equal(
            disp.get_refractive_index(1024), 2.0213900020277, decimal=3
        )
        np.testing.assert_almost_equal(
            disp.get_refractive_index(10080), 1.9799748188746, decimal=4
        )

    def test_formula_5(self):
        disp = self.RII.load_dispersion("SF6", "Vukovic")  # Formula 5

        np.testing.assert_almost_equal(
            disp.get_refractive_index(600), 1.00072905, decimal=6
        )
        np.testing.assert_almost_equal(
            disp.get_refractive_index(1000), 1.00072017, decimal=6
        )
