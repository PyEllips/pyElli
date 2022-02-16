#!/usr/bin/python
# encoding: utf-8

import numpy as np
import elli
from scipy.constants import pi


class TestBragg:

    n_a = 1.0
    n_g = 1.5
    air = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_a))
    glass = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_g))

    lbda0 = 1550  # nm
    k0 = 2 * pi / lbda0
    n_SiO2 = 1.47
    n_TiO2 = 2.23 + 1j * 5.2e-4

    SiO2 = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_SiO2))
    TiO2 = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_TiO2))

    # Layers and Structure
    d_SiO2 = elli.get_qwp_thickness(SiO2, lbda0)
    d_TiO2 = elli.get_qwp_thickness(TiO2, lbda0)

    L_SiO2 = elli.Layer(SiO2, d_SiO2)
    L_TiO2 = elli.Layer(TiO2, d_TiO2)

    # Repeated layers: n periods
    Layerstack = elli.RepeatedLayers([L_TiO2, L_SiO2], 4, 0, 0)

    # Number of interfaces
    N = 2 * Layerstack.repetitions + 1

    # Structure
    s = elli.Structure(air, [Layerstack], glass)

    # Analytical calculation
    n = np.ones(N + 1, dtype=complex)
    n[0] = n_a
    n[1::2] = n_TiO2
    n[2::2] = n_SiO2
    n[-1] = n_g

    n.shape = (-1, 1)

    d = np.ones(N + 1)
    d[1::2] = L_TiO2.d  #  d[0] is not used
    d[2::2] = L_SiO2.d

    (lbda1, lbda2) = (1100, 2500)
    lbda_list = np.linspace(lbda1, lbda2, 200)

    def ReflectionCoeff(self, incidence_angle=0.0, polarisation="s"):
        """Returns the reflection coefficient in amplitude"""
        Kx = self.n[0] * np.sin(incidence_angle)
        sinPhi = Kx / self.n
        kz = 2 * pi / self.lbda_list * np.sqrt(self.n ** 2 - Kx ** 2)

        # Reflexion coefficient r_{k,k+1} for a single interface
        #    polarisation s:
        #    r_ab(p) = r_{p,p+1} = (kz(p)-kz(p+1))/(kz(p)+kz(p+1))
        #    polarisation p:
        #    r_ab(p) = r_{p,p+1} = (kz(p)*n[p+1]**2-kz(p+1)*n[p]**2) \
        #                          /(kz(p)*n[p]**2+kz(p+1)*n[p+1]**2)
        if polarisation == "s":
            r_ab = (-np.diff(kz, axis=0)) / (kz[:-1] + kz[1:])
        elif polarisation == "p":
            r_ab = (kz[:-1] * (self.n[1:]) ** 2 - kz[1:] * (self.n[:-1]) ** 2) / (
                kz[:-1] * (self.n[1:]) ** 2 + kz[1:] * (self.n[:-1]) ** 2
            )

        # Local function definition for recursive calculation
        def U(k):
            """Returns reflection coefficient U(k) = r_{k, {k+1,...,N}}

            Used recursively.
            """
            p = k + 1
            if p == self.N:
                res = r_ab[self.N - 1]
            else:
                res = (r_ab[p - 1] + U(p) * np.exp(2j * kz[p] * self.d[p])) / (
                    1 + r_ab[p - 1] * U(p) * np.exp(2j * kz[p] * self.d[p])
                )
            return res

        return U(0)

    def test_normal_incidence(self):
        data = self.s.evaluate(self.lbda_list, 0)
        R_ss_0 = data.R_ss
        R_th_ss_0 = (np.abs(self.ReflectionCoeff(0, "s"))) ** 2  # Phi_i = 0
        np.testing.assert_allclose(R_ss_0, R_th_ss_0, 1e-10, 0)

    def test_angle(self):
        R_th_ss = (np.abs(self.ReflectionCoeff(pi / 4, "s"))) ** 2  # Phi_i = pi/4
        R_th_pp = (np.abs(self.ReflectionCoeff(pi / 4, "p"))) ** 2

        # Incidence angle Phi_i = 0, 's' polarization

        # Incidence angle Phi_i = pi/4, 's' and 'p' polarizations
        data2 = self.s.evaluate(self.lbda_list, np.rad2deg(pi / 4))

        R_ss = data2.R_ss
        R_pp = data2.R_pp

        np.testing.assert_array_almost_equal(R_ss, R_th_ss, decimal=1)
        np.testing.assert_array_almost_equal(R_pp, R_th_pp, decimal=1)

    def test_normal_incidence_4x4_scipy(self):
        data = self.s.evaluate(self.lbda_list, 0)
        R_ss_0 = data.R_ss
        R_th_ss_0 = (np.abs(self.ReflectionCoeff(0, "s"))) ** 2  # Phi_i = 0
        np.testing.assert_allclose(R_ss_0, R_th_ss_0, 1e-10, 0)

    def test_angle_4x4_scipy(self):
        R_th_ss = (np.abs(self.ReflectionCoeff(pi / 4, "s"))) ** 2  # Phi_i = pi/4
        R_th_pp = (np.abs(self.ReflectionCoeff(pi / 4, "p"))) ** 2

        # Incidence angle Phi_i = 0, 's' polarization

        # Incidence angle Phi_i = pi/4, 's' and 'p' polarizations
        data2 = self.s.evaluate(self.lbda_list, np.rad2deg(pi / 4))

        R_ss = data2.R_ss
        R_pp = data2.R_pp

        np.testing.assert_array_almost_equal(R_ss, R_th_ss, decimal=1)
        np.testing.assert_array_almost_equal(R_pp, R_th_pp, decimal=1)

    def test_normal_incidence_4x4_eig(self):
        data = self.s.evaluate(
            self.lbda_list, 0, solver=elli.Solver4x4, propagator=elli.PropagatorEig()
        )
        R_ss_0 = data.R_ss
        R_th_ss_0 = (np.abs(self.ReflectionCoeff(0, "s"))) ** 2  # Phi_i = 0
        np.testing.assert_allclose(R_ss_0, R_th_ss_0, 1e-10, 0)

    def test_angle_4x4_eig(self):
        R_th_ss = (np.abs(self.ReflectionCoeff(pi / 4, "s"))) ** 2  # Phi_i = pi/4
        R_th_pp = (np.abs(self.ReflectionCoeff(pi / 4, "p"))) ** 2

        # Incidence angle Phi_i = 0, 's' polarization

        # Incidence angle Phi_i = pi/4, 's' and 'p' polarizations
        data2 = self.s.evaluate(
            self.lbda_list,
            np.rad2deg(pi / 4),
            solver=elli.Solver4x4,
            propagator=elli.PropagatorEig(),
        )

        R_ss = data2.R_ss
        R_pp = data2.R_pp

        np.testing.assert_array_almost_equal(R_ss, R_th_ss, decimal=1)
        np.testing.assert_array_almost_equal(R_pp, R_th_pp, decimal=1)

    def test_normal_incidence_4x4_torch(self):
        data = self.s.evaluate(
            self.lbda_list,
            0,
            solver=elli.Solver4x4,
            propagator=elli.PropagatorExpmTorch(),
        )
        R_ss_0 = data.R_ss
        R_th_ss_0 = (np.abs(self.ReflectionCoeff(0, "s"))) ** 2  # Phi_i = 0
        np.testing.assert_allclose(R_ss_0, R_th_ss_0, 1e-10, 0)

    def test_angle_4x4_torch(self):
        R_th_ss = (np.abs(self.ReflectionCoeff(pi / 4, "s"))) ** 2  # Phi_i = pi/4
        R_th_pp = (np.abs(self.ReflectionCoeff(pi / 4, "p"))) ** 2

        # Incidence angle Phi_i = 0, 's' polarization

        # Incidence angle Phi_i = pi/4, 's' and 'p' polarizations
        data2 = self.s.evaluate(
            self.lbda_list,
            np.rad2deg(pi / 4),
            solver=elli.Solver4x4,
            propagator=elli.PropagatorExpmTorch(),
        )

        R_ss = data2.R_ss
        R_pp = data2.R_pp

        np.testing.assert_array_almost_equal(R_ss, R_th_ss, decimal=1)
        np.testing.assert_array_almost_equal(R_pp, R_th_pp, decimal=1)

    def test_normal_incidence_2x2(self):
        data = self.s.evaluate(self.lbda_list, 0, solver=elli.Solver2x2)
        R_ss_0 = data.R_ss
        R_th_ss_0 = (np.abs(self.ReflectionCoeff(0, "s"))) ** 2  # Phi_i = 0
        np.testing.assert_allclose(R_ss_0, R_th_ss_0, 1e-10, 0)

    def test_angle_2x2(self):
        R_th_ss = (np.abs(self.ReflectionCoeff(pi / 4, "s"))) ** 2  # Phi_i = pi/4
        R_th_pp = (np.abs(self.ReflectionCoeff(pi / 4, "p"))) ** 2

        # Incidence angle Phi_i = 0, 's' polarization

        # Incidence angle Phi_i = pi/4, 's' and 'p' polarizations
        data2 = self.s.evaluate(
            self.lbda_list, np.rad2deg(pi / 4), solver=elli.Solver2x2
        )

        R_ss = data2.R_ss
        R_pp = data2.R_pp

        np.testing.assert_array_almost_equal(R_ss, R_th_ss, decimal=1)
        np.testing.assert_array_almost_equal(R_pp, R_th_pp, decimal=1)
