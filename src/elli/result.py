# Encoding: utf-8
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt

class Result:
    """Record of a simulation result."""
    experiment = None

    @property
    def rho(self) -> npt.NDArray:
        rho = np.dot(self._s, self.experiment.jones_vector)
        rho = rho[:, 0] / rho[:, 1]
        return rho

    @property
    def psi(self) -> npt.NDArray:
        return np.rad2deg(np.arctan(np.abs(self.rho)))

    @property
    def delta(self) -> npt.NDArray:
        return -np.angle(self.rho, deg=True)

    @property
    def rho_matrix(self) -> npt.NDArray:
        return self._s

    @property
    def psi_matrix(self) -> npt.NDArray:
        return np.rad2deg(np.arctan(np.abs(self.rho_matrix)))

    @property
    def delta_matrix(self) -> npt.NDArray:
        return -np.angle(self.rho_matrix, deg=True)

    @property
    def mueller_matrix(self) -> npt.NDArray:
        a = np.array([[1, 0, 0, 1],
                      [1, 0, 0, -1],
                      [0, 1, 1, 0],
                      [0, 1j, -1j, 0]])

        # Kronecker product of S and S*
        s_kron_s_star = np.einsum('aij,akl->aikjl', np.conjugate(self._s),
                                  self._s).reshape([self._s.shape[0], 4, 4])

        mueller_matrix = np.real(a @ s_kron_s_star @ np.linalg.inv(a))
        mm11 = mueller_matrix[:, 0, 0]

        return mueller_matrix / mm11[:, None, None]

    @property
    def jones_matrix_t(self) -> npt.NDArray:
        return self._jones_matrix_t

    @property
    def jones_matrix_r(self) -> npt.NDArray:
        return self._jones_matrix_r

    @property
    def _s(self) -> npt.NDArray:
        r_ss = self.jones_matrix_r[..., 1, 1]
        return self.jones_matrix_r / r_ss[:, None, None]

    @property
    def jones_matrix_tc(self) -> npt.NDArray:
        c = 1 / sqrt(2) * np.array([[1, 1], [1j, -1j]])
        return np.einsum('ij,...jk,kl->...il', np.linalg.inv(c), self._jones_matrix_t, c)

    @property
    def jones_matrix_rc(self) -> npt.NDArray:
        c = 1 / sqrt(2) * np.array([[1, 1], [1j, -1j]])
        d = 1 / sqrt(2) * np.array([[-1, -1], [1j, -1j]])
        return np.einsum('ij,...jk,kl->...il', np.linalg.inv(d), self._jones_matrix_r, c)

    @property
    def R(self) -> npt.NDArray:
        return np.abs(self._jones_matrix_r) ** 2

    @property
    def T(self) -> npt.NDArray:
        return np.abs(self._jones_matrix_t) ** 2 * self._power_correction[:, None, None]

    @property
    def Rc(self) -> npt.NDArray:
        return np.abs(self.jones_matrix_rc) ** 2

    @property
    def Tc(self) -> npt.NDArray:
        return np.abs(self.jones_matrix_tc) ** 2 * self._power_correction[:, None, None]

    def __init__(self, experiment: "Experiment",
                 jones_matrix_r: npt.NDArray,
                 jones_matrix_t: npt.NDArray,
                 power_correction: npt.NDArray = None) -> None:
        """Creates result object, to store simulation data. Gets called by solvers.

        Args:
            experiment (Experiment): Evalatued experiment, with structure and experimental parameters.
            jones_matrix_r (npt.NDArray): Jones matrix for the reflection direction.
            jones_matrix_t (npt.NDArray): Jones matrix for the transmission direction.
            power_correction (npt.NDArray): Correction factors, to get the power transmission values.
        """
        self.experiment = experiment
        self._jones_matrix_r = jones_matrix_r
        self._jones_matrix_t = jones_matrix_t

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
        if power_correction is None:
            self._power_correction = np.ones_like(self.experiment.lbda)
        else:
            self._power_correction = power_correction
