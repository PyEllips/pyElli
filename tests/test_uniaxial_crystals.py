#!/usr/bin/python
# encoding: utf-8

import numpy as np
import elli


class TestUniaxial:
    n_i = 1.0  # incident medium is air
    n_o = 2.0  # ordinary index of thin layer
    n_e = 2.5  # extraordinary index of thin layer
    lbda = 620  # Wavelength for evaluation (nm)
    Phi_i = 70  # 70° incidence angle (degree)self.
    d = 100  # thin layer thickness (nm)
    Phi_E = 45  # 1st Euler angle
    Theta_E = 45  # 2nd Euler angle

    filmMaterial = elli.UniaxialMaterial(
        elli.ConstantRefractiveIndex(n=n_o), elli.ConstantRefractiveIndex(n=n_e)
    )
    R = elli.rotation_euler(Phi_E, Theta_E, 0)
    filmMaterial.set_rotation(R)

    air = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_i))
    Kx = n_i * np.sin(np.deg2rad(Phi_i))
    film = elli.Layer(filmMaterial, d)
    epsilon = filmMaterial.get_tensor(lbda)
    Delta = elli.Solver4x4.build_delta_matrix(Kx, epsilon)

    air = elli.AIR
    epsilon_air = air.get_tensor(lbda)

    Tp = elli.PropagatorExpmScipy().calculate_propagation(Delta, -d, np.array([lbda]))
    Li = elli.Solver4x4.transition_matrix_iso_halfspace(
        np.array([Kx]), epsilon_air, inv=True
    )

    n_t = 3.898 + 0.016j  # refractive index of substrate
    silicon = elli.IsotropicMaterial(elli.ConstantRefractiveIndex(n=n_t))
    epsilon_silicon = silicon.get_tensor(lbda)
    Lt = elli.Solver4x4.transition_matrix_iso_halfspace(
        np.array([Kx]), epsilon_silicon, inv=False
    )
    s = elli.Structure(air, [film], silicon)
    data = s.evaluate(np.array([lbda]), Phi_i)

    def test_rotated_tensor(self):
        tensor = np.array(
            [
                [
                    [4.5625 + 0j, -0.5625 + 0j, 0.7955 + 0j],
                    [-0.5625 + 0j, 4.5625 + 0j, -0.7955 + 0j],
                    [0.7955 + 0j, -0.7955 + 0j, 5.125 + 0j],
                ]
            ]
        )

        np.testing.assert_array_almost_equal(
            self.filmMaterial.get_tensor(self.lbda), tensor, decimal=4
        )

    def test_build_delta_matrix(self):
        delta_matrix = np.array(
            [
                [-0.1459, 0.1459, 0.0, 0.8277],
                [0.0, 0.0, -1.0, 0.0],
                [0.439, -3.556, 0.0, -0.1459],
                [4.439, -0.439, 0.0, -0.1459],
            ],
            dtype=np.complex128,
        )

        np.testing.assert_array_almost_equal(self.Delta[0], delta_matrix, decimal=3)

    def test_transition_matrix(self):
        transition_matrix = np.array(
            [
                [
                    [-0.352 - 0.057j, 0.091 - 0.001j, 0.033 + 0.044j, 0.056 - 0.397j],
                    [0.104 + 0.08j, -0.326 - 0.011j, 0.004 + 0.502j, -0.033 - 0.044j],
                    [0.162 - 0.014j, -0.017 + 1.753j, -0.326 - 0.011j, -0.091 + 0.001j],
                    [0.300 - 2.12j, -0.162 + 0.014j, -0.104 - 0.08j, -0.352 - 0.057j],
                ]
            ]
        )

        np.testing.assert_array_almost_equal(self.Tp, transition_matrix, decimal=3)

    def test_li_matrix(self):
        n_i = 1
        cos_phi = 0.342

        li = (
            np.array(
                [
                    [
                        [0, 1, -1 / n_i / cos_phi, 0],
                        [0, 1, 1 / n_i / cos_phi, 0],
                        [1 / cos_phi, 0, 0, 1 / n_i],
                        [-1 / cos_phi, 0, 0, 1 / n_i],
                    ]
                ],
                dtype=np.complex128,
            )
            * 0.5
        )

        np.testing.assert_array_almost_equal(self.Li, li, decimal=3)

    def test_lt_matrix(self):
        n_x = 3.898 + 1j * 0.016
        cos_phi = 0.9705 + 1j * 2.4e-4
        lt = np.array(
            [
                [
                    [0, 0, cos_phi, -cos_phi],
                    [1, 1, 0, 0],
                    [-n_x * cos_phi, n_x * cos_phi, 0, 0],
                    [0, 0, n_x, n_x],
                ]
            ],
            dtype=np.complex128,
        )

        np.testing.assert_array_almost_equal(self.Lt, lt, decimal=3)

    def test_transition_matrix_with_halfspace(self):
        # Fujiwara Original
        tmatrix = np.array(
            [
                [
                    [
                        -1.946 - 1j * 3.588,
                        1.668 - 1j * 1.548,
                        0.273 + 1j * 0.03,
                        0.63 - 1j * 0.148,
                    ],
                    [
                        1.614 + 1j * 1.679,
                        -1.989 + 1j * 3.435,
                        -0.301 - 1j * 0.064,
                        -0.861 - 1j * 0.101,
                    ],
                    [
                        0.065 - 1j * 0.086,
                        0.039 + 1j * 0.097,
                        -0.71 - 1j * 3.486,
                        -0.003 - 1j * 1.266,
                    ],
                    [
                        0.167 + 1j * 0.403,
                        -0.593 - 1j * 0.386,
                        -0.369 + 1j * 1.199,
                        -1.66 + 1j * 3.094,
                    ],
                ]
            ]
        )

        np.testing.assert_array_almost_equal(
            self.Li @ self.Tp @ self.Lt, tmatrix, decimal=1
        )

    def test_jones_calculation(self):
        jones_matrix = np.array(
            [[[-0.311 - 0.161j, -0.107 - 0.002j], [0.042 - 0.036j, -0.551 + 0.151j]]]
        )

        np.testing.assert_array_almost_equal(
            self.data.jones_matrix_r, jones_matrix, decimal=3
        )

    def test_psi_calculation(self):
        psi = np.array([[[31.46, 10.57], [5.54, 45.0]]])

        np.testing.assert_array_almost_equal(self.data.psi_matrix, psi, decimal=2)

    def test_delta_calculation(self):
        delta = np.array([[[-42.67, -16.35], [-154.93, 0.0]]])

        np.testing.assert_array_almost_equal(self.data.delta_matrix, delta, decimal=1)
