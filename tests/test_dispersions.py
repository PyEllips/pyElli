"""Tests for dispersion models"""
import elli
import numpy as np
import pandas as pd
import os
from distutils import dir_util
from pytest import fixture
from pandas.testing import assert_frame_equal
from numpy.testing import assert_array_equal


@fixture
def datadir(tmpdir, request):
    """Fixture for providing the dispersion prototype folder"""
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir


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


def test_regression_dispersions_default(datadir):
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
        "Table",
        "TableEpsilon",
    ]
    lbda = np.linspace(400, 1000, 500)

    for dispersion in dispersions:
        prototype = pd.read_csv(datadir.join(f"{dispersion}_default.csv"), index_col=0)
        disp = elli.DispersionFactory.get_dispersion(dispersion)

        assert_frame_equal(prototype, disp.get_dielectric_df(lbda))
