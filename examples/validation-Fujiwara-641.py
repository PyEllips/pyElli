#!/usr/bin/python
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
Phi_E = pi/2                        # 1st Euler angle
Theta_E_list = [0, pi/4, pi/2]      # 2nd Eulet angle

# Incidence angles
Phi_i_list = numpy.linspace(0, 0.999*pi/2, 37)  # array of Phi_i values
Phi_i_deg = Phi_i_list*180/pi
Kx_list = front.get_Kx_from_Phi(Phi_i_list)     # array of Kx values

data = []
for Theta_E in Theta_E_list:
    R = Berreman4x4.rotation_Euler((Phi_E, Theta_E, 0))
    back.setMaterial(uniaxialMaterialRef.rotated(R))
    l = []
    for Kx in Kx_list:
        Jr = s.getJones(Kx)[0]
        l.append(Berreman4x4.extractEllipsoParam(Jr))
    data.append(l)
data = numpy.array(data)

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.plot(Phi_i_deg, data[:,:,0,0].T)
ax.set_xlabel(r"$\theta_i$")
ax.set_ylabel(r"$\Psi_{pp}$")

pyplot.tight_layout()

##############################################################################
# We reproduce figure 6.17

print("We reproduce figure 6.17, p. 239...")
Phi_i = 70*pi/180   # 70° incidence angle 
Kx = front.get_Kx_from_Phi(Phi_i)

# Orientations of the anisotropic substrate
Phi_E_list = numpy.linspace(0, 2*pi, 36*2+1)    # 1st Euler angle
Phi_E_deg = Phi_E_list*180/pi
Theta_E_list = [0, pi/4, pi/2]                  # 2nd Eulet angle

data = []
for Theta_E in Theta_E_list:
    l = []
    for Phi_E in Phi_E_list:
        R = Berreman4x4.rotation_Euler((Phi_E, Theta_E, 0))
        back.setMaterial(uniaxialMaterialRef.rotated(R))
        Jr = s.getJones(Kx)[0]
        l.append(Berreman4x4.extractEllipsoParam(Jr))
    data.append(l)
data = numpy.array(data)

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.plot(Phi_E_deg, data[:,:,0,0].T)
ax.set_xlim(0,360)
ax.set_xlabel(r"$\phi_E$")
ax.set_ylabel(r"$\Psi_{pp}$")

pyplot.tight_layout()
pyplot.show()


