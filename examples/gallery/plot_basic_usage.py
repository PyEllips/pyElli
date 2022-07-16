"""
Basic usage
===========

This example doesn't do much, it just makes a simple plot
"""
import elli
from elli.fitting import ParamsHist, fit
from elli.nexus import read_psi_delta

# %%
# Reading data
# ------------------------
#
# In the built documentation, it will be rendered as rST. All rST lines
# must begin with '# ' (note the space) including underlines below section
# headers.
ANGLE = 70
psi_delta = read_psi_delta("SiO2onSi.ellips.nxs").loc[ANGLE].loc[210:800]
psi_delta

# %%
# Setting parameters
# ------------------------
#
# In the built documentation, it will be rendered as rST. All rST lines
# must begin with '# ' (note the space) including underlines below section
# headers.

params = ParamsHist()
params.add("SiO2_n0", value=1.452, min=-100, max=100, vary=False)
params.add("SiO2_n1", value=36.0, min=-40000, max=40000, vary=False)
params.add("SiO2_n2", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_k0", value=0, min=-100, max=100, vary=False)
params.add("SiO2_k1", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_k2", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_d", value=20, min=0, max=40000, vary=True)


# %%
# Building the model
# ------------------------
#
# In the built documentation, it will be rendered as rST. All rST lines
# must begin with '# ' (note the space) including underlines below section
# headers.
@fit(psi_delta, params)
def model(lbda, params):
    # Load the literature values for Si
    sr = elli.SpectraRay("./")
    Si = elli.IsotropicMaterial(sr.loadDispersionTable("Si_Aspnes.mat"))

    # Generate the cauchy model from the current lmfit parameters
    SiO2 = elli.Cauchy(
        params["SiO2_n0"],
        params["SiO2_n1"],
        params["SiO2_n2"],
        params["SiO2_k0"],
        params["SiO2_k1"],
        params["SiO2_k2"],
    ).get_mat()
    # get_mat() generates an IsotropicMaterial from the dispersion relation

    # Construct the layers you expect in your sample
    # Here, it only consists of one layer SiO2 in between air and Si.
    # We build the structure coming from air, through the layers,
    # represented as an array, and having Si as bulk material.
    structure = elli.Structure(
        elli.AIR,  # Input medium
        [elli.Layer(SiO2, params["SiO2_d"])],  # Overlayer structure
        Si,
    )  # Output medium / Substrate

    # The model should return the evaluation of the structure at the experimental wavelengths lbda,
    # the experimental angle ANGLE and it should define a solver to calculate the transfer matrix.
    return structure.evaluate(lbda, ANGLE, solver=elli.Solver2x2)


# %%
# Fitting
# ------------------------
#
# In the built documentation, it will be rendered as rST. All rST lines
# must begin with '# ' (note the space) including underlines below section
# headers.
fit_stats = model.fit()
model.plot()
