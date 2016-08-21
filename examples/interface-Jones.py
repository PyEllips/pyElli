#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# Simple example: reflection on an air/glass interface, at normal indicence.

print("*** Air / glass interface ***\n")

import numpy, Berreman4x4
from Berreman4x4 import c, pi 

# Materials:
air = Berreman4x4.IsotropicNonDispersiveMaterial(1.0)
glass = Berreman4x4.IsotropicNonDispersiveMaterial(1.5)

# Half-spaces:
front = Berreman4x4.IsotropicHalfSpace(air)
back = Berreman4x4.IsotropicHalfSpace(glass)

# Structure:
s = Berreman4x4.Structure(front, [], back)

# Incidence angle (Kx = n sin(Φ):
Kx = 0.0

print("When the basis is the linear polarizations ('p','s')...")
J = s.getJones(Kx, k0=1e6)
(Jr, Jt) = J
print("Jones matrix for reflection (Jr):")
print(Jr)
print("Jones matrix for transmission (Jt):")
print(Jt)
"""
(matrix([[-0.2,  0. ],     matrix([[ 0.8,  0. ],
        [ 0. , -0.2]]),           [ 0. ,  0.8]]))
"""

print("\nWhen the basis is the circular polarizations ('L','R')...")
print("Jones matrix for reflection (Jcr):")
Jcr = Berreman4x4.DataList.getCircularJones(Jr, "reflection")
print(Jcr)
print("Jones matrix for transmission (Jct):")
Jct = Berreman4x4.DataList.getCircularJones(Jt, "transmission")
print(Jct)
"""
array([[ 0.0+0.j, -0.2+0.j],      array([[ 0.8+0.j,  0.0+0.j],
       [-0.2+0.j,  0.0+0.j]])            [ 0.0+0.j,  0.8+0.j]])
"""
print(
"""
In a reflexion, the handedness of an elliptic polarization is reversed, 
so the matrix 'Jcr' is anti-diagonal.
""")

s.drawStructure()
Berreman4x4.matplotlib.pyplot.show()        # show drawing


