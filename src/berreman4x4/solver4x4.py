# Encoding: utf-8
import numpy as np

from .materials import IsotropicMaterial
from .solver4x4_math import hs_propagator_pade_scipy, TransitionMatrixHalfspace, TransitionMatrixIsoHalfspace, \
    buildDeltaMatrix, getPowerTransmissionCorrection
from .solver import Solver
from .result import Result


class Solver4x4(Solver):
    """
    Solver class to evaluate Experiment objects.
    Based on Berreman's 4x4 method.
    """
    _S = None
    _jones_matrix_t = None
    _jones_matrix_r = None

    @property
    def rho(self):
        rho = np.dot(self._S, self.jonesVector)
        rho = rho[:, 0] / rho[:, 1]
        return rho

    @property
    def psi(self):
        return np.rad2deg(np.arctan(np.abs(self.rho)))

    @property
    def delta(self):
        d = -np.angle(self.rho, deg=True)
        return np.where(d < 0, d + 360, d)

    @property
    def mueller_matrix(self):
        if self._S is None:
            return None

        A = np.array([[1, 0, 0, 1],
                      [1, 0, 0, -1],
                      [0, 1, 1, 0],
                      [0, 1j, -1j, 0]])

        # Kroneker product of S and S*
        SxS_star = np.einsum('aij,akl->aikjl', self._S, np.conjugate(self._S)).reshape(self._S.shape[0], 4, 4)

        mmatrix = np.real(A @ SxS_star @ A.T)
        m11 = mmatrix[:, 0, 0]

        return mmatrix / m11[:, None, None]

    @property
    def jones_matrix_t(self):
        return self._jones_matrix_t

    @property
    def jones_matrix_r(self):
        return self._jones_matrix_r

    @property
    def R(self):
        return np.abs(self._jones_matrix_r)**2

    @property
    def T(self):
        return np.abs(self._jones_matrix_t)**2 * self.powerCorrection[:, None, None]

    def __init__(self, experiment, hs_propagator=hs_propagator_pade_scipy):
        super().__init__(experiment)
        self.hs_propagator = hs_propagator

    def calculate(self):
        """Simulates optical Experiment"""

        # Kx = kx/k0 = n sin(Φ) : Reduced wavenumber.
        nx = self.structure.frontMaterial.getRefractiveIndex(self.lbda)[:, 0, 0]
        Kx = nx * np.sin(np.deg2rad(self.theta_i))

        layers = reversed(self.permProfile[1:-1])

        ILf = TransitionMatrixIsoHalfspace(Kx, self.permProfile[0], inv=True)

        P_tot = np.identity(4)
        for d, epsilon in layers:
            P = hs_propagator_pade_scipy(buildDeltaMatrix(self.Kx, epsilon), -d, self.lbda)
            P_tot = P @ P_tot

        if isinstance(self.structure.backMaterial, IsotropicMaterial):
            Lb = TransitionMatrixIsoHalfspace(self.Kx, self.permProfile[-1])
        else:
            Lb = TransitionMatrixHalfspace(self.Kx, self.permProfile[-1])

        T = ILf @ P_tot @ Lb

        # Extraction of T_it out of T. "2::-2" means integers {2,0}.
        T_it = T[:, 2::-2, 2::-2]
        # Calculate the inverse and make sure it is a matrix.
        T_ti = np.linalg.inv(T_it)

        # Extraction of T_rt out of T. "3::-2" means integers {3,1}.
        T_rt = T[:, 3::-2, 2::-2]

        # Then we have T_ri = T_rt * T_ti
        T_ri = T_rt @ T_ti

        # Normalize for r_ss
        r_ss = T_ri[..., 1, 1]
        S = T_ri / r_ss[:, None, None]
        S[..., 0, :] = -S[..., 0, :]

        self.powerCorrection = getPowerTransmissionCorrection(self.structure, self.lbda, self.Kx)

        self._jones_matrix_t = T_ti
        self._jones_matrix_r = T_ri
        self._S = S

        return Result(self)
