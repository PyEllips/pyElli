# Encoding: utf-8
from .materials import Material
import numpy as np
from typing import List

from .experiment import Experiment


#########################################################
# Layer Class...

class Layer:
    """Homogeneous layer finite of dielectric material."""

    material = None     # Material making the layer
    d = None            # Thickness of the layer

    def __init__(self, material, d):
        """New layer of material 'material', with thickness 'd'

        'material' : Material object
        'd'        : Thickness of layer in nm or tuple (thickness, unit)
        """
        self.setMaterial(material)
        self.setThickness(d)

    def setMaterial(self, material: Material):
        """Defines the material for this layer. """
        self.material = material

    def setThickness(self, d):
        """Defines the thickness of this homogeneous layer in nm."""
        self.d = d

    def getPermittivityProfile(self, lbda):
        """Returns permittivity tensor profile.

        Returns a list containing one tuple: [(d, epsilon)]
        """
        return [(self.d, self.material.getTensor(lbda))]


#########################################################
# Repeated layers...

class RepeatedLayers(Layer):
    """Repetition of a structure."""

    n = None        # Number of repetitions
    before = None   # additional layers before the first period
    after = None    # additional layers after the last period
    layers = None   # layers to repeat

    def __init__(self, layers: List[Layer], n: int = 2, before: int = 0, after: int = 0):
        """Repeated structure of layers

        'layers' : list of the repeated layers
        'n' : number of repetitions
        'before', 'after' : see method setRepetition()
        """
        self.setRepetition(n, before, after)
        self.setLayers(layers)

    def setRepetition(self, n: int, before: int = 0, after: int = 0):
        """Defines the number of repetitions.

        'n' : number of repetitions
        'before' : number of additional layers before the first period
        'after' : number of additional layers after the last period

        Example : For layers [1,2,3] with n=2, before=1 and after=0, the
        structure will be 3123123.
        """
        self.n = n
        self.before = before
        self.after = after

    def setLayers(self, layers: List[Layer]):
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPermittivityProfile(self, lbda):
        """Returns permittivity tensor profile.

        Returns list of tuples [(d1, epsilon1), (d2, epsilon2), ... ]
        """
        layers = [L.getPermittivityProfile(lbda)[0] for L in self.layers]

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
        Returns list [(d1, epsilon1), (d2, epsilon2), ... ]
        """
        z = self.material.getSlices()
        h = np.diff(z)
        zmid = (z[:-1] + z[1:]) / 2.
        tensor = [self.material.getTensor(z, lbda) for z in zmid]
        return list(zip(h, tensor))


#########################################################
# Structure Class...

class Structure:
    """Description of the whole structure.

    * front half-space (incident), must be isotropic
    * back half-space (exit), may be anisotropic
    * layer succession
    """
    frontMaterial = None
    backMaterial = None
    layers = []  # list of layers

    def __init__(self, front: Material, layers: List[Layer], back: Material):
        """Creates an empty structure.

        'front' : front half space, see setFrontHalfSpace()
        'layers' : layer list, see setLayers()
        'back' : back half space, see setBackHalfSpace()
        """
        self.setFrontMaterial(front)
        self.setLayers(layers)
        self.setBackMaterial(back)

    def setFrontMaterial(self, material: Material):
        """Defines the front half-space material.

        'material' : Material object
        """
        self.frontMaterial = material

    def setBackMaterial(self, material: Material):
        """Defines the back half-space material.

        'material' : Material object
        """
        self.backMaterial = material

    def setLayers(self, layers: List[Layer]):
        """Set list of layers.

        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPermittivityProfile(self, lbda):
        """Get permitivity profile of the complete structure for the wavelenghts lbda.
        """
        permProfile = []
        permProfile.append(self.frontMaterial.getTensor(lbda))

        for L in self.layers:
            permProfile.append(L.getPermittivityProfile(lbda))

        permProfile.append(self.backMaterial.getTensor(lbda))
        return permProfile

    def evaluate(self, lbda, theta_i, vector=[1, 0, 1, 0]):
        """Return the Evaluation of the structure for the given parameters"""
        exp = Experiment(self, lbda, theta_i, vector)
        return exp.evaluate()
