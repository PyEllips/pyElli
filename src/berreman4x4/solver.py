# Encoding: utf-8
from abc import ABC, abstractmethod

from .result import Result


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
    def calculate(self) -> Result:
        pass

    def __init__(self, experiment: "Experiment"):
        self.structure = experiment.structure
        self.lbda = experiment.lbda
        self.theta_i = experiment.theta_i
        self.jonesVector = experiment.jonesVector
        self.permProfile = self.structure.getPermittivityProfile(self.lbda)
