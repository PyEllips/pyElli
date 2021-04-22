# Encoding: utf-8

from .solverExpm import SolverExpm


class Result:
    """Record of a simulation result."""

    experiment = None       # Simulated experiment
    solver = None
    data = None

    def __init__(self, experiment, solver=SolverExpm):
        """

        """
        self.experiment = experiment
#        self.solver = solver

        result = solver(self.experiment)

        self.data = result.data

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
