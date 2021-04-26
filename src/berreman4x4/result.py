# Encoding: utf-8
from .solverExpm import SolverExpm
from .solver2x2 import Solver2x2
from .settings import settings

class Result:
    """Record of a simulation result."""

    __experiment = None       # Simulated experiment
    __result = None

    @property
    def psi(self):
        return self.__result.psi

    @property
    def delta(self):
        return self.__result.delta

    @property
    def rho(self):
        return self.__result.rho

    @property
    def mueller_matrix(self):
        return self.__result.mueller_matrix

    @property
    def jones_matrix_r(self):
        return self.__result.jones_matrix_r

    @property
    def jones_matrix_t(self):
        return self.__result.jones_matrix_t

    def __init__(self, experiment, solver='default'):
        """

        """
        self.__experiment = experiment

        if solver == 'default' and 'solver' in settings:
            solver = settings['solver']

        solvers = ['berreman4x4', 'simple2x2']
        if solver not in solvers:
            raise ValueError("Invalid solver type {:}. Expected one of: {:}"
                             .format(solver, solvers))

        if solver == 'berreman4x4':
            self.__result = SolverExpm(self.__experiment)
        elif solver == 'simple2x2':
            self.__result = Solver2x2(self.__experiment)

    # def get(self, name):
    #     """Return the data for the requested coefficient 'name'.
    #
    #     Examples for 'name'...
    #     'r_sp' : Amplitude reflection coefficient from 's' to 'p' polarization.
    #     'r_LR' : Reflection from circular right to circular left polarization.
    #     'T_pp' : Power transmission coefficient from 'p' to 'p' polarization.
    #     'Ψ_ps', 'Δ_pp' : Ellipsometry parameters.
    #
    #     Note : 'Ψ', 'Δ' are shortcuts for 'Ψ_pp' and 'Δ_pp', which are the only
    #     non zero parameters for samples with isotropic layers.
    #
    #     For more information about the definition of the...
    #     * ellipsomtery parameters see getEllipsometryParameters()
    #     * circular polarization, see getCircularJones()
    #
    #     Returns : array of values
    #     """
    #     param = name[0]
    #
    #     # Read the requested indices...
    #     (i, j) = map(self._polarIndex, name[2:4]) if len(name) > 1 else (0, 0)
    #
    #     # Select the requested array...
    #     if param == 'r':
    #         M = self.Tc_ri if self.circular else self.T_ri
    #     elif param == 't':
    #         M = self.Tc_ti if self.circular else self.T_ti
    #     elif param == 'R':
    #         M = self.Rc if self.circular else self.R
    #     elif param == 'T':
    #         M = self.Tc if self.circular else self.T
    #     elif param == 'Ψ' or param == 'psi':
    #         M = self.Psi
    #     elif param == 'Δ' or param == 'delta':
    #         M = self.Delta
    #
    #     # Return the requested data...
    #     return M[..., i, j]
    #
    # def _polarIndex(self, char):
    #     """Return polarization index for character 'char'.
    #
    #     Returned value : 'p', 'L' -> 0
    #                      's', 'R' -> 1
    #     """
    #     if char in ['p', 'L']:
    #         return 0
    #     elif char in ['s', 'R']:
    #         return 1
