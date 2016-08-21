#!/usr/bin/python3
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# Verification of the code against results presented in Fujiwara's book 
# p. 237 (section 6.4.1). We reproduce figures 6.16 and 6.17.

import numpy, Berreman4x4
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot

n_i = 1.0       # incident medium is air
n_o = 2.0       # ordinary index of thin layer
n_e = 2.5       # extraordinary index of thin layer

##############################################################################
# Setting up the structure

# Front half-space (air)
air = Berreman4x4.IsotropicNonDispersiveMaterial(n_i)
front = Berreman4x4.IsotropicHalfSpace(air)

# Anisotropic substrate
uniaxialMaterialRef = Berreman4x4.UniaxialNonDispersiveMaterial(n_o,n_e)
back = Berreman4x4.HalfSpace()

s = Berreman4x4.Structure(front, [], back)

##############################################################################
# We reproduce figure 6.16
print("\nWe reproduce results from section 6.4.1 in " + 
      "'Spectroscopic Ellipsometry',\nby H. Fujiwara.\n")
print("*** Air / anisotropic sample ***")
print("We reproduce figure 6.16, p. 238...")

# Orientations of the anisotropic substrate
Φ_E = pi/2                      # 1st Euler angle
θ_E_list = [0, pi/4, pi/2]      # 2nd Eulet angle

# Incidence angles
Φ_i_list = numpy.linspace(0, 0.999*pi/2, 300)   # array of Φ_i values
Φ_i_deg = Φ_i_list*180/pi
Kx_list = front.get_Kx_from_Phi(Φ_i_list)       # array of Kx values

data = Berreman4x4.DataList()
for θ_E in θ_E_list:
    R = Berreman4x4.rotation_Euler((Φ_E, θ_E, 0))
    back.setMaterial(uniaxialMaterialRef.rotated(R))
    data.append([s.evaluate(Kx) for Kx in Kx_list])

Psi = data.get('Ψ')

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.plot(Φ_i_deg, Psi.T)
ax.set_xlabel(r"$\theta_i$")
ax.set_ylabel(r"$\Psi_{pp}$")

pyplot.tight_layout()

##############################################################################
# We reproduce figure 6.17

print("We reproduce figure 6.17, p. 239...")
Φ_i = 70*pi/180   # 70° incidence angle 
Kx = front.get_Kx_from_Phi(Φ_i)

# Orientations of the anisotropic substrate
Φ_E_list = numpy.linspace(0, 2*pi, 36*2+1)  # 1st Euler angle
Φ_E_deg = Φ_E_list*180/pi
θ_E_list = [0, pi/4, pi/2]                  # 2nd Eulet angle

data = Berreman4x4.DataList()
for θ_E in θ_E_list:
    evaluation_list = []
    for Φ_E in Φ_E_list:
        R = Berreman4x4.rotation_Euler((Φ_E, θ_E, 0))
        back.setMaterial(uniaxialMaterialRef.rotated(R))
        evaluation_list.append(s.evaluate(Kx))
    data.append(evaluation_list)

Psi = data.get('Ψ')

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.plot(Φ_E_deg, Psi.T)
ax.set_xlim(0,360)
ax.set_xlabel(r"$\phi_E$")
ax.set_ylabel(r"$\Psi_{pp}$")

pyplot.tight_layout()
pyplot.show()

