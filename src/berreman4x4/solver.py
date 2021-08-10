# Encoding: utf-8
from abc import ABC, abstractmethod
import numpy as np

from .experiment import Experiment


class Solver(ABC):
    """
    Solver base class to evaluate Experiment objects.
    Here the experiment and structure get unpacked
    and the simulation results get returned.

    The actual simulation is handled by subclasses.
    Because of this, this class should never be called.
    """

    structure = None
    lbda = None
    theta_i = None
    jonesVector = None
    Kx = None
    permProfile = None

    @property
    @abstractmethod
    def psi(self):
        pass

    @property
    @abstractmethod
    def delta(self):
        pass

    @property
    @abstractmethod
    def mueller_matrix(self):
        pass

    @property
    @abstractmethod
    def jones_matrix_t(self):
        pass

    @property
    @abstractmethod
    def jones_matrix_r(self):
        pass

    @property
    def data(self):
        return {
            'T_ri': self.jones_matrix_r,
            'T_ti': self.jones_matrix_t,
            'Psi': self.psi,
            'Delta': self.delta,
            'Mueller': self.mueller_matrix
        }

    @abstractmethod
    def calculate(self):
        pass

    def __init__(self, experiment: Experiment):
        self.permProfile = []
        self.unpackData(experiment)
        self.calculate()

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

        # Returns the value of Kx.
        # As detailed in the documentation, 'Phi' is the angle of the wave
        # traveling to the right with respect to the horizontal.
        # kx = n k0 sin(Φ) : Real and constant throughout the structure.
        #                   If n ∈ ℂ, then Φ ∈ ℂ
        # Kx = kx/k0 = n sin(Φ) : Reduced wavenumber.
        nx = self.structure.frontMaterial.getRefractiveIndex(self.lbda)[:, 0, 0]
        self.Kx = nx * np.sin(np.deg2rad(self.theta_i))
