# Encoding: utf-8


class Result:
    """Record of a simulation result."""

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
    def rhoMat(self):
        return self.__result.rhoMat

    @property
    def psiMat(self):
        return self.__result.psiMat

    @property
    def deltaMat(self):
        return self.__result.deltaMat

    @property
    def mueller_matrix(self):
        return self.__result.mueller_matrix

    @property
    def jones_matrix_r(self):
        return self.__result.jones_matrix_r

    @property
    def jones_matrix_t(self):
        return self.__result.jones_matrix_t

    @property
    def R(self):
        return self.__result.R

    @property
    def T(self):
        return self.__result.T

    def __init__(self, solver):
        """

        """
        self.__result = solver

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
