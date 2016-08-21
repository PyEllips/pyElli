#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Authors: O. Castany, C. Molinaro

# Interface between two materials n1/n2. Calculations of the transmission and 
# reflexion coefficients with varying incidence angle.

import numpy, Berreman4x4
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot
import sys

############################################################################
# Program parameters

if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print("Usage: interface-reflection.py [-h, --help] n1 n2\n")
    sys.exit()

if len(sys.argv) > 2:
    (n1, n2) = map(float, sys.argv[1:3])
else:
    (n1, n2) = (1.0, 1.5)    # default values

print("\n*** Interface n1 = {:} / n2 = {:} ***\n".format(n1,n2))

############################################################################
# Structure definition

# Materials
medium1 = Berreman4x4.IsotropicNonDispersiveMaterial(n1)
medium2 = Berreman4x4.IsotropicNonDispersiveMaterial(n2)

# Half-spaces
front = Berreman4x4.IsotropicHalfSpace(medium1)
back = Berreman4x4.IsotropicHalfSpace(medium2)

# Structure
s = Berreman4x4.Structure(front, [], back)

# Parameters for the calculation
lbda = 1e-6
k0 = 2*pi/lbda
Phi_i = numpy.linspace(0, pi/2*0.9999)  # range for the incidence angles

############################################################################
# Analytical calculation
Phi_t = numpy.arcsin((n1*numpy.sin(Phi_i)/n2).astype(complex))
kz1 = n1*k0*numpy.cos(Phi_i)
kz2 = n2*k0*numpy.cos(Phi_t)
r_s = (kz1 - kz2) / (kz1 + kz2)
t_s = 1 + r_s
r_p = (kz1 * n2**2 - kz2 * n1**2) / (kz1 * n2**2 + kz2 * n1**2)
t_p = numpy.cos(Phi_i)*(1-r_p)/numpy.cos(Phi_t)

# Reflection and transmission coefficients, polarisation s and p
R_th_ss = abs(r_s)**2
R_th_pp = abs(r_p)**2
t2_th_ss = abs(t_s)**2
t2_th_pp = abs(t_p)**2
# The power transmission coefficient is T = Re(kz2/kz1) × |t|^2
correction = numpy.real(kz2/kz1)  
T_th_ss = correction * t2_th_ss
T_th_pp = correction * t2_th_pp


############################################################################
# Calculation with Berreman4x4
Kx_list = front.get_Kx_from_Phi(Phi_i, k0)

data = Berreman4x4.DataList([s.evaluate(Kx,k0) for Kx in Kx_list])

# Extraction of the power coefficients
for name in ['R_ss', 'R_pp', 't_ss', 't_pp', 't_ss', 't_pp', 'T_ss', 'T_pp']:
    exec("{0:} = data.get('{0:}')".format(name))
t2_ss = data.get('t_ss')**2
t2_pp = data.get('t_pp')**2

############################################################################
# Plotting
fig = pyplot.figure(figsize=(12., 6.))
pyplot.rcParams['axes.prop_cycle'] = pyplot.cycler('color', 'bgrcbg')
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])

d = numpy.vstack((R_ss,R_pp,t2_ss,t2_pp,T_ss,T_pp)).T
lines1 = ax.plot(Kx_list, d)
legend1 = ("R_ss","R_pp","t2_ss","t2_pp","T_ss","T_pp")

d = numpy.vstack((R_th_ss,R_th_pp,t2_th_ss,t2_th_pp,T_th_ss,T_th_pp)).T
lines2 = ax.plot(Kx_list, d, 'o')
legend2 = ("R_th_ss","R_th_pp","t2_th_ss","t2_th_pp","T_th_ss","T_th_pp")

ax.legend(lines1 + lines2, legend1 + legend2, 
          loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

ax.set_title("Interface n$_1$={:} / n$_2$={:}".format(n1,n2))
ax.set_xlabel(r"Reduced wave vector $Kx$ ")
ax.set_ylabel(r"Reflexion and transmission coefficients $R$,$T$, $|t|^2$")

s.drawStructure()
print("Lines and circles should be superimposed!")
pyplot.show()

