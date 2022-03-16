"""This files generates files for the current values of the dispersions"""
import numpy as np
import elli


def execute_and_save(dispersion, identifier, rep_params, *args, **kwargs):
    lbda = np.linspace(400, 1000, 500)
    fname = f"test_dispersions/{dispersion}_{identifier}.csv"

    disp = elli.DispersionFactory.get_dispersion(dispersion, *args, **kwargs)
    for rep_param in rep_params:
        disp.add(**rep_param)
    disp.get_dielectric_df(lbda).to_csv(fname)


def loop_dispersions_default():
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

    for dispersion in dispersions:
        execute_and_save(dispersion, "default", [])


def loop_dispersions_custom_values():
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

    for dispersion in dispersions:
        execute_and_save(
            dispersion.get("name"),
            "custom_values",
            dispersion.get("rep_params"),
            **dispersion.get("single_params"),
        )


if __name__ == "__main__":
    loop_dispersions_default()
    loop_dispersions_custom_values()
