# Encoding: utf-8
import numpy as np

from .evaluation import Evaluation
from .experiment import Experiment
from .math import unitConversion


#########################################################
# Structure Class...

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

    def evaluate(self, lbda, theta_i):
        """Return the Evaluation of the structure for the given parameters"""
        return Evaluation(Experiment(self, lbda, theta_i, None))


#########################################################
# Layer Class...

class Layer:
    """Homogeneous layer finite of dielectric material."""

    material = None     # Material making the layer
    h = None            # Thickness of the layer

    def __init__(self, material, h):
        """New layer of material 'material', with thickness 'h'

        'material' : Material object
        'h'        : Thickness of layer in nm or tuple (thickness, unit)
        """
        self.setMaterial(material)
        self.setThickness(h)

    def setMaterial(self, material):
        """Defines the material for this layer. """
        self.material = material

    def setThickness(self, h):
        """Defines the thickness of this homogeneous layer."""
        self.h = unitConversion(h)

    def getPermittivityProfile(self, lbda):
        """Returns permittivity tensor profile.

        Returns a list containing one tuple: [(h, epsilon)]
        """
        return [(self.h, self.material.getTensor(lbda))]


#########################################################
# Repeated layers...

class RepeatedLayers(Layer):
    """Repetition of a structure."""

    n = None        # Number of repetitions
    before = None   # additionnal layers before the first period
    after = None    # additionnal layers after the last period
    layers = None   # layers to repeat

    def __init__(self, layers=None, n=2, before=0, after=0):
        """Repeated structure of layers

        'layers' : list of the repeated layers
        'n' : number of repetitions
        'before', 'after' : see method setRepetition()
        """
        self.setRepetition(n, before, after)
        self.setLayers(layers)

    def setRepetition(self, n,  before=0, after=0):
        """Defines the number of repetitions.

        'n' : number of repetitions
        'before' : number of additionnal layers before the first period
        'after' : number of additionnal layers after the last period

        Example : For layers [1,2,3] with n=2, before=1 and after=0, the
        structure will be 3123123.
        """
        self.n = n
        self.before = before
        self.after = after

    def setLayers(self, layers):
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPermittivityProfile(self, lbda):
        """Returns permittivity tensor profile.

        Returns list of tuples [(h1, epsilon1), (h2, epsilon2), ... ]
        """
        layers = sum([L.getPermittivityProfile(lbda) for L in self.layers], [])
        if self.before > 0:
            before = layers[-self.before:]
        else:
            before = []
        return before + self.n * layers + layers[:self.after]


#########################################################
# Inhomogeneous layers...

class InhomogeneousLayer(Layer):
    """Inhomogeneous layer.

    Must be fabricated with an InhomogemeousMaterial object.
    """

    def getPermittivityProfile(self, lbda):
        """Returns permittivity tensor profile.

        Tensor is evaluated in the middle of each slice.
        Returns list [(h1, epsilon1), (h2, epsilon2), ... ]
        """
        z = self.material.getSlices()
        h = np.diff(z)
        zmid = (z[:-1] + z[1:]) / 2.
        tensor = [self.material.getTensor(z, lbda) for z in zmid]
        return list(zip(h, tensor))
