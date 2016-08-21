#!/usr/bin/python3
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# Verification of the code against results presented in Fujiwara's book 
# p. 241 (section 6.4.2). References in the comments refer to this book.
# Expected results are indicated after the commands. They are identical 
# with Fujiwara's results, except for a sign convention for Erp.

import numpy, Berreman4x4
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot
import scipy.linalg

print("\nWe reproduce results from section 6.4.2 in " +       
      "'Spectroscopic Ellipsometry',\nby H. Fujiwara.")

# reduces the number of printed figures in numbers:
numpy.set_printoptions(suppress=True, precision=4)

n_i = 1.0       # incident medium is air
n_o = 2.0       # ordinary index of thin layer
n_e = 2.5       # extraordinary index of thin layer
w = 3.04e15	# pulsation (rad/s)
Phi_i = 70*pi/180   # 70° indicence angle (rad)
d = 0.1e-6      # thin layer thickness (m)
# Orientation of the anisotropy of the thin layer
Phi_E = pi/4    # 1st Euler angle
Theta_E = pi/4  # 2nd Eulet angle

print("\n*** Air / anisotropic film / silicon substrate ***")

filmMaterialRef = Berreman4x4.UniaxialNonDispersiveMaterial(n_o,n_e)
R = Berreman4x4.rotation_Euler((Phi_E, Theta_E, 0))
filmMaterial = filmMaterialRef.rotated(R)
print("\nPermittivity tensor of the anisotropic film (eq 6.63, p. 241):")
print(filmMaterial.getTensor())
"""
matrix([[ 4.5625, -0.5625,  0.7955],
        [-0.5625,  4.5625, -0.7955],
        [ 0.7955, -0.7955,  5.125 ]])
"""

air = Berreman4x4.IsotropicNonDispersiveMaterial(n_i)
front = Berreman4x4.IsotropicHalfSpace(air)     # Front half-space
Kx = front.get_Kx_from_Phi(Phi_i)
print("\nValue of Kx: {:.4f}".format(Kx))
"""
Kx = 0.9397
"""

film = Berreman4x4.HomogeneousLayer(filmMaterial, d)
Delta = film.getDeltaMatrix(Kx)
print("\nDelta matrix:")
print(Delta)
"""
matrix([[-0.1459,  0.1459,  0.    ,  0.8277],
        [ 0.    ,  0.    , -1.    ,  0.    ],
        [ 0.439 , -3.556 ,  0.    , -0.1459],
        [ 4.439 , -0.439 ,  0.    , -0.1459]])
"""
q,Psi = scipy.linalg.eig(Delta)
print("\nEigenvalues of the Delta matrix (eq 6.64, p.241):")
print(numpy.real(q))
"""                                                                 (eq 6.64)
real(q) = array([-2.174 , -1.7655,  1.7655,  1.8822])
imag(q) = array([ 0.,  0.,  0.,  0.])
"""

k0 = w / c
Tp = film.getPropagationMatrix(Kx, k0, inv=True)
print("\nPropagation matrix (eq 6.66, p. 242):")
numpy.set_printoptions(suppress=True, precision=3)
print(Tp)
"""                                                                 (eq 6.66)
Tp =
matrix([[-0.353-0.057j,  0.091-0.001j,  0.033+0.044j,  0.056-0.397j],
        [ 0.104+0.08j , -0.327-0.011j,  0.004+0.502j, -0.033-0.044j],
        [ 0.162-0.014j, -0.017+1.753j, -0.327-0.011j, -0.091+0.001j],
        [ 0.300-2.12j , -0.162+0.014j, -0.104-0.08j , -0.353-0.057j]])
"""

n_t = 3.898 + 0.016j    # refractive index of substrate
silicon = Berreman4x4.IsotropicNonDispersiveMaterial(n_t)
back = Berreman4x4.IsotropicHalfSpace(silicon)
numpy.set_printoptions(suppress=True, precision=4)
print("\nValue of cos(Φt): " + str(numpy.cos(back.get_Phi_from_Kx(Kx))))
print("Value of cos(Φi): " + str(numpy.cos(front.get_Phi_from_Kx(Kx))))
"""
cos(back.get_Phi_from_Kx(Kx)) = 
(0.97050916278673638+0.00024578299783964012j)
cos(front.get_Phi_from_Kx(Kx)) =
0.34202014332566882
"""

s = Berreman4x4.Structure(front, [film], back)
T = s.getStructureMatrix(Kx,k0)
print("\nTransfer matrix T (eq 6.67, p. 242):")
print(T)
"""                                                                 (eq 6.67)
Fujiwara uses the ellipsometry convention for the orientation of the 'p' 
polarized electric fields (see figures 2.15 and 6.14). With my convention, 
Erp is reversed. Consequently, T_{4j} and T_{i4} have a reversed sign, except
T_{44}.
T = 
matrix([[-1.949-3.588j,  1.671-1.548j,  0.273-0.03j , -0.630+0.147j],
        [ 1.617+1.679j, -1.992+3.434j, -0.301-0.064j,  0.861+0.101j],
        [ 0.065-0.086j,  0.039+0.097j, -0.712-3.485j,  0.004+1.265j],
        [-0.167-0.403j,  0.593+0.386j,  0.370-1.199j, -1.662+3.093j]])
"""
Jr = s.getJones(Kx,k0)[0]   # Jones reflexion matrix
print("\nJones reflexion matrix (p. 243):")
print(Jr)
"""
Jr =
matrix([[ 0.310+0.161j,  0.107+0.002j],
        [ 0.042-0.036j, -0.552+0.151j]])
The first line, [r_pp, r_ps], has reversed sign compared to Fujiwara's result, 
due to the different convention for Erp.
"""
print("\nEllipsometry parameters (p. 243):")
(Psi,Delta) = Berreman4x4.DataList.getEllipsometryParameters(Jr)
print("Psi\n" + str(Psi))
print("Delta\n" + str(Delta))
"""
Ellipsometry parameters: 
Psi                         Delta
[[ 31.4419  10.5641]         [[ -42.734   -16.4123]
 [  5.5332  45.    ]]         [-155.024     0.    ]]
"""

# We now reproduce figure 6.19:
print("\nWe reproduce figure 6.19, p. 242...")

Theta_E_list = [0, pi/4, pi/2]
Phi_E_list = numpy.linspace(0,pi,36*2+1)
Phi_E_deg = Phi_E_list*180/pi

data = Berreman4x4.DataList()
for Theta_E in Theta_E_list:
    l = []
    for Phi_E in Phi_E_list:
        R = Berreman4x4.rotation_Euler((Phi_E, Theta_E, 0))
        film.setMaterial(filmMaterialRef.rotated(R))
        l.append(s.evaluate(Kx,k0))
    data.append(l)

fig = pyplot.figure()
# Plot curves for the three values of Theta_E
pyplot.rcParams['axes.prop_cycle'] = pyplot.cycler('color', 'kbg')
ax1 = fig.add_subplot("221")
Psi_pp = data.get('Ψ_pp')
ax1.plot(Phi_E_deg, Psi_pp.T)
ax1.set_ylabel(r"$\Psi_{pp}$")

ax2 = fig.add_subplot("222")
Delta_pp = data.get('Δ_pp')
ax2.plot(Phi_E_deg, Delta_pp.T)
ax2.set_ylabel(r"$\Delta_{pp}$")

# Plot curves for two values of Theta_E
pyplot.rcParams['axes.prop_cycle'] = pyplot.cycler('color', 'bg')
ax3 = fig.add_subplot("223")
Psi_ps = data.get('Ψ_ps')
ax3.plot(Phi_E_deg, Psi_ps.T)
ax3.set_ylabel(r"$\Psi_{ps}$")
ax3.set_xlabel(r"$\phi_E$")

ax4 = fig.add_subplot("224")
Delta_ps = data.get('Δ_ps')
ax4.plot(Phi_E_deg, Delta_ps.T)
ax4.set_ylabel(r"$\Delta_{ps}$")
ax4.set_xlabel(r"$\phi_E$")

pyplot.tight_layout()
pyplot.show()


