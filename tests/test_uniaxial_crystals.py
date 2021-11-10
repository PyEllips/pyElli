#!/usr/bin/python
# encoding: utf-8

import numpy as np
import berreman4x4 as bm


class TestUniaxial:
    n_i = 1.0  # incident medium is air
    n_o = 2.0  # ordinary index of thin layer
    n_e = 2.5  # extraordinary index of thin layer
    lbda = 620  # Wavelength for evaluation (nm)
    Phi_i = 70  # 70° incidence angle (degree)self.
    d = 100  # thin layer thickness (nm)
    Phi_E = 45  # 1st Euler angle
    Theta_E = 45  # 2nd Euler angle

    filmMaterial = bm.UniaxialMaterial(bm.DispersionLess(n_o),
                                       bm.DispersionLess(n_e))
    R = bm.rotation_Euler(Phi_E, Theta_E, 0)
    filmMaterial.setRotation(R)

    air = bm.IsotropicMaterial(bm.DispersionLess(n_i))
    Kx = n_i * np.sin(np.deg2rad(Phi_i))
    film = bm.Layer(filmMaterial, d)
    epsilon = filmMaterial.getTensor(lbda)
    Delta = bm.Solver4x4.build_delta_matrix(Kx, epsilon)

    Tp = bm.PropagatorExpmScipy().calculate_propagation(Delta, -d, np.array([lbda]))

    n_t = 3.898 + 0.016j  # refractive index of substrate
    silicon = bm.IsotropicMaterial(bm.DispersionLess(n_t))
    s = bm.Structure(air, [film], silicon)
    data = s.evaluate(np.array([lbda]), Phi_i)

    def test_rotated_tensor(self):
        tensor = np.array([[[4.5625 + 0j, -0.5625 + 0j, 0.7955 + 0j],
                            [-0.5625 + 0j, 4.5625 + 0j, -0.7955 + 0j],
                            [0.7955 + 0j, -0.7955 + 0j, 5.125 + 0j]]])

        np.testing.assert_allclose(self.filmMaterial.getTensor(self.lbda), tensor, 1e-3, 0)

    def test_build_delta_matrix(self):
        delta_matrix = np.array([[-0.1459, 0.1459, 0., 0.8277],
                                 [0., 0., -1., 0.],
                                 [0.439, -3.556, 0., -0.1459],
                                 [4.439, -0.439, 0., -0.1459]], dtype=np.complex128)

        np.testing.assert_allclose(self.Delta[0], delta_matrix, 1e-3, 0)

    def test_transition_matrix(self):
        transition_matrix = np.array([[[-0.353 - 0.057j, 0.091 - 0.001j, 0.033 + 0.044j, 0.056 - 0.397j],
                                       [0.104 + 0.08j, -0.327 - 0.011j, 0.004 + 0.502j, -0.033 - 0.044j],
                                       [0.162 - 0.014j, -0.017 + 1.753j, -0.327 - 0.011j, -0.091 + 0.001j],
                                       [0.300 - 2.12j, -0.162 + 0.014j, -0.104 - 0.08j, -0.353 - 0.057j]]])

        np.testing.assert_allclose(self.Tp, transition_matrix, 1e-2, 0)

    def test_jones_calculation(self):
        jones_matrix = np.array([[[-0.310 - 0.161j, -0.107 - 0.002j],
                                  [0.042 - 0.036j, -0.552 + 0.151j]]])

        np.testing.assert_allclose(self.data.jones_matrix_r, jones_matrix, 5e-2, 0)

    def test_psi_calculation(self):
        psi = np.array([[[31.4419, 10.5641],
                         [5.5332, 45.]]])

        np.testing.assert_allclose(self.data.psiMat, psi, 1e-3, 0)

    def test_delta_calculation(self):
        delta = np.array([[[42.734, 16.4123],
                           [155.024, 0.]]])

        np.testing.assert_allclose(self.data.deltaMat, delta, 1e-3, 1e-1)
