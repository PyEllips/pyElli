# Encoding: utf-8
import numpy as np

from .evaluation import Evaluation
from .experiment import Experiment


class Structure:
    """Description of the whole structure.

    * front half-space (incident), must be isotropic
    * back half-space (exit), may be anisotropic
    * layer succession
    """
    frontHalfSpace = None
    backHalfSpace = None
    layers = []  # list of layers

    def __init__(self, front=None, layers=None, back=None):
        """Creates an empty structure.

        'front' : front half space, see setFrontHalfSpace()
        'layers' : layer list, see setLayers()
        'back' : back half space, see setBackHalfSpace()
        """
        self.setFrontHalfSpace(front)
        self.setLayers(layers)
        self.setBackHalfSpace(back)

    def setFrontHalfSpace(self, halfSpace):
        """Defines the front half-space material.

        'material' : Material object
        """
        self.frontHalfSpace = halfSpace

    def setBackHalfSpace(self, halfSpace):
        """Defines the back half-space material.

        'material' : Material object
        """
        self.backHalfSpace = halfSpace

    def setLayers(self, layers):
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def evaluate(self, lbda, theta_i, unit='nm'):
        """Return the Evaluation of the structure for the given parameters"""
        return Evaluation(Experiment(self, None, theta_i, lbda, unit))
