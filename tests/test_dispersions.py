"""Tests for dispersion models"""
import elli
import numpy as np
import pandas as pd
from pandas.util.testing import assert_frame_equal
from numpy.testing import assert_array_equal


def test_constant_refr_index():
    """Tests constant refractive index"""
    disp = elli.ConstantRefractiveIndex(n=3)
    diel = disp.get_dielectric_df()
    eps0 = diel.loc[:, "ϵ1"].values
    eps1 = diel.loc[:, "ϵ2"].values

    assert_array_equal(np.ones(500) * 3 ** 2, eps0)
    assert_array_equal(np.zeros(500), eps1)


def test_epsilon_inf():
    """Tests epsilon infinity / constant dielectric function"""
    disp = elli.EpsilonInf(eps=3)
    diel = disp.get_dielectric_df()
    eps0 = diel.loc[:, "ϵ1"].values
    eps1 = diel.loc[:, "ϵ2"].values

    assert_array_equal(np.ones(500) * 3, eps0)
    assert_array_equal(np.zeros(500), eps1)


def test_regression_dispersions_default():
    """Test dispersions against their prior values"""
    dispersions = [
        "Cauchy",
        "DrudeEnergy",
        "DrudeResistivity",
        "Gauss",
        "LorentzEnergy",
        "LorentzLambda",
        "Poles",
        "Sellmeier",
        "Tanguy",
        "TaucLorentz",
    ]
    lbda = np.linspace(400, 1000, 500)

    for dispersion in dispersions:
        prototype = pd.read_csv(f"dispersion_prototypes/{dispersion}_default.csv")
        disp = elli.DispersionFactory.get_dispersion(dispersion)

        assert_frame_equal(prototype, disp.get_dielectric_df(lbda))


def test_table_refr_index():
    """Test refractive index dispersion table"""


def test_table_epsilon():
    """Test epsilon dispersion table"""
