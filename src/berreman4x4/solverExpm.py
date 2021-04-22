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

    def calculate(self):
        """Simulates optical Experiment"""

        layers = reversed(self.permProfile[1:-1])

        ILf = TransitionMatrixIsoHalfspace(self.Kx, self.permProfile[0], inv=True)
        P = [hs_propagator_Pade(buildDeltaMatrix(self.Kx, epsilon), -d, self.lbda)
             for d, epsilon in layers]
        Lb = TransitionMatrixHalfspace(self.Kx, self.permProfile[-1])

        T = ILf
        for p in P:
            T = T @ p
        T = T @ Lb

        # Extraction of T_it out of T. "2::-2" means integers {2,0}.
        T_it = T[:, 2::-2, 2::-2]
        # Calculate the inverse and make sure it is a matrix.
        T_ti = np.linalg.inv(T_it)

        # Extraction of T_rt out of T. "3::-2" means integers {3,1}.
        T_rt = T[:, 3::-2, 2::-2]

        # Then we have T_ri = T_rt * T_ti
        T_ri = T_rt @ T_ti

        self.T_ti = T_ti
        self.T_ri = T_ri


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
