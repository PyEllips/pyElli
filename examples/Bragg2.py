#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# Example of an SiO2/TiO2 Bragg mirror

import numpy, Berreman4x4
import scipy.linalg
import matplotlib.pyplot as pyplot
from Berreman4x4 import c, pi

print("\n*** SiO2/TiO2 Bragg mirror ***\n")


# Front and back materials
n_g = 1.5
glass = Berreman4x4.IsotropicNonDispersiveMaterial(n_g)
front = back = Berreman4x4.IsotropicHalfSpace(glass)

# Materials for a SiO2/TiO2 Bragg mirror
lbda0 = 1.550e-6
k0 = 2*pi/lbda0
nr_SiO2 = 1.47
nr_TiO2 = 2.23
alpha_SiO2 = 0e2    # (m⁻¹)
alpha_TiO2 = 42e2   # (m⁻¹)
ni_SiO2 = alpha_SiO2 * lbda0 / (4*pi)
ni_TiO2 = alpha_TiO2 * lbda0 / (4*pi)
n_SiO2 = nr_SiO2 + 1j * ni_SiO2
n_TiO2 = nr_TiO2 + 1j * ni_TiO2

SiO2 = Berreman4x4.IsotropicNonDispersiveMaterial(n_SiO2)
TiO2 = Berreman4x4.IsotropicNonDispersiveMaterial(n_TiO2)

# Layers

L_SiO2 = Berreman4x4.HomogeneousIsotropicLayer(SiO2, ("QWP", lbda0))
L_TiO2 = Berreman4x4.HomogeneousIsotropicLayer(TiO2, ("QWP", lbda0))

print("Thickness of the SiO2 QWP: {:.1f} nm".format(L_SiO2.h*1e9))
print("Thickness of the TiO2 QWP: {:.1f} nm".format(L_TiO2.h*1e9))

# Repeated layers: n periods
L = Berreman4x4.RepeatedLayers([L_TiO2, L_SiO2], 4,0,0)

#Theory polarisation s
n = numpy.complex128(numpy.ones(2*L.n+2))
n[::2] = n_SiO2
n[1::2] = n_TiO2
n[0] = n[-1] = n_g

d = numpy.ones(2*L.n+2)
d[::2] = L_SiO2.h
d[1::2] = L_TiO2.h

def sinPhi(p):
    res = numpy.sin(Phi_0)*n[0]/n[p]
    return res

def kz(p):
    res = 2*numpy.pi/lbda_list*numpy.sqrt(n[p]**2-(n[p]*sinPhi(p))**2)
    return res

def r_int(p):
    res = (kz(p)-kz(p+1))/(kz(p)+kz(p+1))#(-numpy.diff(kz(p)))/(kz(p)[:-1]+kz(p)[1:])
    return res

def U(k):
    p = k+1
    if (p == 2*L.n + 1):
        res = r_int(2*L.n)
    else :
        res = (r_int(p-1)+U(p)*numpy.exp(2j*kz(p)*d[p]))/(1+r_int(p-1)*U(p)*numpy.exp(2j*kz(p)*d[p]))
    return res

# Structure
s = Berreman4x4.Structure(front, [L], back)

# Power coefficient reflexion

(lbda1, lbda2) = (1.1e-6, 2.5e-6)
lbda_list = numpy.linspace(lbda1, lbda2, 200)
#Phi_0 = 0
Phi_0 = 0
Kx = n[0]*numpy.sin(Phi_0)
data = [s.getJones(Kx,2*pi/lbda) for lbda in lbda_list]
data = numpy.array(data)
r = Berreman4x4.extractCoefficient(data, 'r_ss')
R_ss_0 = numpy.abs(r)**2
R_th_ss_0 = (numpy.abs(U(0)))**2

#Phi_0 = pi/4
Phi_0 = numpy.pi/4
Kx = n[0]*numpy.sin(Phi_0)
data = [s.getJones(Kx,2*pi/lbda) for lbda in lbda_list]
data = numpy.array(data)
r = Berreman4x4.extractCoefficient(data, 'r_ss')
R_ss = numpy.abs(r)**2
R_th_ss = (numpy.abs(U(0)))**2

# Graphics
fig = pyplot.figure()
ax = fig.add_subplot("111")
lines = ax.plot(lbda_list, R_ss_0, lbda_list, R_ss,
lbda_list, R_th_ss_0, 'bo',lbda_list, R_th_ss, 'go')
ax.legend(lines, ("R_ss_0","R_ss","R_th_ss_0","R_th_ss"))
ax.xaxis.major.formatter.set_powerlimits((-3,3))
ax.set_xlabel(r"Wavelength $\lambda$ (m)")
ax.set_ylabel(r"$R$, $T$")
ax.set_title(r"SiO$_2$/TiO$_2$ Bragg mirror ("+str(L.n)+" periods)")
pyplot.show()

