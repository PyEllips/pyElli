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
back =  Berreman4x4.IsotropicHalfSpace(glass2)

# Structure:
s = Berreman4x4.Structure(front, [layer], back)

# Wavelength and wavenumber:
lbda = 1e-6
k0 = 2*pi/lbda

####################################################################
# Variation of transmitted power with air thickness

Phi_i = pi/2 * 0.6   # Incidence angle higher than the limit angle
Kx = front.get_Kx_from_Phi(Phi_i, k0)

# Calculation with Berreman4x4
h_list = numpy.linspace(0, 1.0e-6)
l = []
for h in h_list:
    layer.setThickness(h)
    l.append(s.getJones(Kx,k0))
data = numpy.array(l)

# Extraction of the transmission and reflexion coefficients
data = (numpy.abs(data))**2
R_pp  = Berreman4x4.extractCoefficient(data, 'r_pp')
R_ss  = Berreman4x4.extractCoefficient(data, 'r_ss')
t2_pp = Berreman4x4.extractCoefficient(data, 't_pp')
t2_ss = Berreman4x4.extractCoefficient(data, 't_ss')
#T_ss = t2_ss*correction
#T_pp = t2_pp*correction



Phi_b = numpy.arcsin((Kx)/n_b)
Phi_n = numpy.arcsin((complex(Kx/n)))

#### Theory
# Wave vector:
k_f = n_f*k0*numpy.cos(Phi_i)
k_n = k0*numpy.sqrt(complex(((Kx)**2 - n**2)))
k_b = n_b*k0*numpy.cos(Phi_b)

#Amplitude coefficient polarisation s:
r_nf = (k_f-k_n)/(k_n+k_f)
r_bn = (k_n-k_b)/(k_n+k_b)
t_nf = 1+r_nf
t_bn = 1+r_bn

#Amplitude coefficient polarisation p:

ep_f = n_f**2
ep_n = n**2
ep_b = n_b**2
r_nfp = (ep_n*k_f-ep_f*k_n)/(ep_f*k_n+ep_n*k_f)
r_bnp = (ep_b*k_n-ep_n*k_b)/(ep_b*k_n+ep_n*k_b)
t_nfp = numpy.cos(Phi_i)*(1-r_nfp)/numpy.cos(Phi_n)
t_bnp = numpy.cos(Phi_n)*(1-r_bnp)/numpy.cos(Phi_b)



# Theoritical power coefficients:

R_th_ss = (numpy.abs((r_nf+r_bn*numpy.exp(2j*k_n*h_list))/(1+r_bn*r_nf*numpy.exp(2j*k_n*h_list))))**2

#t2_th_ss = (numpy.abs((t_bn*t_nf*numpy.exp(1j*k_n*h_list))/(1+r_bn*r_nf*numpy.exp(2j*k_n*h_list))))**2

R_th_pp = (numpy.abs((r_nfp+r_bnp*numpy.exp(2j*k_n*h_list))/(1+r_bnp*r_nfp*numpy.exp(2j*k_n*h_list))))**2

#t2_th_pp= (numpy.abs((t_bnp*t_nfp*numpy.exp(1j*k_n*h_list))/(1+r_bnp*r_nfp*numpy.exp(2j*k_n*h_list))))**2

#correction = numpy.real(n_b*numpy.cos(Phi_b)/(n_f*numpy.cos(Phi_i)))# This is a correction term used in R +T*correction = 1

#T_th_ss = t2_th_ss*correction
#T_th_pp = t2_th_pp*correction

############################################################################
# Plotting

fig = pyplot.figure(figsize=(12., 6.))
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])

d = numpy.vstack((R_ss,R_pp)).T#,t2_ss,t2_pp,T_ss,T_pp)).T
lines = ax.plot(h_list,d, h_list,R_th_ss,'b'+'o',h_list,R_th_pp,'g'+'o')#, h_list,t2_th_ss, 'r'+'o',h_list,t2_th_pp,'c'+'o', h_list,T_th_ss,'m'+'o',h_list,T_th_pp,'y'+'o')
ax.legend(lines, ("R_ss","R_pp","t2_ss","t2_pp","T_ss","T_pp","R_th_ss","R_th_pp","t2_th_ss","t2_th_pp","T_th_ss","T_th_pp"),bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.set_title("Frustrated Total Internal Reflexion: Glass1 / Air / Glass2")
ax.set_xlabel(r"Air layer thickness, $h$ (m)")
ax.set_ylabel(r"Reflexion and transmission coefficients $R$, $T$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))
pyplot.show()


