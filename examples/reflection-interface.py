#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# The simplest example: a homogeneous glass layer in air

import numpy, Berreman4x4
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot
import sys

if len(sys.argv) > 2:
    (n1, n2) = map(float, sys.argv[1:3])
else:
    (n1, n2) = (1.0,1.5)    # default values

situation = "$n_i$={:}/$n_t$={:}".format(n1,n2)
print situation 

print("\n*** Medium1 n="+str(n1)+" / Medium2 n="+str(n2)+" interface ***\n")
# Materials:
medium1 = Berreman4x4.IsotropicNonDispersiveMaterial(n1)
medium2 = Berreman4x4.IsotropicNonDispersiveMaterial(n2)

# Half-spaces:
front = Berreman4x4.IsotropicHalfSpace(medium1)
back = Berreman4x4.IsotropicHalfSpace(medium2)

# Structure:
s = Berreman4x4.Structure(front, [], back)

# Wavelength and wavenumber:
lbda = 1e-6
k0 = 2*pi/lbda

##Calculations of power coefficients
# Variation of the incidence angle  (Kx)
Phi_i = numpy.linspace(0, numpy.pi/2*0.99)
Kx_list = front.get_Kx_from_Phi(Phi_i,k0)
l = []
for Kx in Kx_list:
    l.append(s.getJones(Kx,k0))

data = numpy.array(l)

##Theorie
Phi_t = numpy.arcsin((n1*numpy.sin(Phi_i)/n2).astype(complex))
k1 = n1*k0*numpy.cos(Phi_i)
k2 = n2*k0*numpy.cos(Phi_t)
r_s = (k1-k2)/(k1+k2)
t_s = 1 + r_s
es1 = n1**2
es2 = n2**2
r_p = (k1*es2-k2*es1)/(k1*es2+k2*es1)
t_p = numpy.cos(Phi_i)*(1-r_p)/numpy.cos(Phi_t)

# Reflection and transmission coefficients, polarisation s and p
R_th_ss = (numpy.abs(r_s))**2
T_part_th_ss = (numpy.abs(t_s))**2
R_th_pp = (numpy.abs(r_p))**2
T_part_th_pp = (numpy.abs(t_p))**2
correction = numpy.real(n2*numpy.cos(Phi_t)/(n1*numpy.cos(Phi_i)))  
#this term is a correction term used in R+correction*T=1
# The real part is taken because T = Re(k2/k1)|t|^2
T_th_ss = T_part_th_ss*correction
T_th_pp = T_part_th_pp*correction

# Calculations of the power coefficients
data = (numpy.abs(data))**2
R_ss = Berreman4x4.extractCoefficient(data, 'r_ss')
R_pp = Berreman4x4.extractCoefficient(data, 'r_pp')
T_part_ss = Berreman4x4.extractCoefficient(data, 't_ss')
T_part_pp = Berreman4x4.extractCoefficient(data, 't_pp')
T_ss = T_part_ss*correction
T_pp = T_part_pp*correction

d = numpy.vstack((R_ss,R_pp,T_part_ss,T_part_pp,T_ss,T_pp)).T
fig = pyplot.figure()
ax = fig.add_subplot("111")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.93, box.height])
lines = ax.plot(Kx_list, d, 
        Kx_list, R_th_ss, 'bo', Kx_list, R_th_pp, 'go',
        Kx_list, T_part_th_ss, 'ro', Kx_list, T_part_th_pp, 'co',
        Kx_list, T_th_ss, 'mo', Kx_list, T_th_pp, 'yo')
ax.legend(lines, ("R_ss","R_pp","T_part_ss","T_part_pp","T_ss","T_pp","R_th_ss","R_th_pp","T_part_th_ss","T_part_th_pp", "T_th_ss","T_th_pp"), bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.set_title("Light incident on a glass - air interface with variable incidence")
ax.set_xlabel(r"Reduced wave vector $Kx$ ")
ax.set_ylabel(r"Reflexion  and transmission coefficients $R$,$T$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))
pyplot.show()

