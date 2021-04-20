# Encoding: utf-8
import numpy as np

from .evaluation import Evaluation
from .half_spaces import IsotropicHalfSpace


class Structure:
    """Description of the whole structure.

    * front half-space (incident), must be isotropic
    * back half-space (exit), may be anisotropic
    * layer succession
    """
    frontHalfSpace = None
    backHalfSpace = None
    layers = None  # list of layers

    def __init__(self, front=None, layers=None, back=None):
        """Creates an empty structure.

        'front' : front half space, see setFrontHalfSpace()
        'layers' : layer list, see setLayers()
        'back' : back half space, see setBackHalfSpace()
        """
        self.layers = []  # list of layers
        if front is not None:
            self.setFrontHalfSpace(front)
        if layers is not None:
            self.setLayers(layers)
        if back is not None:
            self.setBackHalfSpace(back)

    def setFrontHalfSpace(self, halfSpace):
        """Defines the front half-space.

        'halfSpace' : HalfSpace object
        """
        self.frontHalfSpace = halfSpace

    def setBackHalfSpace(self, halfSpace):
        """Defines the back half-space.

        'halfSpace' : HalfSpace object
        """
        self.backHalfSpace = halfSpace

    def setLayers(self, layers):
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPropagationMatrix(self, Kx, k0, inv=False):
        """Gives the propagation matrix of the structure.

        'Kx' : reduced wavenumber along x
        'k0' : wavenumber in vacuum
        'inv' : returns propagation matrix for decreasing z

        Returns : propagation matrix P(zb,zf) for the full structure

        Psi(zb) = P_(zb, z_{N-1}) * ... * P(z1,zf) * Psi(zf)
                = P(zb,zf) * Psi(zf)
        """
        if inv:
            layers = reversed(self.layers)
        else:
            layers = self.layers
        P_tot = np.identity(4)
        # Cumulative products :
        for L in layers:
            P = L.getPropagationMatrix(Kx, k0, inv)
            P_tot = P @ P_tot
        return P_tot

    def getStructureMatrix(self, Kx, k0):
        """Returns the transfer matrix T of the structure.

        [Eis, Ers, Eip, Erp].T = T * [c1, c2, c3, c4].T
        T = Lf^-1 * P(zf,zb) * Lb
        """
        ILf = self.frontHalfSpace.getTransitionMatrix(Kx, k0, inv=True)
        P = self.getPropagationMatrix(Kx, k0, inv=True)
        Lb = self.backHalfSpace.getTransitionMatrix(Kx, k0)
        T = ILf @ P @ Lb
        return T

    def getJones(self, Kx, k0):
        """Returns the Jones matrices.

        Returns : tuple (T_ri, T_ti)

        T_ri is the Jones matrix for reflexion : [[r_pp, r_ps],
                                                  [r_sp, r_ss]]

        T_ti is the Jones matrix for transmission : [[t_pp, t_ps],
                                                     [t_sp, t_ss]]

        Naming convention (Fujiwara, p. 220):
        't_ps' : transmitted 'p' component for an 's' incident wave
        't_ss' : transmitted 's' component for an 's' incident wave
        ...

        Note: If all materials are isotropic, r_ps = r_sp = t_sp = t_ps = 0

        See also:
        * extractCoefficient() to extract the desired coefficients.
        * circularJones() for circular polarization basis
        """
        T = self.getStructureMatrix(Kx, k0)
        # Extraction of T_it out of T. "2::-2" means integers {2,0}.
        T_it = T[:, 2::-2, 2::-2]
        # Calculate the inverse and make sure it is a matrix.
        T_ti = np.linalg.inv(T_it)

        # Extraction of T_rt out of T. "3::-2" means integers {3,1}.
        T_rt = T[:, 3::-2, 2::-2]

        # Then we have T_ri = T_rt * T_ti
        T_ri = T_rt @ T_ti
        return T_ri, T_ti

    def getPowerTransmissionCorrection(self, Kx, k0):
        """Returns correction coefficient for power transmission

        The power transmission coefficient is the ratio of the 'z' components
        of the Poynting vector:       T = P_t_z / P_i_z
        For isotropic media, we have: T = kb'/kf' |t_bf|^2
        The correction coefficient is kb'/kf'

        Note : For the moment it is only meaningful for isotropic half spaces.
        """
        Kzf = self.frontHalfSpace.get_Kz_from_Kx(Kx, k0)
        if isinstance(self.backHalfSpace, IsotropicHalfSpace):
            Kzb = self.backHalfSpace.get_Kz_from_Kx(Kx, k0)
            return Kzb.real / Kzf.real
        else:
            return None

    def evaluate(self, lbda, theta_i, unit='nm'):
        """Return the Evaluation of the structure for the given parameters"""
        return Evaluation(self, lbda, theta_i, unit)
