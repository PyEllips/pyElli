#!/usr/bin/python3
# encoding: utf-8
# %% [markdown]
# # We reproduce results from section 6.4.1 in 'Spectroscopic Ellipsometry', by H. Fujiwara.
#
# Author: O. Castany, M. Müller
#
# Verification of the code against results presented in Fujiwara's book 'Spectroscopic Ellipsometry', section 6.4.1
# (p. 237). We reproduce figures 6.16 and 6.17.

# %%
import numpy as np
import elli
import matplotlib.pyplot as plt

# %% [markdown]
# ## Setting up the materials

# %%
# Front half-space (air)
air = elli.IsotropicMaterial(elli.DispersionLess(1))

# Anisotropic substrate
n_o = 2.0  #  ordinary index of thin layer
n_e = 2.5  #  extraordinary index of thin layer

uniaxialMaterial = elli.UniaxialMaterial(elli.DispersionLess(n_o),
                                       elli.DispersionLess(n_e))

# %% [markdown]
# ## We reproduce figure 6.16 (p. 238)
# %%
# Orientations of the anisotropic substrate
Φ_E = 90  #  1st Euler angle
θ_E_list = [0, 45, 90]  #  2nd Eulet angle

# Incidence angles
Φ_i_list = np.linspace(0, 89, 300)  #  array of Φ_i values

Psi = []

for θ_E in θ_E_list:
    R = elli.math.rotation_Euler(Φ_E, θ_E, 0)
    uniaxialMaterial.setRotation(R)
    s = elli.Structure(air, [], uniaxialMaterial)
    for Φ_i in Φ_i_list:
        data = s.evaluate(500, Φ_i)
        Psi.append(data.psi)

Psi = np.array(Psi)
Psi = Psi.reshape(3, 300).T

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(Φ_i_list, Psi)
ax.set_xlabel(r"$\theta_i$")
ax.set_ylabel(r"$\Psi_{pp}$")

plt.tight_layout()

# %% [markdown]
# ## We reproduce figure 6.17 (p. 239)

# %%
Φ_i = 70  #  70° incidence angle

# Orientations of the anisotropic substrate
Φ_E_list = np.linspace(0, 360, 36*2+1)  #  1st Euler angle
θ_E_list = [0, 45, 90]  #  2nd Euler angle

Psi = []

for θ_E in θ_E_list:
    evaluation_list = []
    for Φ_E in Φ_E_list:
        R = elli.math.rotation_Euler(Φ_E, θ_E, 0)
        uniaxialMaterial.setRotation(R)
        s = elli.Structure(air, [], uniaxialMaterial)
        data = s.evaluate(500, Φ_i)
        evaluation_list.append(data.psiMat[0,0,0])
    Psi.append(evaluation_list)

Psi = np.array(Psi).T

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(Φ_E_list, Psi)
ax.set_xlim(0, 360)
ax.set_xlabel(r"$\phi_E$")
ax.set_ylabel(r"$\Psi_{pp}$")

plt.tight_layout()
plt.show()

# %%
