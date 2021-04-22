# Encoding: utf-8
import numpy as np
import scipy.constants as sc


class Solver:
    '''
    Solver base class to evaluate Experiment objects.
    Here the experiment and structure get unpacked
    and the simulation results get returned.

    The actual simulation is handled by subclasses.
    Because of this, this class should never be called.
    '''

    structure = None
    lbda = None
    theta_i = None
    jonesVector = None
    Kx = None

    data = {}

    def __init__(self, experiment):

        self.permProfile = []
        self.unpackData(experiment)
        self.calculate()
        self.convertResult()

    def calculate(self):
        """Simulates optical Experiment"""
        raise NotImplementedError("Should be implemented in derived classes")

    def unpackData(self, experiment):

        self.structure = experiment.structure
        self.lbda = experiment.lbda
        self.theta_i = experiment.theta_i
        self.jonesVector = experiment.jonesVector

        # Get permitivity profile of the complete structure
        self.permProfile.append(self.structure.frontMaterial.getTensor(self.lbda))

        for L in self.structure.layers:
            self.permProfile.append(L.getPermittivityProfile(self.lbda))

        self.permProfile.append(self.structure.backMaterial.getTensor(self.lbda))

        """Returns the value of Kx.
        As detailed in the documentation, 'Phi' is the angle of the wave
        traveling to the right with respect to the horizontal.
        kx = n k0 sin(Φ) : Real and constant throughout the structure.
                           If n ∈ ℂ, then Φ ∈ ℂ
        Kx = kx/k0 = n sin(Φ) : Reduced wavenumber.
        """
        nx = self.structure.frontMaterial.getRefractiveIndex(self.lbda)[:, 0, 0]
        self.Kx = nx * np.sin(np.deg2rad(self.theta_i))

    def convertResult(self):

        self.R = np.abs(self.T_ri)**2
        self.T = np.abs(self.T_ti)**2  # * self.power_corr

        r_ss = self.T_ri[..., 1, 1]           # Extract 'r_ss'
        S = self.T_ri / r_ss[:, None, None]  # Normalize matrix
        S[..., 0, :] = -S[..., 0, :]  # Change to ellipsometry sign convention

        self.Psi = np.arctan(np.abs(S))*180/sc.pi
        self.Delta = -np.angle(S, deg=True)

        A = np.array([[1,  0,    0,  1],
                      [1,  0,    0, -1],
                      [0,  1,    1,  0],
                      [0,  1j, -1j,  0]])

        Mueller = np.abs(A @ np.einsum('aij,akl->aikjl', S, np.conjugate(S))
                         .reshape(S.shape[0], 4, 4) @ A.T)

        m11 = Mueller[:, 0, 0]
        self.Mueller = Mueller / m11[:, None, None]

        self.data = {
            'T_ri': self.T_ri,
            'T_ti': self.T_ti,
            'Psi': self.Psi,
            'Delta': self.Delta,
            'Mueller': self.Mueller
        }
