#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# Example of a cholesteric liquid crystal

import numpy, Berreman4x4
from numpy import sin, sqrt, abs
from Berreman4x4 import c, pi, C, D, invC, invD
import matplotlib.pyplot as pyplot

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
p = 0.65e-6      # cholesteric pitch
TN = Berreman4x4.TwistedMaterial(LC, p/2, angle=+pi, div=40)

# Inhomogeneous layer, repeated layer, and structure
IL = Berreman4x4.InhomogeneousLayer(TN)
n = 25      # number of repetitions (half pitches)
L = Berreman4x4.RepeatedLayers([IL], n)
s = Berreman4x4.Structure(front, [L], back)

# Normal incidence: 
Kx = 0.0

# Calculation parameters
lbda_min, lbda_max = 0.6e-6, 1.5e-6   # (m)
lbda_list = numpy.linspace(lbda_min, lbda_max, 100)
k0_list = 2*pi/lbda_list

############################################################################
# Analytical calculation
R_th = (numpy.tanh(Dn*n*pi**2/(k0_list)))**2

############################################################################
# Calculation with Berreman4x4
J = numpy.array([s.getJones(Kx,k0) for k0 in k0_list])
power = abs(J)**2
T_pp = Berreman4x4.extractCoefficient(power, 't_pp')
R_pp = Berreman4x4.extractCoefficient(power, 'r_pp')
T_sp = Berreman4x4.extractCoefficient(power, 't_sp')
R_sp = Berreman4x4.extractCoefficient(power, 'r_sp')
# Note: the expression for T is valid if back and front media are identical

# Jones matrices for the circular wave basis
Jc = Berreman4x4.circularJones(J)
power = abs(Jc)**2

# R_LR, T_LR close to zero
R_RR = Berreman4x4.extractCoefficient(power, 'r_RR')
T_RR = Berreman4x4.extractCoefficient(power, 't_RR')

# T_RL, R_RL, R_LL close to zero
# T_LL close to 1
T_LL = Berreman4x4.extractCoefficient(power, 't_LL')
R_LL = Berreman4x4.extractCoefficient(power, 'r_LL')


############################################################################
# Plotting
fig = pyplot.figure()
# pyplot.rcParams['axes.color_cycle'] = ['b','b','b','b','g','r']
ax = fig.add_subplot("111")

# d1 = numpy.vstack((T_pp, R_pp, T_sp, R_sp)).T
# d2 = numpy.vstack((T_RR, R_RR, T_LR, R_LR)).T

# lines1 = ax.plot(lbda_list, d1)
# lines2 = ax.plot(lbda_list, d2)

# legend1 = ('T_pp', 'R_pp', 'T_sp', 'R_sp')
# legend2 = ('T_RR', 'R_RR', 'T_LR', 'R_LR')

ax.plot(lbda_list, R_RR, label='R_RR')
ax.plot(lbda_list, T_RR, label='T_RR')

# ax.legend(lines2, legend2, 
#           loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
ax.set_title(u"Cholesteric Liquid Crystal, {:d} helix full turns".format(n))
ax.set_xlabel(r"Wavelength $\lambda_0$ (m)")
ax.set_ylabel(r"Power transmission $T$ and reflexion $R$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))
pyplot.show()


