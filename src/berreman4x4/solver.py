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
    def rho(self):
        raise ValueError('Value not calculated by solver')

    @property
    def psi(self):
        raise ValueError('Value not calculated by solver')

    @property
    def delta(self):
        raise ValueError('Value not calculated by solver')

    @property
    def rhoMat(self):
        raise ValueError('Value not calculated by solver')

    @property
    def psiMat(self):
        raise ValueError('Value not calculated by solver')

    @property
    def deltaMat(self):
        raise ValueError('Value not calculated by solver')

    @property
    def mueller_matrix(self):
        raise ValueError('Value not calculated by solver')

    @property
    def jones_matrix_t(self):
        raise ValueError('Value not calculated by solver')

    @property
    def jones_matrix_r(self):
        raise ValueError('Value not calculated by solver')

    @property
    def jones_matrix_tc(self):
        raise ValueError('Value not calculated by solver')

    @property
    def jones_matrix_rc(self):
        raise ValueError('Value not calculated by solver')

    @property
    def R(self):
        raise ValueError('Value not calculated by solver')

    @property
    def T(self):
        raise ValueError('Value not calculated by solver')

    @property
    def Rc(self):
        raise ValueError('Value not calculated by solver')

    @property
    def Tc(self):
        raise ValueError('Value not calculated by solver')

    @abstractmethod
    def calculate(self) -> Result:
        pass

    def __init__(self, experiment: "Experiment") -> None:
        self.structure = experiment.structure
        self.lbda = experiment.lbda
        self.theta_i = experiment.theta_i
        self.jonesVector = experiment.jonesVector
        self.permProfile = self.structure.getPermittivityProfile(self.lbda)
