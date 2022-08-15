# Encoding: utf-8
r"""The experiment class defines the external conditions of the sample.

It requires a Structure to evaluate and includes the information about
the incident light beam:

* the wavelengths :math:`\lambda`
* the incidence angle :math:`\theta_\text{i}`
* and the polarization, which can be given by a Jones or Stokes vector

The evaluate method can be called, to start the calculation of the optical properties.
To choose a Solver to be used in the calculation, the solver class is provided
as an argument and an object will be created automatically.

The experiment class is only needed in special cases an can be skipped by calling
:meth:`elli.structure.Structure.evaluate`.
"""
import numpy as np
import numpy.typing as npt

from .result import Result
from .solver import Solver
from .solver4x4 import Solver4x4


class Experiment:
    """Description of a virtual experiment to simulate the behavior of a structure."""

    structure = None
    jones_vector = None
    stokes_vector = None
    theta_i = None
    lbda = None

    def __init__(
        self,
        structure: "Structure",
        lbda: npt.ArrayLike,
        theta_i: float,
        vector: npt.ArrayLike = None,
    ) -> None:
        """Creates a virtual experiment to simulate the behavior of a structure.

        Args:
            structure (Structure): Structure object to evaluate.
            lbda (npt.ArrayLike): Single value or array of wavelengths (in nm).
            theta_i (float): Incident angle (in degrees).
            vector (npt.ArrayLike, optional):
                Jones or Stokes vector of incident light. Defaults to diagonal polarization ([1, 0, 1, 0]).
        """
        self.set_structure(structure)
        self.set_theta(theta_i)
        self.set_lbda(lbda)
        self.set_vector(vector)

    def set_structure(self, structure: "Structure") -> None:
        """Defines the Structure to evaluate.

        Args:
            structure (Structure): Structure object to evaluate.
        """
        self.structure = structure

    def set_vector(self, vector: npt.ArrayLike) -> None:
        """Defines the Jones or Stokes vector of the incident Light.

        Jones:
        [1, 0]: horizontal polarized
        [0, 1]: vertical polarized
        [1/sqrt(2), 1/sqrt(2)]: diagonal polarized
        [1/sqrt(2),-1/sqrt(2)]: anti-diagonal polarized

        Stokes:
        [1,0,0,0]: unpolarized light
        [1,1,0,0]: horizontal polarized
        [1,-1,0,0]: vertical polarized
        [1,0,1,0]: diagonal polarized
        [1,0,-1,0]: anti-diagonal polarized

        Args:
            vector (npt.ArrayLike): Jones or Stokes vector of incident light.
        """
        if vector is None:
            vector = [1, 0, 1, 0]

        vector = np.asarray(vector)

        if vector.shape == (2,):
            self.jones_vector = vector

            self.stokes_vector = np.array(
                [
                    np.abs(self.jones_vector[0]) ** 2
                    + np.abs(self.jones_vector[1]) ** 2,
                    np.abs(self.jones_vector[0]) ** 2
                    - np.abs(self.jones_vector[1]) ** 2,
                    2
                    * np.real(
                        self.jones_vector[0] * np.conjugate(self.jones_vector[1])
                    ),
                    -2
                    * np.imag(
                        self.jones_vector[0] * np.conjugate(self.jones_vector[1])
                    ),
                ]
            )

        elif vector.shape == (4,):
            self.stokes_vector = vector

            p = (
                np.sqrt(
                    self.stokes_vector[1] ** 2
                    + self.stokes_vector[2] ** 2
                    + self.stokes_vector[3] ** 2
                )
                / self.stokes_vector[0]
            )
            Q = self.stokes_vector[1] / (self.stokes_vector[0] * p)
            U = self.stokes_vector[2] / (self.stokes_vector[0] * p)
            V = self.stokes_vector[3] / (self.stokes_vector[0] * p)

            if Q == -1:
                a = 0
                b = 1
            else:
                a = np.sqrt((1 + Q) / 2)
                b = U / (2 * a) - 1j * V / (2 * a)

            self.jones_vector = np.array([a, b])

    def set_theta(self, theta_i: float) -> None:
        """Set incident angle to evaluate.

        Args:
            theta_i (float): Incident angle (in degrees).
        """
        self.theta_i = theta_i

    def set_lbda(self, lbda: npt.ArrayLike) -> None:
        """Set experiment wavelengths.

        Args:
            lbda (npt.ArrayLike): single value or array of wavelengths (in nm).
        """
        lbda_array = np.asarray(lbda)
        if np.shape(lbda_array) == ():
            lbda_array = np.asarray([lbda])
        self.lbda = lbda_array

    def evaluate(self, solver: Solver = Solver4x4, **solver_kwargs) -> Result:
        """Evaluates the experiment with the given solver.

        Args:
            solver (Solver, optional): Choose which solver class is used. Defaults to Solver4x4.
            solver_kwargs (optional): Keyword arguments for the Solver can be appended as arguments.

        Returns:
            Result: Result of the experiment.
        """
        solv = solver(self, **solver_kwargs)
        return solv.calculate()
