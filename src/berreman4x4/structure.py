# Encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.scimath import sqrt

from .half_spaces import IsotropicHalfSpace
from .evaluation import Evaluation

e_x = np.array([1, 0, 0]).reshape((3,))  # base vectors
e_y = np.array([0, 1, 0]).reshape((3,))
e_z = np.array([0, 0, 1]).reshape((3,))

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

    def getPermittivityProfile(self, lbda, unit='m'):
        """Returns permittivity tensor profile."""
        layers = sum([L.getPermittivityProfile(lbda, unit) for L in self.layers], [])
        front = (float('inf'), self.frontHalfSpace.material.getTensor(lbda, unit))
        back = (float('inf'), self.backHalfSpace.material.getTensor(lbda, unit))
        return sum([[front], layers, [back]], [])

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

    def getIndexProfile(self, lbda, unit='m', v=e_x):
        """Returns refractive index profile.

        'v' : Unit vector, direction of evaluation of the refraction index.
              Default value is v = e_x.
        """
        profile = self.getPermittivityProfile(lbda, unit)
        (h, epsilon) = list(zip(*profile))  # unzip
        n = [sqrt((v.T * eps * v)[0, 0, 0]) for eps in epsilon]
        return list(zip(h, n))

    def drawStructure(self, lbda=1000, unit='nm', method="graph", margin=0.15):
        """Draw the structure.

        'method' : 'graph' or 'section'
        Returns : Axes object
        """
        # Build index profile
        profile = self.getIndexProfile(lbda, unit)
        (h, n) = list(zip(*profile))     # unzip
        n = np.array(n)
        z_layers = np.hstack((0., np.cumsum(h[1:-1])))
        z_max = z_layers[-1]
        if z_max != 0.:
            z_margin = margin * z_max
        else:
            z_margin = 1e-6
        z = np.hstack((-z_margin, z_layers, z_max + z_margin))
        # Call specialized methods
        if method == "graph":
            ax = self._drawStructureGraph(z, n, unit)
        elif method == "section":
            ax = self._drawStructureSection(z, n, unit)
        else:
            ax = None
        return ax

    def _drawStructureGraph(self, z, n, unit):
        """Draw a graph of the refractive index profile """
        n = np.hstack((n, n[-1]))
        # Draw the graph
        fig = plt.figure(figsize=(8, 3))
        ax = fig.add_subplot(1, 1, 1)
        fig.subplots_adjust(bottom=0.17)
        ax.step(z, n.real, 'black', where='post')
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xlabel("z ({})".format(unit))
        ax.set_ylabel("n'")
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0, 0))
        ax.set_xlim(z.min(), z.max())
        ax.set_ylim(bottom=1.0)
        return ax

    def _drawStructureSection(self, z, n, unit):
        """Draw a cross section of the structure"""
        # Prepare arrays for pcolormesh()
        X = z * np.ones((2, 1))
        Y = np.array([0, 1]).reshape((2, 1)) * np.ones_like(z)
        n = np.array(n).reshape((1, -1)).real
        # Draw the cross section
        fig = plt.figure(figsize=(8, 3))
        ax = fig.add_subplot(1, 1, 1)
        fig.subplots_adjust(left=0.05, bottom=0.15)
        ax.set_yticks([])
        ax.set_xlabel("z ({})".format(unit))
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0, 0))
        ax.set_xlim(z.min(), z.max())
        stack = ax.pcolormesh(X, Y, n, cmap=plt.get_cmap('gray_r'))
        colbar = fig.colorbar(stack, orientation='vertical', anchor=(1.2, 0.5),
                              fraction=0.05)
        colbar.ax.set_xlabel("n'", position=(3, 0))
        return ax

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