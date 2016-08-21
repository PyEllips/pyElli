#!/usr/bin/python
# encoding: utf-8
# Berreman4x4 example
# Author: O. Castany, C. Molinaro

# Validation for a TiO2/SiO2 Bragg mirror

import numpy, Berreman4x4
import scipy.linalg
import matplotlib.pyplot as pyplot
from Berreman4x4 import c, pi
from numpy import newaxis, exp, sin

print("\n*** TiO2/SiO2 Bragg mirror ***\n")

############################################################################
# Structure definition

# Front and back materials
n_a = 1.0
n_g = 1.5
air = Berreman4x4.IsotropicNonDispersiveMaterial(n_a)
glass = Berreman4x4.IsotropicNonDispersiveMaterial(n_g)

front = Berreman4x4.IsotropicHalfSpace(air)
back = Berreman4x4.IsotropicHalfSpace(glass)

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
L = Berreman4x4.RepeatedLayers([L_TiO2, L_SiO2], 4, 0, 0)

# Number of interfaces
N = 2 * L.n + 1

# Structure
s = Berreman4x4.Structure(front, [L], back)

############################################################################
# Analytical calculation
n = numpy.ones(N+1, dtype=complex)
n[0] = n_a
n[1::2] = n_TiO2
n[2::2] = n_SiO2
n[-1] = n_g

n.shape = (-1,1)

d = numpy.ones(N+1)
d[1::2] = L_TiO2.h  # d[0] is not used
d[2::2] = L_SiO2.h

(lbda1, lbda2) = (1.1e-6, 2.5e-6)
lbda_list = numpy.linspace(lbda1, lbda2, 200)


def ReflectionCoeff(incidence_angle=0., polarisation='s'):
    """Returns the reflection coefficient in amplitude"""
    Kx = n[0]*sin(incidence_angle)    
    sinPhi = Kx/n
    kz = 2*pi/lbda_list * numpy.sqrt(n**2-(Kx)**2)

    # Reflexion coefficient r_{k,k+1} for a single interface 
    #    polarisation s:
    #    r_ab(p) = r_{p,p+1} = (kz(p)-kz(p+1))/(kz(p)+kz(p+1))
    #    polarisation p:
    #    r_ab(p) = r_{p,p+1} = (kz(p)*n[p+1]**2-kz(p+1)*n[p]**2) \ 
    #                          /(kz(p)*n[p]**2+kz(p+1)*n[p+1]**2)
    if (polarisation == 's'):
        r_ab = (-numpy.diff(kz,axis=0)) / (kz[:-1] + kz[1:])
    elif (polarisation == 'p'):
        r_ab =(kz[:-1]*(n[1:])**2 - kz[1:]*(n[:-1])**2) \
              / (kz[:-1]*(n[1:])**2 + kz[1:]*(n[:-1])**2)
    
    # Local function definition for recursive calculation
    def U(k):
        """Returns reflection coefficient U(k) = r_{k, {k+1,...,N}}

        Used recursively.
        """
        p = k+1
        if (p == N):
            res = r_ab[N-1]
        else :
            res =   (r_ab[p-1] + U(p)*exp(2j*kz[p]*d[p]))  \
              / (1 + r_ab[p-1] * U(p)*exp(2j*kz[p]*d[p]))
        return res

    return U(0)

# Power reflexion coefficient for different incidence angles and polarisations
R_th_ss_0 = (abs(ReflectionCoeff(0, 's')))**2       # Phi_i = 0 
R_th_ss = (abs(ReflectionCoeff(pi/4, 's')))**2      # Phi_i = pi/4
R_th_pp = (abs(ReflectionCoeff(pi/4, 'p')))**2

############################################################################
# Calculation with Berreman4x4
# Incidence angle Phi_i = 0, 's' polarization
Kx = front.get_Kx_from_Phi(0)
data = Berreman4x4.DataList([s.evaluate(Kx, 2*pi/lbda) for lbda in lbda_list])
R_ss_0 = data.get('R_ss')

# Incidence angle Phi_i = pi/4, 's' and 'p' polarizations
Kx = front.get_Kx_from_Phi(pi/4)
data = Berreman4x4.DataList([s.evaluate(Kx, 2*pi/lbda) for lbda in lbda_list])
R_ss = data.get('R_ss')
R_pp = data.get('R_pp')

############################################################################
# Plotting
fig = pyplot.figure(figsize=(12., 6.))
pyplot.rcParams['axes.prop_cycle'] = pyplot.cycler('color', 'bgr')
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])

d = numpy.vstack((R_ss_0,R_ss,R_pp)).T
lines1 = ax.plot(lbda_list,d)
legend1 = ("R_ss (0$^\circ$)","R_ss (45$^\circ$)","R_pp (45$^\circ$)")

d = numpy.vstack((R_th_ss_0,R_th_ss,R_th_pp)).T
lines2 = ax.plot(lbda_list,d,'x')
legend2 = ("R_th_ss (0$^\circ$)","R_th_ss (45$^\circ$)",
           "R_th_pp (45$^\circ$)")

ax.legend(lines1 + lines2, legend1 + legend2, 
          loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

ax.set_title(r"Bragg mirror: Air/{TiO$_2$/SiO$_2$}x" + str(L.n) + "/Glass")
ax.set_xlabel(r"Wavelength $\lambda$ (m)")
ax.set_ylabel(r"$R$")
fmt = ax.xaxis.get_major_formatter()
fmt.set_powerlimits((-3,3))

s.drawStructure()
pyplot.show()

