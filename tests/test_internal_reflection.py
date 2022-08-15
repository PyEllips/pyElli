#!/usr/bin/python
# encoding: utf-8

import elli
import numpy as np
from scipy.constants import pi


class TestTirThickness:
    # Refractive indices
    n_f = 1.5
    n_s = 1.0
    n_b = 1.7

    # Materials:
    glass1 = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_f))
    air = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_s))
    glass2 = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_b))

    # Air layer thickness variation range
    d = np.linspace(0, 1000)

    # Structure:
    structures = []

    for dd in d:
        layer = elli.Layer(air, dd)
        structures.append(elli.Structure(glass1, [layer], glass2))

    # Wavelength and wavenumber:
    lbda = 1000
    k0 = 2 * pi / lbda
    Phi_i = pi / 2 * 0.6  #  Incidence angle (higher than the limit angle)

    # Analytical calculation

    # Reduced wavenumber
    Kx = n_f * np.sin(Phi_i)

    # Incidence angle
    Phi_s = np.arcsin((complex(Kx / n_s)))
    Phi_b = np.arcsin(Kx / n_b)

    # Wave vector:
    kz_f = n_f * k0 * np.cos(Phi_i)
    kz_s = k0 * np.sqrt(complex(n_s**2 - Kx**2))
    kz_b = n_b * k0 * np.cos(Phi_b)

    # Amplitude coefficient polarisation s:
    r_sf_s = (kz_f - kz_s) / (kz_s + kz_f)
    r_bs_s = (kz_s - kz_b) / (kz_s + kz_b)
    t_sf_s = 1 + r_sf_s
    t_bs_s = 1 + r_bs_s

    # Amplitude coefficient polarisation p:
    r_sf_p = (kz_f * n_s**2 - kz_s * n_f**2) / (kz_s * n_f**2 + kz_f * n_s**2)
    r_bs_p = (kz_s * n_b**2 - kz_b * n_s**2) / (kz_s * n_b**2 + kz_b * n_s**2)
    t_sf_p = np.cos(Phi_i) * (1 - r_sf_p) / np.cos(Phi_s)
    t_bs_p = np.cos(Phi_s) * (1 - r_bs_p) / np.cos(Phi_b)

    # Power coefficients:
    R_th_s = (
        np.abs(
            (r_sf_s + r_bs_s * np.exp(2j * kz_s * d))
            / (1 + r_bs_s * r_sf_s * np.exp(2j * kz_s * d))
        )
    ) ** 2

    t2_th_s = (
        np.abs(
            (t_bs_s * t_sf_s * np.exp(1j * kz_s * d))
            / (1 + r_bs_s * r_sf_s * np.exp(2j * kz_s * d))
        )
    ) ** 2

    R_th_p = (
        np.abs(
            (r_sf_p + r_bs_p * np.exp(2j * kz_s * d))
            / (1 + r_bs_p * r_sf_p * np.exp(2j * kz_s * d))
        )
    ) ** 2

    t2_th_p = (
        np.abs(
            (t_bs_p * t_sf_p * np.exp(1j * kz_s * d))
            / (1 + r_bs_p * r_sf_p * np.exp(2j * kz_s * d))
        )
    ) ** 2

    correction = np.real(n_b * np.cos(Phi_b) / (n_f * np.cos(Phi_i)))
    # This is a correction term used in R +T*correction = 1

    T_th_s = t2_th_s * correction
    T_th_p = t2_th_p * correction

    def test_tir_thickness_4x4_expm(self):
        data = elli.ResultList(
            [s.evaluate(self.lbda, np.rad2deg(self.Phi_i)) for s in self.structures]
        )

        # Extraction of the transmission and reflexion coefficients
        R_p = data.R_pp
        R_s = data.R_ss
        T_p = data.T_pp
        T_s = data.T_ss
        t2_p = np.abs(data.t_pp) ** 2  # Before power correction
        t2_s = np.abs(data.t_ss) ** 2

        np.testing.assert_allclose(R_p, self.R_th_p)
        np.testing.assert_allclose(R_s, self.R_th_s)
        np.testing.assert_allclose(T_p, self.T_th_p)
        np.testing.assert_allclose(T_s, self.T_th_s)
        np.testing.assert_allclose(t2_p, self.t2_th_p)
        np.testing.assert_allclose(t2_s, self.t2_th_s)

    def test_tir_thickness_4x4_eig(self):
        data = elli.ResultList(
            [
                s.evaluate(
                    self.lbda,
                    np.rad2deg(self.Phi_i),
                    solver=elli.Solver4x4,
                    propagator=elli.PropagatorEig(),
                )
                for s in self.structures
            ]
        )

        # Extraction of the transmission and reflexion coefficients
        R_p = data.R_pp
        R_s = data.R_ss
        T_p = data.T_pp
        T_s = data.T_ss
        t2_p = np.abs(data.t_pp) ** 2  # Before power correction
        t2_s = np.abs(data.t_ss) ** 2

        np.testing.assert_allclose(R_p, self.R_th_p)
        np.testing.assert_allclose(R_s, self.R_th_s)
        np.testing.assert_allclose(T_p, self.T_th_p)
        np.testing.assert_allclose(T_s, self.T_th_s)
        np.testing.assert_allclose(t2_p, self.t2_th_p)
        np.testing.assert_allclose(t2_s, self.t2_th_s)

    def test_tir_thickness_2x2(self):
        data = elli.ResultList(
            [
                s.evaluate(self.lbda, np.rad2deg(self.Phi_i), solver=elli.Solver2x2)
                for s in self.structures
            ]
        )

        # Extraction of the transmission and reflexion coefficients
        R_p = data.R_pp
        R_s = data.R_ss
        T_p = data.T_pp
        T_s = data.T_ss
        t2_p = np.abs(data.t_pp) ** 2  # Before power correction
        t2_s = np.abs(data.t_ss) ** 2

        np.testing.assert_allclose(R_p, self.R_th_p)
        np.testing.assert_allclose(R_s, self.R_th_s)
        np.testing.assert_allclose(T_p, self.T_th_p)
        np.testing.assert_allclose(T_s, self.T_th_s)
        np.testing.assert_allclose(t2_p, self.t2_th_p)
        np.testing.assert_allclose(t2_s, self.t2_th_s)


class TestTirAngle:
    n_f = 1.5
    n_s = 1.0
    n_b = 1.7

    # Materials:
    glass1 = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_f))
    air = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_s))
    glass2 = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_b))

    # Layer:
    layer = elli.Layer(air, 0)

    # Structure:
    s = elli.Structure(glass1, [layer], glass2)

    # Wavelength and wavenumber:
    lbda = 1000
    k0 = 2 * pi / lbda

    # Layer thickness
    d = lbda * 0.347
    layer.set_thickness(d)

    # Variation of incidence angle
    Phi_list = np.deg2rad(np.linspace(0, 89, 90))

    # Analytical calculation

    # Reduced wavenumber
    Kx = n_f * np.sin(Phi_list)

    Phi_s = np.arcsin((Kx / n_s).astype(complex))
    Phi_b = np.arcsin((Kx / n_b).astype(complex))

    # Wave vector:
    kz_f = n_f * k0 * np.cos((Phi_list.astype(complex)))
    kz_s = k0 * np.sqrt((-(Kx**2 - n_s**2)).astype(complex))
    kz_b = n_b * k0 * np.cos(Phi_b)

    # Amplitude coefficient for 's' polarisation:
    r_sf_s = (kz_f - kz_s) / (kz_s + kz_f)
    r_bs_s = (kz_s - kz_b) / (kz_s + kz_b)
    t_sf_s = 1 + r_sf_s
    t_bs_s = 1 + r_bs_s

    # Amplitude coefficient for 'p' polarisation:
    r_sf_p = (kz_f * n_s**2 - kz_s * n_f**2) / (kz_s * n_f**2 + kz_f * n_s**2)
    r_bs_p = (kz_s * n_b**2 - kz_b * n_s**2) / (kz_s * n_b**2 + kz_b * n_s**2)
    t_sf_p = np.cos((Phi_list.astype(complex))) * (1 - r_sf_p) / np.cos(Phi_s)
    t_bs_p = np.cos(Phi_s) * (1 - r_bs_p) / np.cos(Phi_b)

    # Power coefficients:
    R_th_s = (
        np.abs(
            (r_sf_s + r_bs_s * np.exp(2j * kz_s * d))
            / (1 + r_bs_s * r_sf_s * np.exp(2j * kz_s * d))
        )
    ) ** 2

    t2_th_s = (
        np.abs(
            (t_bs_s * t_sf_s * np.exp(1j * kz_s * d))
            / (1 + r_bs_s * r_sf_s * np.exp(2j * kz_s * d))
        )
    ) ** 2

    R_th_p = (
        np.abs(
            (r_sf_p + r_bs_p * np.exp(2j * kz_s * d))
            / (1 + r_bs_p * r_sf_p * np.exp(2j * kz_s * d))
        )
    ) ** 2

    t2_th_p = (
        np.abs(
            (t_bs_p * t_sf_p * np.exp(1j * kz_s * d))
            / (1 + r_bs_p * r_sf_p * np.exp(2j * kz_s * d))
        )
    ) ** 2

    correction = np.real(n_b * np.cos(Phi_b) / (n_f * np.cos(Phi_list.astype(complex))))
    # This is a correction term used in R +T*correction = 1

    T_th_s = t2_th_s * correction
    T_th_p = t2_th_p * correction

    def test_tir_angle_4x4_expm(self):
        data = elli.ResultList(
            [self.s.evaluate(self.lbda, np.rad2deg(Phi_i)) for Phi_i in self.Phi_list]
        )

        # Extraction of the transmission and reflexion coefficients
        R_p = data.R_pp
        R_s = data.R_ss
        T_p = data.T_pp
        T_s = data.T_ss
        t2_p = np.abs(data.t_pp) ** 2  # Before power correction
        t2_s = np.abs(data.t_ss) ** 2

        np.testing.assert_allclose(R_p, self.R_th_p)
        np.testing.assert_allclose(R_s, self.R_th_s)
        np.testing.assert_allclose(T_p, self.T_th_p)
        np.testing.assert_allclose(T_s, self.T_th_s)
        np.testing.assert_allclose(t2_p, self.t2_th_p)
        np.testing.assert_allclose(t2_s, self.t2_th_s)

    def test_tir_angle_4x4_eig(self):
        data = elli.ResultList(
            [
                self.s.evaluate(
                    self.lbda,
                    np.rad2deg(Phi_i),
                    solver=elli.Solver4x4,
                    propagator=elli.PropagatorEig(),
                )
                for Phi_i in self.Phi_list
            ]
        )

        # Extraction of the transmission and reflexion coefficients
        R_p = data.R_pp
        R_s = data.R_ss
        T_p = data.T_pp
        T_s = data.T_ss
        t2_p = np.abs(data.t_pp) ** 2  # Before power correction
        t2_s = np.abs(data.t_ss) ** 2

        np.testing.assert_allclose(R_p, self.R_th_p)
        np.testing.assert_allclose(R_s, self.R_th_s)
        np.testing.assert_allclose(T_p, self.T_th_p)
        np.testing.assert_allclose(T_s, self.T_th_s)
        np.testing.assert_allclose(t2_p, self.t2_th_p)
        np.testing.assert_allclose(t2_s, self.t2_th_s)

    def test_tir_angle_2x2(self):
        data = elli.ResultList(
            [
                self.s.evaluate(self.lbda, np.rad2deg(Phi_i), solver=elli.Solver2x2)
                for Phi_i in self.Phi_list
            ]
        )

        # Extraction of the transmission and reflexion coefficients
        R_p = data.R_pp
        R_s = data.R_ss
        T_p = data.T_pp
        T_s = data.T_ss
        t2_p = np.abs(data.t_pp) ** 2  # Before power correction
        t2_s = np.abs(data.t_ss) ** 2

        np.testing.assert_allclose(R_p, self.R_th_p)
        np.testing.assert_allclose(R_s, self.R_th_s)
        np.testing.assert_allclose(T_p, self.T_th_p)
        np.testing.assert_allclose(T_s, self.T_th_s)
        np.testing.assert_allclose(t2_p, self.t2_th_p)
        np.testing.assert_allclose(t2_s, self.t2_th_s)


def test_4x4_transition_matrix_halfspace():
    # Refractive indices
    n_glass = 1.5
    n_air = 1.0

    # Materials:
    glass = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_glass))
    air = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_air))

    # Pseudo uniaxial Backhalfspace, to force different algorithm
    air_uniaxial = elli.UniaxialMaterial(
        elli.ConstantRefractiveIndex(n=n_air), elli.ConstantRefractiveIndex(n=n_air)
    )

    # Structure:
    s = elli.Structure(glass, [], air)
    s2 = elli.Structure(glass, [], air_uniaxial)

    # Wavelength
    lbda = 1000  # nm

    # Variation of incidence angle
    Phi_list = np.linspace(0, 89, 90)

    R = []
    R_uni = []

    for Phi_i in Phi_list:
        data = s.evaluate(lbda, Phi_i)
        R.append(data.R[0])

        data2 = s2.evaluate(lbda, Phi_i)
        R_uni.append(data2.R[0])

    R = np.array(R)
    R_uni = np.array(R_uni)

    np.testing.assert_allclose(R, R_uni)
