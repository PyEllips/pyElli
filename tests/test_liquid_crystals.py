#!/usr/bin/python
# encoding: utf-8

import elli
import numpy as np
from numpy.lib.scimath import sqrt
from scipy.constants import pi
from scipy.signal import argrelmax, argrelmin


def test_cholesteric_lc():
    # Materials
    front = back = elli.IsotropicMaterial(elli.DispersionLess(1.6))

    # Liquid crystal oriented along the x direction
    (no, ne) = (1.5, 1.7)
    Dn = ne-no
    n_med = (ne + no)/2
    LC = elli.UniaxialMaterial(elli.DispersionLess(no), elli.DispersionLess(ne))  # ne along z
    R = elli.rotation_v_theta(elli.e_y, 90)  # rotation round y
    LC.set_rotation(R)  # apply rotation from z to x
    # Cholesteric pitch:
    p = 650
    # One half turn of a right-handed helix:
    TN = elli.TwistedLayer(LC, p/2, 25, 180)

    # Inhomogeneous layer, repeated layer, and structure
    N = 5  # number half pitch repetitions
    h = N * p/2
    L = elli.RepeatedLayers([TN], N)
    s = elli.Structure(front, [L], back)

    # Normal incidence:
    Kx = 0.0

    # Calculation parameters
    lbda_min, lbda_max = 600, 1500  # (nm)
    lbda = np.linspace(lbda_min, lbda_max, 100)
    k0 = 2*pi/(lbda*1e-9)

    # Theoretical calculation
    q = 2*pi/p/1e-9
    alpha = q/k0
    epsilon = (no**2+ne**2)/2
    delta = (no**2-ne**2)/2
    n2 = sqrt((alpha**2 + epsilon - sqrt(4*epsilon*alpha**2+delta**2)))
    w = 1j*(ne**2-n2**2-alpha**2)/(2*alpha*n2)  # not k0/c
    A = -2j*k0*n2*h*1e-9

    R_th = np.abs((w**2+1)*(1-np.exp(-2j*k0*n2*h*1e-9))
                  / (2*w*(1+np.exp(-2j*k0*n2*h*1e-9))
                     - 1j*(w**2-1)*(1-np.exp(-2j*k0*n2*h*1e-9))))**2

    # Berreman simulation
    data = s.evaluate(lbda, 0)
    R_RR = data.Rc[:, 1, 1]

    # Checks positions of local extrema
    np.testing.assert_allclose(argrelmax(R_RR)[0], argrelmax(R_th)[0], atol=3)
    np.testing.assert_allclose(argrelmin(R_RR)[0], argrelmin(R_th)[0])


def test_twisted_nematic_lc():
    # Materials
    glass = elli.IsotropicMaterial(elli.DispersionLess(1.55))
    front = back = glass

    # Liquid crystal oriented along the x direction
    (no, ne) = (1.5, 1.6)
    Dn = ne-no
    LC = elli.UniaxialMaterial(elli.DispersionLess(no),
                             elli.DispersionLess(ne))
    R = elli.rotation_v_theta(elli.e_y, 90)
    LC.set_rotation(R)
    d = 4330
    TN = elli.TwistedLayer(LC, d, 18, 90)

    # Structure
    s = elli.Structure(front, [TN], back)

    # Calculation parameters
    (lbda_min, lbda_max) = (200e-9, 1)  # (m)
    k0_list = np.linspace(2*pi/lbda_max, 2*pi/lbda_min)
    lbda_list = (2*pi)/k0_list*1e9

    # Gooch-Tarry law
    u = 2*d*Dn/lbda_list
    T_gt = np.sin(pi/2*sqrt(1+u**2))**2 / (1+u**2)

    # Berreman simulation
    data = s.evaluate(lbda_list, 0)
    T_bm = np.real(data.T[:, 0, 0])

    # Compare results
    np.testing.assert_array_almost_equal(T_bm, T_gt, decimal=2)
