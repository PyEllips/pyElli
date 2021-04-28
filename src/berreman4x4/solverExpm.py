# Encoding: utf-8
import numpy as np
from numpy.lib.scimath import sqrt

from .math import buildDeltaMatrix, hs_propagator_Pade
from .settings import settings
from .solver import Solver


class SolverExpm(Solver):
    '''
    Solver class to evaluate Experiment objects.
    Based on Berreman's 4x4 method.
    '''
    _S = None
    _jones_matrix_t = None
    _jones_matrix_r = None

    @property
    def rho(self):
        rho = np.dot(self._S, self.jonesVector)
        rho = rho[:, 0]/rho[:, 1]
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

        A = np.array([[1,  0,    0,  1],
                      [1,  0,    0, -1],
                      [0,  1,    1,  0],
                      [0,  1j, -1j,  0]])

        # Kroneker product of S S*
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

    def calculate(self):
        """Simulates optical Experiment"""

        layers = reversed(self.permProfile[1:-1])

        ILf = TransitionMatrixIsoHalfspace(self.Kx, self.permProfile[0], inv=True)
        P = [hs_propagator_Pade(buildDeltaMatrix(self.Kx, epsilon), -d, self.lbda)
             for d, epsilon in layers]
        Lb = TransitionMatrixHalfspace(self.Kx, self.permProfile[-1])

        P_tot = np.identity(4)
        for p in P:
            P_tot = p @ P_tot
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

        self._jones_matrix_t = T_ti
        self._jones_matrix_r = T_ri
        self._S = S


def TransitionMatrixHalfspace(Kx, epsilon):
    """Returns transition matrix L.

    'Kx' : reduced wavenumber in the x direction, Kx = kx/k0
    'k0' : wavenumber in vacuum, k0 = ω/c

    Sort eigenvectors of the Delta matrix according to propagation
    direction first, then according to $y$ component.

    Returns eigenvectors ordered like (s+,s-,p+,p-)
    """
    Delta = buildDeltaMatrix(Kx, epsilon)

    q, Psi = np.linalg.eig(Delta)

    # Sort according to z propagation direction, highest Re(q) first
    i = np.argsort(-np.real(q))

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
    c[i] = E[i]/nE[i]

    Psi = Psi * c[:, np.newaxis, :]

    # Normalize so that Ey = c1 + c2, analog to Ey = Eis + Ers
    # For an isotropic half-space, this should return the same matrix
    # as IsotropicHalfSpace
    c = Psi[:, 1, 0] + Psi[:, 1, 1]
    np.where(np.abs(c) == 0, 1, c)

    Psi = 2 * Psi / c[:, np.newaxis, np.newaxis]

    return Psi


def TransitionMatrixIsoHalfspace(Kx, epsilon, inv=False):
    """Returns transition matrix L.

    'Kx' : Reduced wavenumber
    'k0' : wavenumber in vacuum
    'inv' : if True, returns inverse transition matrix L^-1

    Returns : transition matrix L
    """
    nx = sqrt(epsilon[:, 0, 0])
    sin_Phi = Kx/nx
    cos_Phi = sqrt(1 - sin_Phi**2)

    if np.shape(Kx) == ():
        i = 1
    else:
        i = np.shape(Kx)[0]

    if inv:
        L = np.tile(np.array([[0, 1, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]], dtype=settings['dtype']), (i, 1, 1))
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
                              [0, 0, 0, 0]], dtype=settings['dtype']), (i, 1, 1))
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

#
# def getPowerTransmissionCorrection(self, Kx, k0):
#     """Returns correction coefficient for power transmission
#
#     The power transmission coefficient is the ratio of the 'z' components
#     of the Poynting vector:       T = P_t_z / P_i_z
#     For isotropic media, we have: T = kb'/kf' |t_bf|^2
#     The correction coefficient is kb'/kf'
#
#     Note : For the moment it is only meaningful for isotropic half spaces.
#     """
#     Kzf = self.frontHalfSpace.get_Kz_from_Kx(Kx, k0)
#     if isinstance(self.backHalfSpace, IsotropicHalfSpace):
#         Kzb = self.backHalfSpace.get_Kz_from_Kx(Kx, k0)
#         return Kzb.real / Kzf.real
#     else:
#         return None
