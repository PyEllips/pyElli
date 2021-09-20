# Encoding: utf-8
from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt
from scipy.linalg import expm as scipy_expm
import scipy.constants as sc

try:
    import tensorflow as tf
except ImportError:
    pass

try:
    import torch
except ImportError:
    pass

from .materials import IsotropicMaterial
from .solver import Solver
from .result import Result


class Propagator(ABC):
    @abstractmethod
    def calculate_propagation(self, Delta: npt.NDArray, h: float, lbda: npt.ArrayLike) -> npt.NDArray:
        pass


class PropagatorLinear(Propagator):
    def calculate_propagation(self, Delta: npt.NDArray, h: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns propagator with linear approximation."""
        P_hs_lin = np.identity(4) + 1j * h * \
            np.einsum('nij,n->nij', Delta, 2 * sc.pi / lbda)
        return P_hs_lin


class PropagatorExpmScipy(Propagator):
    def calculate_propagation(self, Delta: npt.NDArray, h: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns propagator with Padé approximation.

        The diagonal Padé approximant of any order is symplectic, i.e.
        P_hs_Pade(h)·P_hs_Pade(-h) = 1.
        Such property may be suitable for use with Z. Lu's method.
        """
        mats = 1j * h * np.einsum('nij,n->nij', Delta, 2 * sc.pi / lbda)

        P_hs_Pade = np.asarray([scipy_expm(mat) for mat in mats])

        return P_hs_Pade


class PropagatorExpmTorch(Propagator):
    def calculate_propagation(self, Delta: npt.NDArray, h: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns propagator with Padé approximation.

        The diagonal Padé approximant of any order is symplectic, i.e.
        P_hs_Pade(h)·P_hs_Pade(-h) = 1.
        Such property may be suitable for use with Z. Lu's method.
        """
        mats = 1j * h * np.einsum('nij,n->nij', Delta, 2 * sc.pi / lbda)

        t = torch.from_numpy(mats)
        texp = torch.matrix_exp(t)
        P_hs_Pade = np.asarray(texp.numpy(), dtype=np.complex128)

        return P_hs_Pade


class PropagatorExpmTF(Propagator):
    def calculate_propagation(self, Delta: npt.NDArray, h: float, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns propagator with Padé approximation.

        The diagonal Padé approximant of any order is symplectic, i.e.
        P_hs_Pade(h)·P_hs_Pade(-h) = 1.
        Such property may be suitable for use with Z. Lu's method.
        """
        mats = 1j * h * np.einsum('nij,n->nij', Delta, 2 * sc.pi / lbda)

        t = tf.convert_to_tensor(np.asarray(mats, dtype=np.complex64))
        texp = tf.linalg.expm(t)
        P_hs_Pade = np.array(texp, dtype=np.complex128)

        return P_hs_Pade


class Solver4x4(Solver):
    """
    Solver class to evaluate Experiment objects.
    Based on Berreman's 4x4 method.
    """
    _S = None
    _jones_matrix_t = None
    _jones_matrix_r = None

    @staticmethod
    def buildDeltaMatrix(Kx: npt.ArrayLike, eps: npt.NDArray) -> npt.NDArray:
        """Returns Delta matrix for given permittivity and reduced wave number.

        'Kx' : reduce wave number, Kx = kx/k0
        'eps' : permittivity tensor

        Returns : Delta 4x4 matrix, generator of infinitesimal translations
        """
        if np.shape(Kx) == ():
            i = 1
        else:
            i = np.shape(Kx)[0]

        Delta = np.array(
            [[-Kx * eps[:, 2, 0] / eps[:, 2, 2], -Kx * eps[:, 2, 1] / eps[:, 2, 2],
              np.tile(0, i), np.tile(1, i) - Kx ** 2 / eps[:, 2, 2]],
             [np.tile(0, i), np.tile(0, i), np.tile(-1, i), np.tile(0, i)],
             [eps[:, 1, 2] * eps[:, 2, 0] / eps[:, 2, 2] - eps[:, 1, 0],
              Kx ** 2 - eps[:, 1, 1] + eps[:, 1, 2] * eps[:, 2, 1] / eps[:, 2, 2],
              np.tile(0, i), Kx * eps[:, 1, 2] / eps[:, 2, 2]],
             [eps[:, 0, 0] - eps[:, 0, 2] * eps[:, 2, 0] / eps[:, 2, 2],
              eps[:, 0, 1] - eps[:, 0, 2] * eps[:, 2, 1] / eps[:, 2, 2],
              np.tile(0, i), -Kx * eps[:, 0, 2] / eps[:, 2, 2]]], dtype=np.complex128)
        Delta = np.moveaxis(Delta, 2, 0)
        return Delta

    @staticmethod
    def TransitionMatrixHalfspace(Delta: npt.NDArray) -> npt.NDArray:
        """Returns transition matrix L.

        'Kx' : reduced wavenumber in the x direction, Kx = kx/k0
        'k0' : wavenumber in vacuum, k0 = ω/c

        Sort eigenvectors of the Delta matrix according to propagation
        direction first, then according to $y$ component.

        Returns eigenvectors ordered like (s+,s-,p+,p-)
        """
        q, Psi = np.linalg.eig(Delta)

        # Round to remove numerical noise
        q = q.round(16)

        # Sort according to z propagation direction, highest Re(q) first
        # if Re(q) is zero, sort by Im(q)
        i = np.where(q.real == 0, np.argsort(-np.imag(q)), np.argsort(-np.real(q)))

        q = np.take_along_axis(q, i, axis=-1)
        Psi = np.take_along_axis(Psi, i[:, np.newaxis, :], axis=-1)
        # Result should be (+,+,-,-)

        # For each direction, sort according to Ey component, highest Ey first
        i1 = np.argsort(-np.abs(Psi[:, 1, :2]))
        i2 = 2 + np.argsort(-np.abs(Psi[:, 1, 2:]))
        i = np.hstack((i1, i2))
        # Result should be (s+,p+,s-,p-)

        # Reorder
        i[:, [1, 2]] = i[:, [2, 1]]

        q = np.take_along_axis(q, i, axis=-1)
        Psi = np.take_along_axis(Psi, i[:, np.newaxis, :], axis=-1)
        # Result should be(s+,s-,p+,p-)

        # Adjust Ey in ℝ⁺ for 's', and Ex in ℝ⁺ for 'p'
        E = np.hstack((Psi[:, 1, :2], Psi[:, 0, 2:]))

        nE = np.abs(E)
        c = np.ones_like(E)
        i = (nE != 0.0)
        c[i] = E[i] / nE[i]

        Psi = Psi * c[:, np.newaxis, :]

        # Normalize so that Ey = c1 + c2, analog to Ey = Eis + Ers
        # For an isotropic half-space, this should return the same matrix
        # as IsotropicHalfSpace
        c = Psi[:, 1, 0] + Psi[:, 1, 1]
        np.where(np.abs(c) == 0, 1, c)

        Psi = 2 * Psi / c[:, np.newaxis, np.newaxis]

        return Psi

    @staticmethod
    def TransitionMatrixIsoHalfspace(Kx: npt.ArrayLike, epsilon: npt.ArrayLike, inv: bool = False) -> npt.NDArray:
        """Returns transition matrix L.

        'Kx' : Reduced wavenumber
        'epsilon' : dielectric tensor
        'inv' : if True, returns inverse transition matrix L^-1

        Returns : transition matrix L
        """
        nx = sqrt(epsilon[:, 0, 0])
        sin_Phi = Kx / nx
        cos_Phi = sqrt(1 - sin_Phi ** 2)

        i = np.shape(Kx)[0]

        if inv:
            L = np.tile(np.array([[0, 1, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]], dtype=np.complex128), (i, 1, 1))
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [1, 0, 0, 0],
                                   [1, 0, 0, 0]]), (i, 1, 1)) / cos_Phi[:, None, None]
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 1],
                                   [0, 0, 0, -1]]), (i, 1, 1)) / nx[:, None, None]
            L += np.tile(np.array([[0, 0, -1, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0]]), (i, 1, 1)) / cos_Phi[:, None, None] / nx[:, None, None]
            return 0.5 * L
            #   np.array(
            # [[0, 1, -1/(nx*cos_Phi),  0],
            #  [0, 1,  1/(nx*cos_Phi),  0],
            #  [1/cos_Phi, 0,  0,  1/nx],
            #  [1/cos_Phi, 0,  0, -1/nx]])
        else:
            L = np.tile(np.array([[0, 0, 0, 0],
                                  [1, 1, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]], dtype=np.complex128), (i, 1, 1))
            L += np.tile(np.array([[0, 0, 1, 1],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0]]), (i, 1, 1)) * cos_Phi[:, None, None]
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 1, -1]]), (i, 1, 1)) * nx[:, None, None]
            L += np.tile(np.array([[0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [-1, 1, 0, 0],
                                   [0, 0, 0, 0]]), (i, 1, 1)) * cos_Phi[:, None, None] * nx[:, None, None]
            return L
            # np.array(
            # [[0, 0, cos_Phi, cos_Phi],
            #  [1, 1, 0, 0],
            #  [-nx*cos_Phi, nx*cos_Phi, 0, 0],
            #  [0, 0, nx, -nx]])

    @staticmethod
    def getKz(material: "Material", lbda: npt.ArrayLike, Kx: npt.ArrayLike) -> npt.NDArray:
        """Returns the value of Kz in the half-space"""
        nx = material.getRefractiveIndex(lbda)[:, 0, 0]
        Kz2 = nx ** 2 - Kx ** 2
        return sqrt(Kz2)

    @property
    def rho(self) -> npt.NDArray:
        rho = np.dot(self._S, self.jonesVector)
        rho = rho[:, 0] / rho[:, 1]
        return rho

    @property
    def psi(self) -> npt.NDArray:
        return np.rad2deg(np.arctan(np.abs(self.rho)))

    @property
    def delta(self) -> npt.NDArray:
        d = -np.angle(self.rho, deg=True)
        return np.where(d < 0, d + 360, d)

    @property
    def rhoMat(self) -> npt.NDArray:
        return self._S

    @property
    def psiMat(self) -> npt.NDArray:
        return np.rad2deg(np.arctan(np.abs(self.rhoMat)))

    @property
    def deltaMat(self) -> npt.NDArray:
        return -np.angle(self.rhoMat, deg=True)

    @property
    def mueller_matrix(self) -> npt.NDArray:
        if self._S is None:
            return None

        A = np.array([[1, 0, 0, 1],
                      [1, 0, 0, -1],
                      [0, 1, 1, 0],
                      [0, 1j, -1j, 0]])

        # Kroneker product of S and S*
        SxS_star = np.einsum('aij,akl->aikjl', self._S,
                             np.conjugate(self._S)).reshape(self._S.shape[0], 4, 4)

        mmatrix = np.real(A @ SxS_star @ A.T)
        m11 = mmatrix[:, 0, 0]

        return mmatrix / m11[:, None, None]

    @property
    def jones_matrix_t(self) -> npt.NDArray:
        return self._jones_matrix_t

    @property
    def jones_matrix_r(self) -> npt.NDArray:
        return self._jones_matrix_r

    @property
    def R(self) -> npt.NDArray:
        return np.abs(self._jones_matrix_r) ** 2

    @property
    def T(self) -> npt.NDArray:
        return np.abs(self._jones_matrix_t) ** 2 * self.powerCorrection[:, None, None]

    def __init__(self, experiment: "Experiment", propagator: Propagator = PropagatorExpmScipy()) -> None:
        super().__init__(experiment)
        self.propagator = propagator

        # Kx = kx/k0 = n sin(Φ) : Reduced wavenumber.
        nx = self.structure.frontMaterial.getRefractiveIndex(self.lbda)[:, 0, 0]
        self.Kx = nx * np.sin(np.deg2rad(self.theta_i))

    def calculate(self) -> Result:
        """Simulates optical Experiment"""
        layers = reversed(self.permProfile[1:-1])

        ILf = self.TransitionMatrixIsoHalfspace(self.Kx, self.permProfile[0], inv=True)

        P_tot = np.identity(4)
        for d, epsilon in layers:
            P = self.propagator.calculate_propagation(
                self.buildDeltaMatrix(self.Kx, epsilon), -d, self.lbda)
            P_tot = P @ P_tot

        if isinstance(self.structure.backMaterial, IsotropicMaterial):
            Lb = self.TransitionMatrixIsoHalfspace(self.Kx, self.permProfile[-1])
        else:
            Lb = self.TransitionMatrixHalfspace(
                self.buildDeltaMatrix(self.Kx, self.permProfile[-1]))

        T = ILf @ P_tot @ Lb

        # Extraction of T_it out of T. "2::-2" means integers {2,0}.
        T_it = T[:, 2::-2, 2::-2]
        # Calculate the inverse and make sure it is a matrix.
        T_ti = np.linalg.inv(T_it)

        # Extraction of T_rt out of T. "3::-2" means integers {3,1}.
        T_rt = T[:, 3::-2, 2::-2]

        # Then we have T_ri = T_rt * T_ti
        T_ri = T_rt @ T_ti

        r_ss = T_ri[..., 1, 1]
        S = T_ri / r_ss[:, None, None]
        S[..., 0, :] = -S[..., 0, :]

        Kzf = self.getKz(self.structure.frontMaterial, self.lbda, self.Kx)
        if isinstance(self.structure.backMaterial, IsotropicMaterial):
            Kzb = self.getKz(self.structure.backMaterial, self.lbda, self.Kx)
            self.powerCorrection = Kzb.real / Kzf.real
        else:
            self.powerCorrection = np.ones_like(self.lbda)
        # The power transmission coefficient is the ratio of the 'z' components
        # of the Poynting vector:       T = P_t_z / P_i_z
        # For isotropic media, we have: T = kb'/kf' |t_bf|^2
        # The correction coefficient is kb'/kf'
        # Note : For the moment it is only meaningful for isotropic half spaces.

        self._jones_matrix_t = T_ti
        self._jones_matrix_r = T_ri
        self._S = S

        return Result(self)
