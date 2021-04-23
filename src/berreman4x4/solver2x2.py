# Encoding: utf-8
import numpy as np
from numpy.lib.scimath import arcsin

from .solver import Solver

class Solver2x2(Solver):
    '''
    Solver class to evaluate Experiment objects.
    Simple but fast 2x2 transfer matrix method.
    Cannot handle anisotropy or anything fancy,
    thus Jonas and Mueller matrices cannot be calculated (respective functions return None).
    '''
    _rtots = None
    _ttots = None
    _rtotp = None
    _ttotp = None

    @property
    def psi(self):
        if not all((self._rtotp, self._rtots)):
            return None
        return np.arctan(np.abs(self._rtotp / self._rtots))

    @property
    def rho(self):
        if not all((self._rtotp, self._rtots)):
            return None
        return self._rtotp / self._rtots

    @property
    def delta(self):
        if not all((self._rtotp, self._rtots)):
            return None
        return np.angle(-self._rtotp / self._rtots)

    @property
    def mueller_matrix(self):
        return None

    @property
    def jones_matrix_t(self):
        return None

    @property
    def jones_matrix_r(self):
        return None
        
    def list_snell(n_list):
        angles = arcsin(n_list[0] * np.sin(self.theta_i) / n_list)

        angles[0] = np.where(np.invert(Solver2x2.is_forward_angle(n_list[0], angles[0])), 
                            np.pi - angles[0], angles[0])
        angles[-1] = np.where(np.invert(Solver2x2.is_forward_angle(n_list[-1], angles[-1])), 
                            np.pi - angles[-1], angles[-1])

        return angle
        
    def calculate(self):
        """Calculates the transfer matrix for the given material stack"""
        lbda = np.array(self.lbda)
        d, n = list(zip(*self.permProfile))
        d_list = np.array(d)
        n_list = np.array(n)[:,:,0,0]

        if n_list.shape[0] != d_list.shape[0]:
            raise Exception("Solver2x2: n and d arrays do not have the same length")

        if not n_list.ndim == 1 and n_list.shape[1] != lbda.size:
            raise Exception("Solver2x2: n and lbda arrays do not have the same length")

        num_layers = n_list.shape[0]
        th_list = self.list_snell(n_list)
        kz_list = 2 * np.pi * n_list * np.cos(th_list) / lbda

        delta = kz_list[1:-1] * (d_list[1:-1] if n_list.ndim == 1 else d_list[1:-1,None])

        esum = 'ij...,jk...->ik...'
        ones = np.repeat(1, n_list.shape[1]) if n_list.ndim > 1 else 1

        rs, rp, ts, tp = Solver2x2.fresnel(n_list[0], n_list[1], th_list[0], th_list[1])
        Ms = np.array([[ones, rs],
                       [rs, ones]], dtype=complex) / ts
        Mp = np.array([[ones, rp],
                       [rp, ones]], dtype=complex) / tp

        for i in range(1, num_layers-1):
            rs, rp, ts, tp = Solver2x2.fresnel(n_list[i], n_list[i+1], th_list[i], th_list[i+1])
            em = np.exp(-1j * delta[i-1])
            ep = np.exp(1j * delta[i-1])

            Ms = np.einsum(esum, Ms,
                           np.array([[em, rs * em],
                                     [rs * ep, ep]], dtype=complex) / ts)
            Mp = np.einsum(esum, Mp,
                            np.array([[em, rp * em],
                                      [rp * ep, ep]], dtype=complex) / tp)

        self._rtots = Ms[1,0] / Ms[0,0]
        self._ttots = 1 / Ms[0,0]
        self._rtotp = Mp[1,0] / Mp[0,0]
        self._ttotp = 1 / Mp[0,0]


    @staticmethod
    def fresnel(n_i, n_t, th_i, th_t):
        """Calculate fresnel coefficients at the interface of two materials

            n_i: Refractive index of the material of the incident wave
            n_t: Refractive index of the material of the transmitted wave
            thi_i: Incident angle of the incident wave
            thi_t: Refracted angle of the transmitted wave

            returns:
                r_s: s-polarized reflection coefficient
                r_p: p-polarized reflection coefficient
                t_s: s-polarized transmission coefficient
                t_p: p-polarized transmission coefficient
        """
        cos_i = np.cos(th_i)
        cos_t = np.cos(th_t)

        r_s = (n_i * cos_i - n_t * cos_t) / (n_i * cos_i + n_t * cos_t)
        r_p = (n_t * cos_i - n_i * cos_t) / (n_t * cos_i + n_i * cos_t)
        t_s = 2 * n_i * cos_i / (n_i * cos_i + n_t * cos_t)
        t_p = 2 * n_i * cos_i / (n_i * cos_i + n_i * cos_t)

        return r_s, r_p, t_s, t_p

    @staticmethod
    def is_forward_angle(n, theta): 
        ncostheta = n * np.cos(theta)
        return np.where(abs(ncostheta.imag) > 1e-10,
                        ncostheta.imag > 0, 
                        ncostheta.real > 0)
