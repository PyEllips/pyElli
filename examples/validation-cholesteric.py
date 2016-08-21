#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# Example of a cholesteric liquid crystal 

import numpy, Berreman4x4
from numpy import sin, sqrt, abs, exp
from Berreman4x4 import c, pi, e_y
import matplotlib.pyplot as pyplot

############################################################################
# Structure

# Materials
glass = Berreman4x4.IsotropicNonDispersiveMaterial(1.6)
front = back = Berreman4x4.IsotropicHalfSpace(glass)

# Liquid crystal oriented along the x direction
(no, ne) = (1.5, 1.7)
Dn = ne-no
n_med = (ne + no)/2
LC = Berreman4x4.UniaxialNonDispersiveMaterial(no, ne)  # ne along z
R = Berreman4x4.rotation_v_theta(e_y, pi/2)         # rotation round y
LC = LC.rotated(R)              # apply rotation from z to x
# Cholesteric pitch:
p = 0.65e-6
# One half turn of a right-handed helix:
TN = Berreman4x4.TwistedMaterial(LC, p/2, angle=+pi, div=25)

# Inhomogeneous layer, repeated layer, and structure
IL = Berreman4x4.InhomogeneousLayer(TN)
N = 5 # number half pitch repetitions
h = N * p/2
L = Berreman4x4.RepeatedLayers([IL], N)
s = Berreman4x4.Structure(front, [L], back)

# Normal incidence: 
Kx = 0.0

# Calculation parameters
lbda_min, lbda_max = 0.6e-6, 1.5e-6   # (m)
lbda = numpy.linspace(lbda_min, lbda_max, 100)
k0 = 2*pi/lbda

############################################################################
# Analytical calculation for the power reflection coefficient
q = 2*pi/p
alpha = q/k0
epsilon = (no**2+ne**2)/2
delta = (no**2-ne**2)/2
n2 = sqrt((alpha**2 + epsilon \
     - sqrt(4*epsilon*alpha**2+delta**2)).astype(complex))
w = 1j*(ne**2-n2**2-alpha**2)/(2*alpha*n2) # not k0/c 
A = -2j*k0*n2*h

R_th = abs((w**2+1)*(1-exp(-2j*k0*n2*h)) \
           / (2*w*(1+exp(-2j*k0*n2*h)) \
           - 1j*(w**2-1)*(1-exp(-2j*k0*n2*h))))**2

############################################################################
# Calculation with Berreman4x4
data = Berreman4x4.DataList([s.evaluate(Kx,_k0) for _k0 in k0])

# Jones matrices for the circular wave basis
# Right-circular wave is reflected in the stop-band
# R_LR, T_LR close to zero
R_RR = data.get('R_RR')

############################################################################
# Plotting
fig = pyplot.figure()
ax = fig.add_subplot("111")

ax.plot(lbda, R_RR, label='R_RR')
ax.plot(lbda, R_th, 'r', label='R_th')

ax.legend(loc='center right', bbox_to_anchor=(1.00, 0.50))

ax.set_title("Right-handed Cholesteric Liquid Crystal, " +
             "{:.1f} helix pitches".format(N/2.))
ax.set_xlabel(r"Wavelength $\lambda_0$ (m)")
ax.set_ylabel(r"Power reflexion $R$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))

s.drawStructure()
pyplot.show()

