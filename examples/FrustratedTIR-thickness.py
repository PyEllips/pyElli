#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# Frustrated Total Internal Reflection 
# Glass1 / Air / Glass2

import numpy, Berreman4x4
from Berreman4x4 import c, pi
from numpy import exp, cos, arcsin, real, sqrt
import matplotlib.pyplot as pyplot

print("\n*** Glass1 / Air / Glass2 ***\n")

############################################################################
# Structure definition

# Refractive indices
n_f = 1.5
n_s = 1.0
n_b = 1.7

# Materials:
glass1 = Berreman4x4.IsotropicNonDispersiveMaterial(n_f)
air    = Berreman4x4.IsotropicNonDispersiveMaterial(n_s)
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
Phi_i = pi/2 * 0.6   # Incidence angle (higher than the limit angle)

# Air thickness variation range
d = numpy.linspace(0, 1.0e-6)

############################################################################
# Analytical calculation

Kx = n_f*numpy.sin(Phi_i) # Reduced wavenumber

# Incidence angle
Phi_s = arcsin((complex(Kx/n_s)))
Phi_b = arcsin(Kx/n_b)

# Wave vector:
kz_f = n_f*k0*cos(Phi_i)
kz_s = k0*sqrt(complex(n_s**2 - Kx**2))
kz_b = n_b*k0*cos(Phi_b)

# Amplitude coefficient polarisation s:
r_nfs = (kz_f-kz_s)/(kz_s+kz_f)
r_bns = (kz_s-kz_b)/(kz_s+kz_b)
t_nfs = 1+r_nfs
t_bns = 1+r_bns

# Amplitude coefficient polarisation p:
r_nfp = (kz_f*n_s**2-kz_s*n_f**2)/(kz_s*n_f**2+kz_f*n_s**2)
r_bnp = (kz_s*n_b**2-kz_b*n_s**2)/(kz_s*n_b**2+kz_b*n_s**2)
t_nfp = cos(Phi_i)*(1-r_nfp)/cos(Phi_s)
t_bnp = cos(Phi_s)*(1-r_bnp)/cos(Phi_b)

# Power coefficients:
R_th_ss = (abs((r_nfs+r_bns*exp(2j*kz_s*d)) \
                /(1+r_bns*r_nfs*exp(2j*kz_s*d))))**2

t2_th_ss = (abs((t_bns*t_nfs*exp(1j*kz_s*d)) \
                /(1+r_bns*r_nfs*exp(2j*kz_s*d))))**2

R_th_pp = (abs((r_nfp+r_bnp*exp(2j*kz_s*d)) \
                /(1+r_bnp*r_nfp*exp(2j*kz_s*d))))**2

t2_th_pp= (abs((t_bnp*t_nfp*exp(1j*kz_s*d)) \
                /(1+r_bnp*r_nfp*exp(2j*kz_s*d))))**2

correction = real(n_b*cos(Phi_b)/(n_f*cos(Phi_i)))
# This is a correction term used in R +T*correction = 1

T_th_ss = t2_th_ss*correction
T_th_pp = t2_th_pp*correction

############################################################################
# Calculation with Berreman4x4

Kx = front.get_Kx_from_Phi(Phi_i, k0)   # Reduced wavenumber

l = []
for d_i in d:
    layer.setThickness(d_i)
    l.append(s.getJones(Kx,k0))
data = numpy.array(l)

# Extraction of the transmission and reflexion coefficients
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

y = numpy.vstack((R_ss,R_pp,t2_ss,t2_pp,T_ss,T_pp)).T
legend1 = ("R_ss","R_pp","t2_ss","t2_pp","T_ss","T_pp")
lines1 = ax.plot(d, y)

y_th = numpy.vstack((R_th_ss,R_th_pp,t2_th_ss,t2_th_pp,T_th_ss,T_th_pp)).T
legend2 = ("R_th_ss","R_th_pp","t2_th_ss","t2_th_pp","T_th_ss","T_th_pp")
lines2 = ax.plot(d, y_th, 'x')

ax.legend(lines1 + lines2, legend1 + legend2, 
          loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

ax.set_title("FTIR: Glass1 / Air (d) / Glass2, for incidence angle " +
             "$\Phi_i$ = {:.0f}$^\circ$".format(Phi_i*180/pi))
ax.set_xlabel(r"Air layer thickness, $d$ (m)")
ax.set_ylabel(r"Reflexion and transmission coefficients $R$, $T$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))
pyplot.show()


