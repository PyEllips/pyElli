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

    assert_array_equal(np.ones(801) * 3 ** 2, eps0)
    assert_array_equal(np.zeros(801), eps1)


def test_epsilon_inf():
    """Tests epsilon infinity / constant dielectric function"""
    disp = elli.EpsilonInf(eps=3)
    diel = disp.get_dielectric_df()
    eps0 = diel.loc[:, "ϵ1"].values
    eps1 = diel.loc[:, "ϵ2"].values

    assert_array_equal(np.ones(801) * 3, eps0)
    assert_array_equal(np.zeros(801), eps1)


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


def test_regression_dispersions_custom_values(datadir):
    """Test dispersions against their prior values"""
    dispersions = [
        {
            "name": "Cauchy",
            "single_params": {
                "n0": 1.5,
                "n1": 0.3,
                "n2": 0.05,
                "k0": 0.6,
                "k1": 0.2,
                "k2": 0.1,
            },
            "rep_params": [],
        },
        {
            "name": "DrudeEnergy",
            "single_params": {"A": 100, "gamma": 0.5},
            "rep_params": [],
        },
        {
            "name": "DrudeResistivity",
            "single_params": {"rho_opt": 100, "tau": 1e-2},
            "rep_params": [],
        },
        {
            "name": "LorentzLambda",
            "single_params": {},
            "rep_params": [
                {"A": 100, "lambda": 500, "gamma": 10},
                {"A": 150, "lambda": 300, "gamma": 20},
                {"A": 300, "lambda": 750, "gamma": 50},
            ],
        },
        {
            "name": "LorentzEnergy",
            "single_params": {},
            "rep_params": [
                {"A": 100, "E": 3, "gamma": 0.1},
                {"A": 150, "E": 1.5, "gamma": 0.05},
                {"A": 300, "E": 0.3, "gamma": 0.02},
            ],
        },
        {
            "name": "Gauss",
            "single_params": {},
            "rep_params": [
                {"A": 100, "E": 3, "sigma": 0.1},
                {"A": 150, "E": 1.5, "sigma": 0.05},
                {"A": 300, "E": 0.3, "sigma": 0.02},
            ],
        },
        {
            "name": "TaucLorentz",
            "single_params": {"Eg": 2},
            "rep_params": [
                {"A": 100, "E": 2.5, "C": 0.1},
                {"A": 150, "E": 3, "C": 0.05},
                {"A": 300, "E": 4.5, "C": 0.02},
            ],
        },
        {
            "name": "Tanguy",
            "single_params": {
                "A": 1,
                "d": 2,
                "gamma": 0.1,
                "R": 0.1,
                "Eg": 2,
                "a": 1,
                "b": 0,
            },
            "rep_params": [],
        },
        {
            "name": "Poles",
            "single_params": {"A_ir": 100, "A_uv": 100, "E_uv": 4},
            "rep_params": [],
        },
        {
            "name": "Table",
            "single_params": {
                "lbda": np.linspace(400, 1000, 100),
                "n": np.linspace(1, 1.5, 100) + 1j * np.linspace(0, 1, 100),
            },
            "rep_params": [],
        },
        {
            "name": "TableEpsilon",
            "single_params": {
                "lbda": np.linspace(400, 1000, 100),
                "epsilon": np.linspace(1, 1.5, 100) + 1j * np.linspace(0, 1, 100),
            },
            "rep_params": [],
        },
    ]
    lbda = np.linspace(400, 1000, 500)

    for dispersion in dispersions:
        disp_name = dispersion.get("name")
        prototype = pd.read_csv(
            datadir.join(f"{disp_name}_custom_values.csv"), index_col=0
        )
        disp = elli.DispersionFactory.get_dispersion(
            disp_name, **dispersion.get("single_params")
        )
        for rep_param in dispersion.get("rep_params"):
            disp.add(**rep_param)

        assert_frame_equal(prototype, disp.get_dielectric_df(lbda))
