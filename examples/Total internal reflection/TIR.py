#!/usr/bin/python
# encoding: utf-8
# %% [markdown]
# # Example of Total Internal Reflection on the Glass / Air interface
#
# Author: O. Castany, M.Müller

# %%
import elli
import matplotlib.pyplot as plt
import numpy as np


# %% [markdown]
# ## Structure definition

# %%
# Refractive indices
n_glass = 1.5
n_air = 1.0

# Materials:
glass = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n_glass))
air = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n_air))

# Structure:
s = elli.Structure(glass, [], air)

# Wavelength
lbda = 1000  # nm

# Variation of incidence angle
Phi_list = np.linspace(0, 89, 90)


# %% [markdown]
# ## Calculation

# %%
data = elli.ResultList([s.evaluate(lbda, Phi_i) for Phi_i in Phi_list])


# %% [markdown]
# ## Plotting

# %%
plt.figure()
plt.plot(Phi_list, data.R_pp, label="R_pp")
plt.plot(Phi_list, data.R_ss, label="R_ss")
plt.title("FTIR: Glass / Air")
plt.xlabel("Angle of incidence (°)")
plt.ylabel(r"Reflexion coefficients $R$")
plt.legend()
plt.show()


# %%
