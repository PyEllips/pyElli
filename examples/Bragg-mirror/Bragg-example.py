#!/usr/bin/python
# encoding: utf-8
# %% [markdown]
# # Example of a TiO2/SiO2 Bragg mirror with 8.5 periods
#
# Author: O. Castany, M.Müller

# %%
import elli
import elli.plot.structure as elliplot
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(suppress=True, precision=3)

# %% [markdown]
# ## Front and back materials

# %%
air = elli.IsotropicMaterial(elli.DispersionLess(1.0))
glass = elli.IsotropicMaterial(elli.DispersionLess(1.5))

# %% [markdown]
# ## Materials for a SiO2/TiO2 Bragg mirror

# %%
n_SiO2 = 1.47
n_TiO2 = 2.23 + 1j * 5.2e-4

SiO2 = elli.IsotropicMaterial(elli.DispersionLess(n_SiO2))
TiO2 = elli.IsotropicMaterial(elli.DispersionLess(n_TiO2))

# %% [markdown]
# ## Calculate layer thickness as quarterwaveplates

# %%
lbda0 = 1550

d_SiO2 = elli.get_qwp_thickness(SiO2, lbda0)
d_TiO2 = elli.get_qwp_thickness(TiO2, lbda0)

print("Thickness of the SiO2 QWP: {} nm".format(d_SiO2))
print("Thickness of the TiO2 QWP: {} nm".format(d_TiO2))

# %% [markdown]
# ## Create layers and structure

# %%
L_SiO2 = elli.Layer(SiO2, d_SiO2)
L_TiO2 = elli.Layer(TiO2, d_TiO2)

# Repeated layers: 8.5 periods
Layerstack = elli.RepeatedLayers([L_TiO2, L_SiO2], 8, 0, 1)

s = elli.Structure(air, [Layerstack], glass)

# %% [markdown]
# ## Calculation

# %%
(lbda1, lbda2) = (1100, 2500)
lbda_list = np.linspace(lbda1, lbda2, 200)

data = s.evaluate(lbda_list, 0)

R = data.R[:, 1, 1]
T = data.T[:, 1, 1]

# %% [markdown]
# ## Plotting

# %%
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(lbda_list, R, label="$R$")
ax.plot(lbda_list, T, label="$T$")
ax.legend(loc='center right')
ax.set_xlabel(r"Wavelength $\lambda$ (nm)")
ax.set_ylabel(r"Power reflection $R$ or transmission $T$")
ax.set_title(r"Bragg mirror: Air/{TiO$_2$/SiO$_2$}x8/TiO$_2$/Glass")
plt.show()

# %% [markdown]
# ## Structure Graph

# %%
elliplot.drawStructure(s)
