# Encoding: utf-8
import numpy as np
from numpy.lib.scimath import arcsin

from .solver import Solver

class SolverExpm(Solver):
    '''
    Solver class to evaluate Experiment objects.
    Based on Berreman's 4x4 method.
    '''
    _rtots = None
    _ttots = None
    _rtotp = None
    _ttotp = None

    @property
    def psi(self):
        if not all((self._rtotp, self._rtots)):
            return None
        return np.arctan(np.abs(self._rtotp / self._rtots))

    @property
    def rho(self):
        if not all((self._rtotp, self._rtots)):
            return None
        return self._rtotp / self._rtots

    @property
    def delta(self):
        if not all((self._rtotp, self._rtots)):
            return None
        return np.angle(-self._rtotp / self._rtots)

    @property
    def mueller_matrix(self):
        return None

    @property
    def jones_matrix_t(self):
        return None

    @property
    def jones_matrix_r(self):
        return None
        
    def calculate(self):
        """Simulates optical Experiment"""
        pass
