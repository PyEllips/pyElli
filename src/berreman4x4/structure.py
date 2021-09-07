# Encoding: utf-8
import numpy as np

from .experiment import Experiment
from .solver4x4 import Solver4x4


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

    def __init__(self, frontMaterial=None, layers=None, backMaterial=None):
        """Creates an structure consisting of a semiinfinit frontmaterial,
        an optional list of finite layers and a semiinfinit material in the back.

        'front' : front half space material
        'layers' : List of layers
        'back' : back half space material
        """
        self.frontMaterial = frontMaterial
        self.backMaterial = backMaterial
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
        exp = Experiment(self, lbda, theta_i, [1, 0, 1, 0])
        return exp.evaluate(Solver4x4())


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

    reps = None        # Number of repetitions
    before = None   # additionnal layers before the first period
    after = None    # additionnal layers after the last period
    layers = None   # layers to repeat

    def __init__(self, layers=None, reps=2, before=0, after=0):
        """Repeated structure of layers

        'layers' : list of the repeated layers
        'reps' : number of repetitions
        'before' : number of additionnal layers before the first period
        'after' : number of additionnal layers after the last period

        Example : For layers [1,2,3] with n=2, before=1 and after=0, the
        structure will be 3123123.
        """
        self.reps = reps
        self.before = before
        self.after = after
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
        return before + self.reps * layers + layers[:self.after]


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
