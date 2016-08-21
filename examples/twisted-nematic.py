#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# Example of a 90° twisted nematic liquid crystal

import numpy, Berreman4x4
from numpy import sin, sqrt
from Berreman4x4 import c, pi, e_y
import matplotlib.pyplot as pyplot

"""
Consider the following situation:
- twisted liquid crystal with 90° twist between z=0 and z=d
- liquid crystal aligned along x at z=0.
- input and output polarizers aligned parallel to x

Gooch-Tarry law gives: T_pp = sin²(pi/2·√(1+u²)) / (1+u²),
with u = 2dΔn/λ. 
The transmission minima are given by u = ((2m)²-1)^{-1/2} = √(3),√(15),√(35),…

We consider a birefringence Δn = 0.10 and a thickness d = 4.33 µm. The first
minimum should be at λ = 500 nm, or k0 = 1.257e7 m⁻¹.

Note: Gooch-Tarry law does not take into account interferences between the two
glass substrates. A glass with n = 1.55 minimizes the interferences.
"""

# Materials
glass = Berreman4x4.IsotropicNonDispersiveMaterial(1.55)
front = back = Berreman4x4.IsotropicHalfSpace(glass)

# Liquid crystal oriented along the x direction
(no, ne) = (1.5, 1.6)
Dn = ne-no
LC = Berreman4x4.UniaxialNonDispersiveMaterial(no, ne)
R = Berreman4x4.rotation_v_theta(e_y, pi/2)
LC = LC.rotated(R)
d = 4.33e-6
TN = Berreman4x4.TwistedMaterial(LC, d)

# Inhomogeneous layer
IL = Berreman4x4.InhomogeneousLayer(TN)

# Structure
s = Berreman4x4.Structure(front, [IL], back)

# Normal incidence: 
Kx = 0.0

# Calculation parameters
(lbda_min, lbda_max) = (200e-9, 1)   # (m)
k0_list = numpy.linspace(2*pi/lbda_max, 2*pi/lbda_min)

# Plot setup
fig = pyplot.figure()
ax = fig.add_subplot("111")

# Plot Gooch-Tarry law, for comparison
u = 2*d*Dn*k0_list/(2*pi)
T = sin(pi/2*sqrt(1+u**2))**2 / (1+u**2)
ax.plot(k0_list, T, label="Gooch-Tarry law")

# Calulation with Berreman4x4 and plotting
def plotTransmission(label):
    """Plots power transmission vs. wavenumber."""
    data = Berreman4x4.DataList([s.evaluate(Kx,k0) for k0 in k0_list])
    T = data.get('T_pp')
    ax.plot(k0_list, T, 'x', label=label)

# Two plots are mad, with different numbers of divisions in the TwistedMaterial
TN.setDivision(7)
plotTransmission("Berreman4x4, 7 div")
TN.setDivision(18) 
plotTransmission("Berreman4x4, 18 div")

# Titles
ax.set_title(u"90° Twisted Nematic Liquid Crystal, " + 
             u"d = {:.2f} µm".format(d*1e6))
ax.set_xlabel(r"Wavenumber $k_0$ (m$^{-1}$)")
ax.set_ylabel(r"Power transmission $T$")
ax.legend()

s.drawStructure()
pyplot.show()

