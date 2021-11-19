# Encoding: utf-8
import numpy as np
from numpy.lib.scimath import arcsin, sqrt

from .solver import Solver
from .result import Result


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
        if self._rtotp is None or self._rtots is None:
            return None
        return np.rad2deg(np.arctan(np.abs(self._rtotp / self._rtots)))

    @property
    def rho(self):
        if self._rtotp is None or self._rtots is None:
            return None
        return self._rtotp / self._rtots

    @property
    def delta(self):
        if self._rtotp is None or self._rtots is None:
            return None
        return -np.angle(self._rtotp / self._rtots, deg=True)

    @property
    def R(self):
        return np.abs(self._rtotp + self._rtots)

    def list_snell(self, n_list):
        angles = arcsin(n_list[0] * np.sin(np.deg2rad(self.theta_i)) / n_list)

        angles[0] = np.where(np.invert(Solver2x2.is_forward_angle(n_list[0], angles[0])),
                             np.pi - angles[0], angles[0])
        angles[-1] = np.where(np.invert(Solver2x2.is_forward_angle(n_list[-1], angles[-1])),
                              np.pi - angles[-1], angles[-1])

        return angles

    def calculate(self) -> Result:
        """Calculates the transfer matrix for the given material stack"""
        if len(self.permittivity_profile) > 2:
            d, eps = list(zip(*self.permittivity_profile[1:-1]))
            d_list = np.array(d)
            n_list = sqrt(np.vstack([self.permittivity_profile[0][1][:, 0, 0],
                                     np.array(eps)[..., 0, 0],
                                     self.permittivity_profile[-1][1][:, 0, 0]]))
        else:
            d_list = np.array([])
            n_list = sqrt(np.vstack([self.permittivity_profile[0][1][:, 0, 0],
                                     self.permittivity_profile[-1][1][:, 0, 0]]))

        num_layers = n_list.shape[0]
        th_list = self.list_snell(n_list)
        kz_list = 2 * np.pi * n_list * np.cos(th_list) / self.lbda

        delta = kz_list[1:-1] * (d_list if n_list.ndim == 1 else d_list[:, None])

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

        self._rtots = Ms[1, 0] / Ms[0, 0]
        self._ttots = 1 / Ms[0, 0]
        self._rtotp = Mp[1, 0] / Mp[0, 0]
        self._ttotp = 1 / Mp[0, 0]

        return Result(self)

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
