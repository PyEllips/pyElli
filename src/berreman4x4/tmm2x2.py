# Encoding: utf-8
import numpy as np
from numpy.lib.scimath import arcsin

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

def is_forward_angle(n, theta): 
    ncostheta = n * np.cos(theta)
    return np.where(abs(ncostheta.imag) > 1e-10, ncostheta.imag > 0, ncostheta.real > 0)

def list_snell(n_list, th_0):
    angles = arcsin(n_list[0] * np.sin(th_0) / n_list)

    angles[0] = np.where(np.invert(is_forward_angle(n_list[0], angles[0])), 
                         np.pi - angles[0], angles[0])
    angles[-1] = np.where(np.invert(is_forward_angle(n_list[-1], angles[-1])), 
                         np.pi - angles[-1], angles[-1])

    return angles

def calc_ellips(n_list, d_list, Θ, λ):
    λ = np.array(λ)
    n_list = np.array(n_list)
    d_list = np.array(d_list, dtype=float)

    if n_list.shape[0] != d_list.shape[0]:
        raise Exception("n and d arrays should have the same length")

    if not n_list.ndim == 1 and n_list.shape[1] != λ.size:
        raise Exception("n and λ should have the same length")

    num_layers = n_list.shape[0]
    th_list = list_snell(n_list, Θ)
    kz_list = 2 * np.pi * n_list * np.cos(th_list) / λ

    # TODO(Flo): multiply only the layers to avoid inf multiplication. 
    # Should not be relevant when integrated into the half space formalism.
    olderr = np.seterr(invalid='ignore')
    delta = kz_list * (d_list if n_list.ndim == 1 else d_list[:,None])
    np.seterr(**olderr)

    esum = 'ij...,jk...->ik...'
    ones = np.repeat(1, n_list.shape[1]) if n_list.ndim > 1 else 1

    rs, rp, ts, tp = fresnel(n_list[0], n_list[1], th_list[0], th_list[1])
    Ms = np.array([[ones, rs],
                   [rs, ones]], dtype=complex) / ts
    Mp = np.array([[ones, rp],
                   [rp, ones]], dtype=complex) / tp

    for i in range(1, num_layers-1):
        rs, rp, ts, tp = fresnel(n_list[i], n_list[i+1], th_list[i], th_list[i+1])
        em = np.exp(-1j * delta[i])
        ep = np.exp(1j * delta[i])

        Ms = np.einsum(esum, Ms,
                       np.array([[em, rs * em],
                                 [rs * ep, ep]], dtype=complex) / ts)
        Mp = np.einsum(esum, Mp,
                       np.array([[em, rp * em],
                                 [rp * ep, ep]], dtype=complex) / tp)

    # Net complex transmission and reflection amplitudes
    rtots = Ms[1,0] / Ms[0,0]
    ttots = 1 / Ms[0,0]
    rtotp = Mp[1,0] / Mp[0,0]
    ttotp = 1 / Mp[0,0]

    psi = np.arctan(np.abs(rtotp / rtots))
    delta = np.angle(-rtotp / rtots)
    rho = rtotp / rtots

    return psi, delta, rho
