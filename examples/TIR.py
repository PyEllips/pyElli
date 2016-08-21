#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# Total Internal Reflection 
# Glass / Air

import numpy, Berreman4x4
from Berreman4x4 import c, pi
from numpy import exp, cos, arcsin, real, sqrt
import matplotlib.pyplot as pyplot


print("\n*** Glass / Air ***\n")

############################################################################
# Structure definition

# Refractive indices
n_f = 1.5
n_b = 1.0

# Materials:
glass  = Berreman4x4.IsotropicNonDispersiveMaterial(n_f)
air    = Berreman4x4.IsotropicNonDispersiveMaterial(n_b)

# Layer and half-spaces:
front = Berreman4x4.IsotropicHalfSpace(glass)
back  = Berreman4x4.IsotropicHalfSpace(air)

# Structure:
s = Berreman4x4.Structure(front, [], back)

# Wavelength and wavenumber:
lbda = 1e-6
k0 = 2*pi/lbda

# Variation of incidence angle
Phi_list = numpy.linspace(0, pi/2*0.999)
Kx = front.get_Kx_from_Phi(Phi_list)

############################################################################
# Calculation with Berreman4x4
data = Berreman4x4.DataList([s.evaluate(kx,k0) for kx in Kx])

R_p = data.get('R_pp')
R_s = data.get('R_ss')
T_p = data.get('T_pp')
T_s = data.get('T_ss')

############################################################################
# Plotting
fig = pyplot.figure(figsize=(12., 6.))
pyplot.rcParams['axes.prop_cycle'] = pyplot.cycler('color', 'bgrcbg')
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])

y = numpy.vstack((R_s,R_p)).T
legend = ("R_s","R_p")
# lines = ax.plot(Kx, y)
lines = ax.plot(Phi_list*180/pi, y)

ax.legend(lines, legend, 
          loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

ax.set_title("FTIR: Glass / Air")
ax.set_xlabel(u"Angle of incidence (°)")
ax.set_ylabel(r"Reflexion coefficients $R$")
ax.set_ylim(top=1.05)

try: 
    __IPYTHON__     # Are we using ipython?
    pyplot.ion()    # Turn on interactive mode
except NameError:
    pass

# s.drawStructure()
pyplot.show()

