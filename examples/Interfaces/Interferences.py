#!/usr/bin/python
# encoding: utf-8
# %% [markdown]
# # The simplest example: a homogeneous glass layer in air
#
# Berreman4x4 example
# Author: O. Castany, M. Müller
# %%
import numpy as np
import elli
import matplotlib.pyplot as plt

# %%
# Materials:
air = elli.IsotropicMaterial(elli.DispersionLess(1.0))
glass = elli.IsotropicMaterial(elli.DispersionLess(1.5))

# Layer and half-spaces:
layer = elli.Layer(glass, 1)
front = back = air

# Structure:
s = elli.Structure(front, [layer], back)

# %%
# Wavelength and wavenumber:
lbda = 1000      # nm

# Incidence angle:
angle = 30

# %%
# Variation of the reflexion and transmission coefficients with the
# thickness of the glass layer:
h_list = np.linspace(0, 1000, 1000)

R = []
T = []

for h in h_list:
    layer.setThickness(h)
    data = s.evaluate(lbda, angle)
    R.append(data.R[0])
    T.append(data.T[0])
    
R = np.array(R)
T = np.array(T)

# %%
plt.figure(figsize=(12., 6.))
plt.plot(h_list, np.real(R[:, 0, 0]), label='R_pp')
plt.plot(h_list, np.real(R[:, 1, 1]), label='R_ss')
plt.plot(h_list, np.real(T[:, 0, 0]), label='T_pp')
plt.plot(h_list, np.real(T[:, 1, 1]), label='T_ss')
plt.title("Glass layer at 30 degree incidence angle")
plt.xlabel(u"Layer thickness (nm)")
plt.ylabel(r"Reflexion coefficients $R$")
plt.legend()
plt.show()

# %%
