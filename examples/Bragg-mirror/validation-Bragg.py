#!/usr/bin/python
# encoding: utf-8
# %% [markdown]
# # Validation for a TiO2/SiO2 Bragg mirror
#
# Author: O. Castany, C. Molinaro, M. Müller

# %%
import numpy as np
import elli
import elli.plot as elliplot
import matplotlib.pyplot as plt
from scipy.constants import pi

# %% [markdown]
# ## Structure definition
#
# ### Front and back materials

# %%
n_a = 1.0
n_g = 1.5
air = elli.ConstantRefractiveIndex(n_a).get_mat()
glass = elli.ConstantRefractiveIndex(n_g).get_mat()

# %% [markdown]
# ### Materials for a SiO2/TiO2 Bragg mirror

# %%
lbda0 = 1550  # nm
k0 = 2 * pi / lbda0
n_SiO2 = 1.47
n_TiO2 = 2.23 + 1j * 5.2e-4

SiO2 = elli.ConstantRefractiveIndex(n_SiO2).get_mat()
TiO2 = elli.ConstantRefractiveIndex(n_TiO2).get_mat()

# %% [markdown]
# ### Layers and Structure

# %%
d_SiO2 = elli.get_qwp_thickness(SiO2, lbda0)
d_TiO2 = elli.get_qwp_thickness(TiO2, lbda0)

L_SiO2 = elli.Layer(SiO2, d_SiO2)
L_TiO2 = elli.Layer(TiO2, d_TiO2)

# print("Thickness of the SiO2 QWP: {:.1f} nm".format(L_SiO2.h*1e9))
# print("Thickness of the TiO2 QWP: {:.1f} nm".format(L_TiO2.h*1e9))

# Repeated layers: n periods
Layerstack = elli.RepeatedLayers([L_TiO2, L_SiO2], 4, 0, 0)

# Number of interfaces
N = 2 * Layerstack.repetitions + 1

# Structure
s = elli.Structure(air, [Layerstack], glass)

# %% [markdown]
# ## Analytical calculation
# %%
n = np.ones(N + 1, dtype=complex)
n[0] = n_a
n[1::2] = n_TiO2
n[2::2] = n_SiO2
n[-1] = n_g

n.shape = (-1, 1)

d = np.ones(N + 1)
d[1::2] = L_TiO2.thickness  #  d[0] is not used
d[2::2] = L_SiO2.thickness

(lbda1, lbda2) = (1100, 2500)
lbda_list = np.linspace(lbda1, lbda2, 200)


def ReflectionCoeff(incidence_angle=0.0, polarisation="s"):
    """Returns the reflection coefficient in amplitude"""
    Kx = n[0] * np.sin(incidence_angle)
    sinPhi = Kx / n
    kz = 2 * pi / lbda_list * np.sqrt(n**2 - (Kx) ** 2)

    # Reflexion coefficient r_{k,k+1} for a single interface
    #    polarisation s:
    #    r_ab(p) = r_{p,p+1} = (kz(p)-kz(p+1))/(kz(p)+kz(p+1))
    #    polarisation p:
    #    r_ab(p) = r_{p,p+1} = (kz(p)*n[p+1]**2-kz(p+1)*n[p]**2) \
    #                          /(kz(p)*n[p]**2+kz(p+1)*n[p+1]**2)
    if polarisation == "s":
        r_ab = (-np.diff(kz, axis=0)) / (kz[:-1] + kz[1:])
    elif polarisation == "p":
        r_ab = (kz[:-1] * (n[1:]) ** 2 - kz[1:] * (n[:-1]) ** 2) / (
            kz[:-1] * (n[1:]) ** 2 + kz[1:] * (n[:-1]) ** 2
        )

    # Local function definition for recursive calculation
    def U(k):
        """Returns reflection coefficient U(k) = r_{k, {k+1,...,N}}

        Used recursively.
        """
        p = k + 1
        if p == N:
            res = r_ab[N - 1]
        else:
            res = (r_ab[p - 1] + U(p) * np.exp(2j * kz[p] * d[p])) / (
                1 + r_ab[p - 1] * U(p) * np.exp(2j * kz[p] * d[p])
            )
        return res

    return U(0)


# Power reflexion coefficient for different incidence angles and polarisations
R_th_ss_0 = (np.abs(ReflectionCoeff(0, "s"))) ** 2  # Phi_i = 0
R_th_ss = (np.abs(ReflectionCoeff(pi / 4, "s"))) ** 2  #  Phi_i = pi/4
R_th_pp = (np.abs(ReflectionCoeff(pi / 4, "p"))) ** 2

# %% [markdown]
# ## Calculation with pyElli
# %%
# Incidence angle Phi_i = 0, 's' polarization
data = s.evaluate(lbda_list, 0)

R_ss_0 = data.R_ss

# Incidence angle Phi_i = pi/4, 's' and 'p' polarizations
data2 = s.evaluate(lbda_list, np.rad2deg(pi / 4))

R_ss = data2.R_ss
R_pp = data2.R_pp

# %% [markdown]
# ## Plotting
# %%
fig = plt.figure(figsize=(12.0, 6.0))
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", "bgr")
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])

d = np.vstack((R_ss_0, R_ss, R_pp)).T
lines1 = ax.plot(lbda_list, d)
legend1 = ("R_ss (0$^\circ$)", "R_ss (45$^\circ$)", "R_pp (45$^\circ$)")

d = np.vstack((R_th_ss_0, R_th_ss, R_th_pp)).T
lines2 = ax.plot(lbda_list, d, "x")
legend2 = ("R_th_ss (0$^\circ$)", "R_th_ss (45$^\circ$)", "R_th_pp (45$^\circ$)")

ax.legend(
    lines1 + lines2,
    legend1 + legend2,
    loc="upper left",
    bbox_to_anchor=(1.05, 1),
    borderaxespad=0.0,
)

ax.set_title(
    r"Bragg mirror: Air/{TiO$_2$/SiO$_2$}x" + str(Layerstack.repetitions) + "/Glass"
)
ax.set_xlabel(r"Wavelength $\lambda$ (m)")
ax.set_ylabel(r"$R$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3, 3))

elliplot.draw_structure(s)
plt.show()

# %%
