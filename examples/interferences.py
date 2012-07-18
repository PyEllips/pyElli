#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# The simplest example: a homogeneous glass layer in air

import numpy, Berreman4x4
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot

print("\n*** Air / glass / air ***\n")

# Materials:
air = Berreman4x4.IsotropicNonDispersiveMaterial(1.0)
glass = Berreman4x4.IsotropicNonDispersiveMaterial(1.5)

# Layer and half-spaces:
layer = Berreman4x4.HomogeneousIsotropicLayer(glass)
front = back = Berreman4x4.IsotropicHalfSpace(air)

# Structure:
s = Berreman4x4.Structure(front, [layer], back)

# Wavelength and wavenumber:
lbda = 1e-6
k0 = 2*pi/lbda

# Incidence angle (Kx = n sin(Φ):
Kx = 0.5

# Variation of the reflexion and transmission coefficients with the
# thickness of the glass layer:
h_list = numpy.linspace(0, 1.0e-6)
l = []
for h in h_list:
    layer.setThickness(h)
    l.append(s.getJones(Kx,k0))
data = numpy.array(l)

# Calculate the power coefficients
data = numpy.abs(data)**2
R_pp = Berreman4x4.extractCoefficient(data, 'r_pp')
R_ss = Berreman4x4.extractCoefficient(data, 'r_ss')
T_pp = Berreman4x4.extractCoefficient(data, 't_pp')
T_ss = Berreman4x4.extractCoefficient(data, 't_ss')

d = numpy.vstack((R_pp,R_ss,T_pp,T_ss)).T
fig = pyplot.figure()
ax = fig.add_subplot("111")
lines = ax.plot(h_list, d)
ax.legend(lines, ("R_pp","R_ss","T_pp","T_ss"))
ax.set_title("Light incident on a glass layer, with oblique incidence")
ax.set_xlabel(r"Glass layer thickness, $h$ (m)")
ax.set_ylabel(r"Reflexion and transmission coefficients $R$, $T$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))
pyplot.show()

