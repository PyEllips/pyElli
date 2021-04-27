# Encoding: utf-8
from .math import unitConversion
from .result import Result
from .settings import settings
from .solverExpm import SolverExpm
from .solver2x2 import Solver2x2


class Experiment:
    """Description of an experiment.


    """
    structure = None
    jonesVector = None
    theta_i = None
    lbda = None

    def __init__(self, structure=None, lbda=None, theta_i=None, jonesVector=None):
        """Creates an empty structure.

        'structure' : Structure object
        'lbda' : single or list of wavelengths in nm or tuple (wavelength, unit)
        'theta_i' : incident angle in degrees
        'jonesVector' : Jones Vector of incident light
        """
        self.setStructure(structure)
        self.setJonesVector(jonesVector)
        self.setTheta(theta_i)
        self.setLbda(lbda)

    def setStructure(self, structure):
        """Defines the Structure.

        'structure' : Structure object
        """
        self.structure = structure

    def setJonesVector(self, jonesVector):
        """Defines the Jones Vector of the incident Light.

        None : unpolarized light
        [1, 0]: horizontal polarized
        [0, 1]: vertical polarized
        1/sqrt(2)*[1, 1]: diagonal polarized
        1/sqrt(2)*[1,-1]: anti-diagonal polarized
        """
        self.jonesVector = jonesVector

    def setTheta(self, theta_i):
        """Set incident angle, or list of angles to evaluate.

        'theta_i' : incident angle in degrees
        """
        self.theta_i = theta_i

    def setLbda(self, lbda):
        """Set experiment wavelengths.

        'lbda' : single or list of wavelengths in nm or tuple (wavelength, unit)
        """
        self.lbda = (unitConversion(lbda), 'm')

    def evaluate(self, solver='default'):
        """Return the Evaluation of the structure for the given parameters"""
        if solver == 'default' and 'solver' in settings:
            solver = settings['solver']

        solvers = ['berreman4x4', 'simple2x2']
        if solver not in solvers:
            raise ValueError("Invalid solver type {:}. Expected one of: {:}"
                             .format(solver, solvers))

        if solver == 'berreman4x4':
            return Result(self, SolverExpm(self.__experiment))
        elif solver == 'simple2x2':
            return Result(self, Solver2x2(self.__experiment))
