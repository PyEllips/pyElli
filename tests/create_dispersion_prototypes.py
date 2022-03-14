"""This files generates files for the current values of the dispersions"""
import numpy as np
import elli


def execute_and_save(dispersion, identifier, rep_params, *args, **kwargs):
    lbda = np.linspace(400, 1000, 500)
    fname = f"dispersion_prototypes/{dispersion}_{identifier}.csv"

    disp = elli.DispersionFactory.get_dispersion(dispersion, *args, **kwargs)
    for rep_param in rep_params:
        disp.add(*rep_param)
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
    ]

    for dispersion in dispersions:
        execute_and_save(dispersion, "default", [])


if __name__ == "__main__":
    loop_dispersions_default()
