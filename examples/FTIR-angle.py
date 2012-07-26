#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# Frustrated Total Internal Reflection 
# Glass1 / Air / Glass2

import numpy, Berreman4x4
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot

print("\n*** Glass1 / Air / Glass2 ***\n")

############################################################################
# Structure definition

# Refractive indices
n_f = 1.5
n   = 1.0
n_b = 1.7

# Materials:
glass1 = Berreman4x4.IsotropicNonDispersiveMaterial(n_f)
air    = Berreman4x4.IsotropicNonDispersiveMaterial(n)
glass2 = Berreman4x4.IsotropicNonDispersiveMaterial(n_b)

# Layer and half-spaces:
front = Berreman4x4.IsotropicHalfSpace(glass1)
layer = Berreman4x4.HomogeneousIsotropicLayer(air)
back  = Berreman4x4.IsotropicHalfSpace(glass2)

# Structure:
s = Berreman4x4.Structure(front, [layer], back)

# Wavelength and wavenumber:
lbda = 1e-6
k0 = 2*pi/lbda

# Layer thickness
h = lbda*0.347
layer.setThickness(h)

# Variation of incidence angle
Phi_list = numpy.linspace(0, pi/2*0.999)
Kx = Kx_list = front.get_Kx_from_Phi(Phi_list)

############################################################################
# Analytical calculation
# Incidence angle
Phi_b = numpy.arcsin(((Kx_list)/n_b).astype(complex))
Phi_n = numpy.arcsin((Kx_list/n).astype(complex))

# Wave vector:
k_f = n_f*k0*numpy.cos((numpy.arcsin((Kx_list/n_f).astype(complex))))
k_n = k0*numpy.sqrt((-((Kx_list)**2 - n**2)).astype(complex))
k_b = n_b*k0*numpy.cos(Phi_b)

# Amplitude coefficient for 's' polarisation:
r_nf = (k_f-k_n)/(k_n+k_f)
r_bn = (k_n-k_b)/(k_n+k_b)
t_nf = 1+r_nf
t_bn = 1+r_bn

# Amplitude coefficient for 'p' polarisation:
r_nfp = (k_f*n**2-k_n*n_f**2)/(k_n*n_f**2+k_f*n**2)
r_bnp = (k_n*n_b**2-k_b*n**2)/(k_n*n_b**2+k_b*n**2)
t_nfp = numpy.cos((numpy.arcsin((Kx_list/n_f).astype(complex))))*(1-r_nfp)/numpy.cos(Phi_n)
t_bnp = numpy.cos(Phi_n)*(1-r_bnp)/numpy.cos(Phi_b)

# Power coefficients:
R_th_ss = (numpy.abs((r_nf+r_bn*numpy.exp(2j*k_n*h))/(1+r_bn*r_nf*numpy.exp(2j*k_n*h))))**2

t2_th_ss = (numpy.abs((t_bn*t_nf*numpy.exp(1j*k_n*h))/(1+r_bn*r_nf*numpy.exp(2j*k_n*h))))**2

R_th_pp = (numpy.abs((r_nfp+r_bnp*numpy.exp(2j*k_n*h))/(1+r_bnp*r_nfp*numpy.exp(2j*k_n*h))))**2

t2_th_pp= (numpy.abs((t_bnp*t_nfp*numpy.exp(1j*k_n*h))/(1+r_bnp*r_nfp*numpy.exp(2j*k_n*h))))**2

correction = numpy.real(n_b*numpy.cos(Phi_b)/(n_f*numpy.cos(numpy.arcsin((Kx_list/n_f).astype(complex)))))
# This is a correction term used in R +T*correction = 1

T_th_ss = t2_th_ss*correction
T_th_pp = t2_th_pp*correction

####################################################################
# Calculation with Berreman4x4
data = numpy.array([s.getJones(Kx,k0) for Kx in Kx_list])

data = abs(data)**2
R_pp  = Berreman4x4.extractCoefficient(data, 'r_pp')
R_ss  = Berreman4x4.extractCoefficient(data, 'r_ss')
t2_pp = Berreman4x4.extractCoefficient(data, 't_pp')
t2_ss = Berreman4x4.extractCoefficient(data, 't_ss')
T_ss = t2_ss*correction
T_pp = t2_pp*correction

############################################################################
# Plotting
fig = pyplot.figure(figsize=(12., 6.))
pyplot.rcParams['axes.color_cycle'] = ['b','g','r','c','b','g']
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])

d = numpy.vstack((R_ss,R_pp,t2_ss,t2_pp,T_ss,T_pp)).T
legend1 = ("R_ss","R_pp","t2_ss","t2_pp","T_ss","T_pp")
lines1 = ax.plot(Kx_list,d)

d = numpy.vstack((R_th_ss,R_th_pp,t2_th_ss,t2_th_pp,T_th_ss,T_th_pp)).T
legend2 = ("R_th_ss","R_th_pp","t2_th_ss","t2_th_pp","T_th_ss","T_th_pp")
lines2 = ax.plot(Kx_list,d, 'x')

ax.legend(lines1 + lines2, legend1 + legend2, 
          loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

ax.set_title("FTIR: Glass1 / Air ($h$ = {:.3g} m) / Glass2".format(h))
ax.set_xlabel(r"Reduced wave number, $Kx$")
ax.set_ylabel(r"Reflexion and transmission coefficients $R$, $T$")
pyplot.show()

