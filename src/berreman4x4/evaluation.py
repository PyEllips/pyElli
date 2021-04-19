# Encoding: utf-8
import numpy as np
import scipy.constants as sc
from numpy.lib.scimath import sqrt

from .utils import UnitConversion


class Evaluation:
    """Record of a simulation result."""

    structure = None        # Simulated structure
    lbda = None        # Wavelength List for evaluation
    T_ri = None             # Jones matrix for reflection
    T_ti = None             # Jones matrix for transmission
    power_corr = None       # Power correction coefficient for transmission

    Tc_ri = []
    Rc = []
    Tc_ti = []
    Tc = []

    def __init__(self, structure, lbda, phi_i, unit='nm', circular=False):
        """Record the result of the requested simulation for a given list of
        Lambda values and an incidence angle phi_i.

        lbda:       Singular wavelength or np.array of values
        phi_i:      incidence angle of the light (deg)
        unit:       unit of the wavelength (default='nm')
        """

        self.structure = structure
        self.lbda = lbda * UnitConversion[unit]
        self.circular = circular

        k0 = 2 * sc.pi / self.lbda
        Kx = self.structure.frontHalfSpace.get_Kx_from_Phi(phi_i, k0)

        self.T_ri, self.T_ti = structure.getJones(Kx, k0)
        # self.power_corr = structure.getPowerTransmissionCorrection(Kx, k0)
        # Compute additional data...
        self.R = np.abs(self.T_ri)**2
        self.T = np.abs(self.T_ti)**2  # * self.power_corr

        if self.circular:
            self.getCircularJones()

        self.Psi, self.Delta, self.Mueller = self.getEllipsometryParameters(self.T_ri)

    def getCircularJones(self):
        """Return the Jones matrix for the circular polarization basis (L,R)

        The Jones matrices for reflection and transmission (T_ri, T_ti) are
        based on the (p,s) polarization basis. Their shape is [...,2,2].

        The Jones matrices in the (L, R) circular polarizations are
        Tc_ri = D⁻¹ T_ri C   and   Tc_ti = C⁻¹ T_ti C
        """

        # Transformation matrix from the (s,p) basis to the (L,R) basis...
        C = 1 / sqrt(2) * np.array([[1, 1], [1j, -1j]])
        D = 1 / sqrt(2) * np.array([[1, 1], [-1j, 1j]])
        invC = np.linalg.inv(C)
        invD = np.linalg.inv(D)

        for i in range(len(self.T_ri)):
            self.Tc_ri[i] = np.einsum('ij,...jk,kl->...il', invD, self.T_ri[i], C)
            self.Rc[i] = np.abs(self.Tc_ri[i])**2
            self.Tc_ti[i] = np.einsum('ij,...jk,kl->...il', invC, self.T_ti[i], C)
            self.Tc[i] = np.abs(self.Tc_ti[i])**2

    def getEllipsometryParameters(self, J):
        """Calculate the ellipsomerty parameters from Jones matrix 'J'.

        The Jones matrix for reflexion is 'T_ri', with shape [...,2,2].

        Ellipsometry coefficients are defined by the relation
        T_ri / r_ss = [[ tan(Ψ_pp)*exp(-i Δ_pp) , tan(Ψ_ps)*exp(-i Δ_ps) ]
                       [ tan(Ψ_sp)*exp(-i Δ_sp) ,           1            ]]

        The returned arrays are the angles in degrees, in a tuple
           Psi = [[ Ψ_pp, Ψ_ps ]        Delta = [[ Δ_pp, Δ_ps ]
                  [ Ψ_sp, 45°  ]],               [ Δ_sp,  0°  ]].

        Note: Convention for ellipsometry is used.
        See Fujiwara, (4.4), (4.6), (6.14), (6.15)
        """
        r_ss = J[..., 1, 1]           # Extract 'r_ss'
        S = J / r_ss[:, None, None]  # Normalize matrix
        S[..., 0, :] = -S[..., 0, :]  # Change to ellipsometry sign convention

        Psi = np.arctan(np.abs(S))*180/sc.pi
        Delta = -np.angle(S, deg=True)

        A = np.array([[1,  0,    0,  1],
                      [1,  0,    0, -1],
                      [0,  1,    1,  0],
                      [0,  1j, -1j,  0]])

        Mueller = np.abs(A @ np.einsum('aij,akl->aikjl', S, np.conjugate(S))
                         .reshape(S.shape[0], 4, 4) @ A.T)

        m11 = Mueller[:, 0, 0]
        Mueller = Mueller / m11[:, None, None]

        return Psi, Delta, Mueller

    def get(self, name):
        """Return the data for the requested coefficient 'name'.

        Examples for 'name'...
        'r_sp' : Amplitude reflection coefficient from 's' to 'p' polarization.
        'r_LR' : Reflection from circular right to circular left polarization.
        'T_pp' : Power transmission coefficient from 'p' to 'p' polarization.
        'Ψ_ps', 'Δ_pp' : Ellipsometry parameters.

        Note : 'Ψ', 'Δ' are shortcuts for 'Ψ_pp' and 'Δ_pp', which are the only
        non zero parameters for samples with isotropic layers.

        For more information about the definition of the...
        * ellipsomtery parameters see getEllipsometryParameters()
        * circular polarization, see getCircularJones()

        Returns : array of values
        """
        param = name[0]

        # Read the requested indices...
        (i, j) = map(self._polarIndex, name[2:4]) if len(name) > 1 else (0, 0)

        # Select the requested array...
        if param == 'r':
            M = self.Tc_ri if self.circular else self.T_ri
        elif param == 't':
            M = self.Tc_ti if self.circular else self.T_ti
        elif param == 'R':
            M = self.Rc if self.circular else self.R
        elif param == 'T':
            M = self.Tc if self.circular else self.T
        elif param == 'Ψ' or param == 'psi':
            M = self.Psi
        elif param == 'Δ' or param == 'delta':
            M = self.Delta

        # Return the requested data...
        return M[..., i, j]

    def _polarIndex(self, char):
        """Return polarization index for character 'char'.

        Returned value : 'p', 'L' -> 0
                         's', 'R' -> 1
        """
        if char in ['p', 'L']:
            return 0
        elif char in ['s', 'R']:
            return 1
