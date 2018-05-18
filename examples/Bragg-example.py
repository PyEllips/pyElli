#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# Example of a TiO2/SiO2 Bragg mirror with 8.5 periods

import numpy, Berreman4x4
import scipy.linalg
import matplotlib.pyplot as pyplot
from Berreman4x4 import c, pi

print("\n*** SiO2/TiO2 Bragg mirror ***\n")

# Front and back materials
air = Berreman4x4.IsotropicNonDispersiveMaterial(1.0)
glass = Berreman4x4.IsotropicNonDispersiveMaterial(1.5)

front = Berreman4x4.IsotropicHalfSpace(air)
back = Berreman4x4.IsotropicHalfSpace(glass)

# Materials for a SiO2/TiO2 Bragg mirror
lbda0 = 1.550e-6
k0 = 2*pi/lbda0
nr_SiO2 = 1.47
nr_TiO2 = 2.23
alpha_SiO2 = 0e2    # (m⁻¹)
alpha_TiO2 = 42e2   # (m⁻¹)
ni_SiO2 = alpha_SiO2 * lbda0 / (4*pi)
ni_TiO2 = alpha_TiO2 * lbda0 / (4*pi)
n_SiO2 = nr_SiO2 + 1j * ni_SiO2
n_TiO2 = nr_TiO2 + 1j * ni_TiO2

SiO2 = Berreman4x4.IsotropicNonDispersiveMaterial(n_SiO2)
TiO2 = Berreman4x4.IsotropicNonDispersiveMaterial(n_TiO2)

# Layers
L_SiO2 = Berreman4x4.HomogeneousIsotropicLayer(SiO2, ("QWP", lbda0))
L_TiO2 = Berreman4x4.HomogeneousIsotropicLayer(TiO2, ("QWP", lbda0))

print("Thickness of the SiO2 QWP: {:.1f} nm".format(L_SiO2.h*1e9))
print("Thickness of the TiO2 QWP: {:.1f} nm".format(L_TiO2.h*1e9))

# Repeated layers: 8.5 periods
L = Berreman4x4.RepeatedLayers([L_TiO2, L_SiO2], 8, 0, 1)

# To reduce the number of printed characters in the numbers:
# numpy.set_printoptions(suppress=True, precision=3)
Kx = 0.0

# Structure
s = Berreman4x4.Structure(front, [L], back)

# Calculation
(lbda1, lbda2) = (1.1e-6, 2.5e-6)
lbda_list = numpy.linspace(lbda1, lbda2, 200)

data = Berreman4x4.DataList([s.evaluate(Kx, 2*pi/lbda) for lbda in lbda_list])

R = data.get('R_ss')
T = data.get('T_ss')

# Plotting 
fig = pyplot.figure()
ax = fig.add_subplot("111")
ax.plot(lbda_list, R, label="$R$")
ax.plot(lbda_list, T, label="$T$")

ax.legend(loc='center right')
ax.set_xlabel(r"Wavelength $\lambda$ (m)")
ax.set_ylabel(r"Power reflection $R$ or transmission $T$")
ax.set_title(r"Bragg mirror: Air/{TiO$_2$/SiO$_2$}x8/TiO$_2$/Glass")

fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))

s.drawStructure()
pyplot.show()

