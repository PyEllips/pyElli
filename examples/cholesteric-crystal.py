#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# Example of a 180° twisted nematic liquid crystal with n periods

import numpy, Berreman4x4
from numpy import sin, sqrt, abs
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot

"""
Consider the following situation:
- twisted liquid crystal with 90° twist between z=0 and z=d
- liquid crystal aligned along x at z=0.
- output polarizer aligned parallel to x

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
n_med = (ne + no)/2
LC = Berreman4x4.UniaxialNonDispersiveMaterial(no, ne)
R = Berreman4x4.rotation_v_theta([0,1,0], pi/2)
LC = LC.rotated(R)
p = 0.5e-6
TN = Berreman4x4.TwistedMaterial(LC, p, angle=pi, div=40)

# Inhomogeneous layer
IL = Berreman4x4.InhomogeneousLayer(TN)
# IL.setMethod("symplectic","Padé",3)

# Repeated layers: n periods
n = 8
L = Berreman4x4.RepeatedLayers([IL], n, 0, 0)

# Structure
s = Berreman4x4.Structure(front, [L], back)

# Normal incidence: 
Kx = 0.0

# Calculation parameters
lbda_min, lbda_max = 3e-7, 5e-6   # (m)
lbda_list = numpy.linspace(lbda_min, lbda_max,200)
k0_list = 2*pi/lbda_list#numpy.linspace(2*pi/lbda_max, 2*pi/lbda_min,200)#2*pi/lbda_list

############################################################################
# Analytical calculation
R_th = (numpy.tanh(Dn*n*pi**2/(k0_list)))**2

############################################################################
# Calculation with Berreman4x4
data = [s.getJones(Kx,k0) for k0 in k0_list]
data = numpy.array(data)
t_pp = Berreman4x4.extractCoefficient(data, 't_pp')
r_pp = Berreman4x4.extractCoefficient(data, 'r_pp')
T_pp = (abs(t_pp))**2    # valid if back and front media are identical
R_pp = (abs(r_pp))**2

############################################################################
# Plotting
fig = pyplot.figure(figsize=(12., 6.))
pyplot.rcParams['axes.color_cycle'] = ['b','g','r']
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])

d = numpy.vstack((T_pp, R_pp)).T
lines1 = ax.plot(lbda_list, d,lbda_list, R_th,'x')
legend1 = ("T_pp", "R_pp", "R_th")

ax.legend(lines1, legend1, loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
#ax.set_title(u"180° Twisted Nematic Liquid Crystal, " + "d = {:.3f} µm".format(d*1e6))
ax.set_xlabel(r"Wave length $\lambda_0$ (m)")
ax.set_ylabel(r"Power transmission $T$ and reflexion $R$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))
pyplot.show()


