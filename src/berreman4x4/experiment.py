# Encoding: utf-8
from .evaluation import Evaluation
from .math import UnitConversion


class Experiment:
    """Description of an experiment.


    """
    structure = None
    jonesVector = None
    theta_i = None
    lbda = None

    def __init__(self, structure=None, jonesVector=None, theta_i=None,
                 lbda=None, unit='nm'):
        """Creates an empty structure.

        'structure' : Structure object
        'jonesVector' : Jones Vector of incident light
        'theta_i' : incident angle in degrees
        'lbda' : single or list of wavelengths
        'unit' : unit to use (default: nm)
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

    def setLbda(self, lbda, unit='nm'):
        """Set experiment wavelengths.

        'lbda' : single or list of wavelengths
        'unit' : unit to use (default: nm)
        """
        self.lbda = lbda * UnitConversion[unit]

    def evaluate(self):
        """Return the Evaluation of the structure for the given parameters"""
        return Evaluation(self)
