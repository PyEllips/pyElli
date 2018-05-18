# Encoding: utf-8

# Copyright (C) 2012-2016 Olivier Castany
# This program is free software (see LICENCE file)

"""Berreman4x4: module implementing Berreman's 4x4 matrix method.

See file "documentation.pdf"
"""

import numpy
import scipy.linalg, scipy.interpolate
from numpy import pi, newaxis
import matplotlib, matplotlib.pyplot

#########################################################
# Constants...

c = 2.998e8     # speed of light in vacuum
e_x = numpy.array([1,0,0]).reshape((3,1))   # base vectors
e_y = numpy.array([0,1,0]).reshape((3,1))
e_z = numpy.array([0,0,1]).reshape((3,1))

#########################################################
# Rotations... 

def rotation_Euler(angles):
    """Returns rotation matrix defined by Euler angles (p,n,r)
    
    'angles' : tuple (p,n,r)
    
    Returns : rotation matrix M_R.
    If A is an initial vector,  B = M_R * A is the rotated vector

    Successive rotations : z,x',z'
        p = precession angle, 1st rotation, around z (0..2π)
        n = nutation angle, 2nd rotation, around x' (0..π)
        r = 3rd rotation, around z' (0..2π)
    
    Euler rotation for the coordinates is Rz(p)·Rx(n)·Rz(r),
    where Rj(θ) is the matrix rotation for the coordinates.
    (see for example Fujiwara, p. 217)

    Note : The inverse rotation is (-r,-n,-p)
    """
    (p,n,r) = angles
    c1 = numpy.cos(p)
    s1 = numpy.sin(p)
    c2 = numpy.cos(n)
    s2 = numpy.sin(n)
    c3 = numpy.cos(r)
    s3 = numpy.sin(r)
    return numpy.matrix([[c1*c3-s1*c2*s3, -c1*s3-s1*c2*c3,  s1*s2],
                         [s1*c3+c1*c2*s3, -s1*s3+c1*c2*c3, -c1*s2],
                         [s2*s3,           s2*c3,           c2   ]])


def rotation_V(V):
    """Returns rotation matrix defined by a rotation vector V

    'V' : rotation vector (list or array)

    Returns : rotation matrix M_R
    If A is an initial vector,  B = M_R * A is the rotated vector

    The calculation is made with the matrix exponential
    M_R = exp(W), with W_{ij} = - ε_{ijk} V_{k},
    where ε_{ijk} is the Levi-Civita antisymmetric tensor.
    If V is separated in a unit vector v and a magnitude θ, V = θ·v, with
    θ = ∥V∥, the calculation of the matrix exponential is avoided, and only 
    sin(θ) and cos(θ) are needed instead.

    Note : The inverse rotation is -V
    """
    W = numpy.matrix([[0, -V[2], V[1]], 
                      [V[2], 0, -V[0]], 
                      [-V[1], V[0], 0]])
    return numpy.matrix(scipy.linalg.expm(W))


def rotation_v_theta(v,theta):
    """Returns rotation matrix defined by a unit rotation vector and an angle

    'v' : unit vector orienting the rotation (list or array)
    'theta' : rotation angle around v in radians

    Returns : rotation matrix M_R.
    If A is an initial vector,  B = M_R * A is the rotated vector

    Notes : The inverse rotation is (v,-theta) 
    """
    w = numpy.matrix([[0, -v[2], v[1]], 
                      [v[2], 0, -v[0]], 
                      [-v[1], v[0], 0]])
    return numpy.identity(3) + w * numpy.sin(theta) \
                             + w**2 * (1 - numpy.cos(theta))


#########################################################
# Dispersion laws...

class DispersionLaw:
    """Dispersion law (abstract class).
 
    Method that should be implemented in derived classes:
    * getValue(lbda) : returns refractive index for wavelength 'lbda'
    """
    def __init__(self):
        """Creates a new dispersion law -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def getValue(self, lbda):
        """Returns refractive index for wavelength 'lbda'."""
        raise NotImplementedError("Should be implemented in derived classes")


class SellmeierLaw(DispersionLaw):
    """Sellmeier dispersion law equation."""

    A, B, lbda0 = None, None, None  # Sellmeier coefficients

    def __init__(self, coeff=(1.0, 1.0, 300e-9)):
        """Creates a Sellmeier dispersion law.
        
        'coeff' : Sellmeier coefficients (A, B, λ0)
            A, B : without unit
            λ0 : resonance wavelength (m)

        n²(λ) = A + B × λ²/(λ²-λ0²)
        """
        self.A, self.B, self.lbda0 = coeff

    def getValue(self, lbda):
        """Returns refractive index value for wavelength 'lbda'."""
        n2 = self.A + self.B * lbda**2 / (lbda**2 - self.lbda0**2)
        return numpy.sqrt(n2)

class  DispersionTable(DispersionLaw):
    """Dispersion law specified by a table"""
    
    n_law = None    # Refractive index law (interpolation)
    
    def __init__(self, lbda=None, n=None):
        """Create a dispersion law from a refraction index list.
        
        'lbda'  : Wavelength (m)
        'n'     : Refractive index (data of same length)
        """
        if lbda is not None:
            self.n_law = scipy.interpolate.interp1d(lbda, n, kind='cubic')
        
    def getValue(self, lbda):
        """Returns refractive index for wavelength 'lbda'."""
        return self.n_law(lbda)

        
#########################################################
# Materials...

class Material:
    """Base class for materials (abstract class).

    Method that should be implemented in derived classes:
    * getTensor(lbda) : returns the permittivity tensor for wavelength 'lbda'.
    """
    def __init__(self):
        """Creates a new material -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def getTensor(self, lbda):
        """Returns permittivity tensor matrix for the desired wavelength."""
        raise NotImplementedError("Should be implemented in derived classes") 

class NonDispersiveMaterial(Material):

    epsilon = None   # Permittivity tensor matrix

    def __init__(self, epsilon=None):
        """Creates a Material with a non-dispersive permittivity tensor. 
        
        'epsilon' : permittivity tensor, 3x3 array or a matrix

        Notes (sloppy... should be clarified) : 
        * Definition of electromagnetic energy requires that Re(E) > 0
          [reference ???]
        * Im(E) > 0 for an absorbing medium
        * Im(E) < 0 for an amplifying medium
        """
        if epsilon is None: 
            epsilon = numpy.matrix(numpy.identity(3))
        self.epsilon = numpy.matrix(epsilon)

    def getTensor(self, lbda=None):
        """Returns permittivity tensor matrix for the desired wavelength.
        
        Note : permittivity tensor ε in Gaussian units.
        """
        return self.epsilon

    def rotated(self, R):
        """Returns a rotated Material.
        
        'R' : rotation matrix (from rotation_Euler() or others)
        """
        E = R * self.epsilon * R.T
        return NonDispersiveMaterial(E)
    

class IsotropicMaterial(Material):
    """Isotropic material (abstract class).
    
    Method that should be implemented in derived classes:
    * getRefractiveIndex(lbda) : returns refractive index for wavelength 'lbda' 
    * getTensor(lbda) : required from class Material
    """
    def __init__(self):
        """Creates a new isotropic material  -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def getRefractiveIndex(self, lbda):
        """Returns refractive index for wavelength 'lbda'."""
        raise NotImplementedError("Should be implemented in derived classes")


class IsotropicNonDispersiveMaterial(NonDispersiveMaterial, IsotropicMaterial):
    """Isotropic non-dispersive material."""
    
    n = None    # refractive index

    def __init__(self, n=1.5):
        """Creates an isotropic non-dispersive material.
        
        'n' : refractive index
        
        Notes : 
        * Im(n) > 0 for an absorbing medium
        * Im(n) < 0 for an amplifying medium
        """
        self.n = n
        self.epsilon = n**2 * numpy.matrix(numpy.identity(3))

    def getRefractiveIndex(self, lbda=None):
        """Returns refractive index."""
        return self.n


class IsotropicDispersive(IsotropicMaterial):
    """Isotropic material with dispersion law."""

    law = None      # Dispersion law

    def __init__(self, law=None):
        """Creates isotropic material with dispersion law.
        
        'law' : DispersionLaw object (for example SellmeierLaw)
        """
        self.law = law

    def getTensor(self, lbda):
        """Returns permittivity tensor matrix for the desired wavelength."""
        n = self.law.getValue(lbda)
        return numpy.matrix(n**2 * numpy.identity(3))

    def getRefractiveIndex(self, lbda):
        """Returns refractive index."""
        return self.law.getValue(lbda)
        
        

class UniaxialNonDispersiveMaterial(NonDispersiveMaterial):
    """Non-dispersive uniaxial material."""

    def __init__(self, no=1.5, ne=1.7):
        """Creates a uniaxial non-dispersive material.
        
        'no' : ordinary refractive index
        'ne' : extraordinary refractive index (oriented along the z direction)
        """
        n = numpy.diag([no,no,ne])
        self.epsilon = numpy.matrix(n**2)


class BiaxialNonDispersiveMaterial(NonDispersiveMaterial):
    """Non-dispersive biaxial material."""

    def __init__(self, diag=(1.5,1.6,1.7)):
        """Creates a biaxial non-dispersie material
        
        'diag' : xyz refractive indices, tuple (n1,n2,n3)
        """
        n = numpy.diag(diag)
        self.epsilon = numpy.matrix(n**2)


#########################################################
# Inhomogeneous materials...

class InhomogeneousMaterial:
    """Base class for inhomogeneous materials (abstract class).

    Method that should be implemented in derived classes:
    * getTensor(z, lbda) : permittivity tensor at position z
    * getSlices() : returns z_i, position of the slices
    """
    def __init__(self):
        """Creates a new inhomogeneous material -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def getTensor(self, z, lbda):
        """Returns permittivity tensor for position 'z' and wavelength 'lbda'.

        'z' : position where the tensor is evaluated
        'lbda' : wavelength
        """
        raise NotImplementedError("Should be implemented in derived classes")

    def getSlices(self):
        """Returns z slicing (including z0 and zmax).
        
        Origin of 'z' is not important, only relative positions matter.
        """
        raise NotImplementedError("Should be implemented in derived classes")


class TwistedMaterial(InhomogeneousMaterial):
    """Twisted material.
    
    Used to describe twisted nematic or cholesteric liquid crystal for example.
    """
    
    material = None     # Material for the twisted layer
    d = None            # Thickness of the layer
    angle = None        # Angle of the twist
    div = None          # Number of slices

    def __init__(self, material=None, d=4e-6, angle=pi/2, div=25):
        """Creates a layer with a twisted material.
       
        'material' : material for the twisted layer
        'd' : thickness of the layer
        'angle' : rotation angle for distance 'd'
        'div' : number of slices

        Note: Let us call h = d / div. It is useful to assess whether k0·h is 
        greater or smaller than 1. If it is greater than 1, evaluation of the
        exponential for the propagator will not be possible with linear 
        expansion, and may require a Taylor expansion with a very high order
        for convergence. In this case, use the Padé approximation or the 
        exact result with eigenvector decomposition. On the other hand, if
        k0·h is small, a linear or Taylor approximation may suffice.
        """
        self.setThickness(d)
        self.setMaterial(material)
        self.setAngle(angle)
        self.setDivision(div)

    def setDivision(self, div):
        """Defines the number of slices in this TwistedMaterial."""
        self.div = div
    
    def setAngle(self, angle):
        """Defines the total twist angle of this TwistedMaterial."""
        self.angle = angle
    
    def setMaterial(self, material):
        """Defines the material making this TwistedMaterial."""
        self.material = material

    def setThickness(self, d):
        """Defines the thickness of this TwistedMaterial."""
        self.d = d

    def getTensor(self, z, lbda=None):
        """Returns permittivity tensor matrix for position 'z'."""
        epsilon = self.material.getTensor(lbda)
        R = rotation_v_theta([0,0,1], self.angle * z /self.d)
        return R * epsilon * R.T

    def getSlices(self):
        """Returns z slicing.
        
        Returns : array of 'z' positions [z0, z1,... , zmax], 
                  with z0 = 0 and zmax = z{d+1}
        
        Notes:
        * The number of divisions is 'div' (see constructor)
        * Position is relative to this material, not to the whole structure.
        """
        return numpy.linspace(0, self.d, self.div+1)



#########################################################
# Delta matrix...

def buildDeltaMatrix(Kx, eps):
    """Returns Delta matrix for given permittivity and reduced wave number.
    
    'Kx' : reduce wave number, Kx = kx/k0
    'eps' : permittivity tensor
    
    Returns : Delta 4x4 matrix, generator of infinitesimal translations
    """
    return numpy.matrix(
        [[-Kx * eps[2,0] / eps[2,2], -Kx * eps[2,1] / eps[2,2], 
          0, 1 - Kx**2 / eps[2,2]],
         [0, 0, -1, 0],
         [eps[1,2] * eps[2,0] / eps[2,2] - eps[1,0],
          Kx**2 - eps[1,1] + eps[1,2] * eps[2,1] / eps[2,2],
          0, Kx * eps[1,2] / eps[2,2]],
         [eps[0,0] - eps[0,2] * eps[2,0] / eps[2,2],
          eps[0,1] - eps[0,2] * eps[2,1] / eps[2,2],
          0, -Kx * eps[0,2] / eps[2,2]]])


#########################################################
# Propagator for a homogeneous slab of material...

def hs_propagator(Delta, h, k0, method="linear", q=None):
    """Returns propagator for homogeneous slab of thickness h.

    'Delta' : Delta matrix of the homogeneous material
    'h' : thickness of the homogeneous slab
    'k0' : wave vector in vacuum, k0 = ω/c
    'q' : order of the approximation method, if useful

    Returns : propagator matrix, exact or approximated, depending on the 
    value of the 'method' parameter.
    
    The exact propagator is: P_hs = exp(i h k0 Δ)

    This function is a prototype and mainly useful for this docstring.
    Calculation is performed by function hs_propagator_xxxxx(), depending on 
    the value of 'method':
        "linear" -> first order approximation of exp()
        "Padé"   -> Padé approximation of exp()
        "Taylor" -> Taylor development of exp()
        "eig"    -> calculation with eigenvalue decomposition
    """
    if   method == "linear":    return hs_propagator_lin(Delta, h, k0)
    elif method == "Padé":      return hs_propagator_Pade(Delta, h, k0, q)
    elif method == "Taylor":    return hs_propagator_Taylor(Delta, h, k0, q)
    elif method == "eig":       return hs_propagator_eig(Delta, h, k0)

def hs_propagator_lin(Delta, h, k0, q=None):
    """Returns propagator with linear approximation.
    
    'q' is swallowed. It is here so as to offer the same protoype as 
    the other hs_propagator_*() functions.
    """
    P_hs_lin = numpy.identity(4) + 1j * h * k0 * Delta
    return numpy.matrix(P_hs_lin)

def hs_propagator_Pade(Delta, h, k0, q=7):
    """Returns propagator with Padé approximation of order 'q'.
    
    The diagonal Padé approximant of any order 'q' is symplectic, i.e. 
    P_hs_Pade(h)·P_hs_Pade(-h) = 1. 
    Such property may be suitable for use with Z. Lu's method.
    """
    P_hs_Pade = scipy.linalg.expm(1j * h * k0 * Delta, q)
    return numpy.matrix(P_hs_Pade)

def hs_propagator_Taylor(Delta, h, k0, q=5):
    """Returns propagator using Taylor series of order 'q'."""
    P_hs_Taylor = scipy.linalg.expm3(1j * h * k0 * Delta, q+1)
    # 'q+1' to correct SciPy bug 1687
    return numpy.matrix(P_hs_Taylor)

def hs_propagator_eig(Delta, h, k0, q=None):
    """Returns propagator using eigenvalue decomposition.
 
    'q' is swallowed. It is here so as to offer the same protoype as 
    the other hs_propagator_*() functions.

    The calculation is (see scipy.linalg.expm2() source code):
        s,vr = eig()    # eigenvalues, eigenvector array
        vri = inv(vr)   # eigenvector array inversion
        result = vr * diag(exp(s)) * vri
    """
    P_hs = scipy.linalg.expm2(1j * h * k0 * Delta)
    return numpy.matrix(P_hs)


#########################################################
# Half-spaces...

class HalfSpace:
    """Homogeneous half-space with arbitrary permittivity.
    
    A HalfSpace must provide this method:
    * getTransitionMatrix(k0, Kx) : return transition matrix
    
    """

    material = None     # Material object

    def __init__(self, material=None):
        """Create a homogeneous half-space of the given material."""
        self.setMaterial(material)

    def setMaterial(self, material):
        """Defines the material for this half-space"""
        self.material = material

    def getTransitionMatrix(self, Kx, k0=1e6):
        """Returns transition matrix L.
        
        'Kx' : reduced wavenumber in the x direction, Kx = kx/k0
        'k0' : wavenumber in vacuum, k0 = ω/c

        Sort eigenvectors of the Delta matrix according to propagation
        direction first, then according to $y$ component. 

        Returns eigenvectors ordered like (s+,s-,p+,p-)
        """
        epsilon = self.material.getTensor(2*pi/k0)
        Delta = buildDeltaMatrix(Kx, epsilon)
        q, Psi = scipy.linalg.eig(Delta)

        # Sort according to z propagation direction, highest Re(q) first
        i = numpy.argsort(-numpy.real(q))
        q, Psi = q[i], Psi[:,i]     # Result should be (+,+,-,-)
        # For each direction, sort according to Ey component, highest Ey first
        i1 = numpy.argsort(-numpy.abs(Psi[1,:2]))
        i2 = 2 + numpy.argsort(-numpy.abs(Psi[1,2:]))
        i = numpy.hstack((i1,i2))   # Result should be (s+,p+,s-,p-)
        # Reorder
        i[[1,2]] = i[[2,1]]
        q, Psi = q[i], Psi[:,i]     # Result should be(s+,s-,p+,p-)

        # Adjust Ey in ℝ⁺ for 's', and Ex in ℝ⁺ for 'p'
        E = numpy.hstack((Psi[1,:2], Psi[0,2:]))
        nE = numpy.abs(E)
        c = numpy.ones_like(E)
        i = (nE != 0.0)
        c[i] = E[i]/nE[i]
        Psi = Psi * c
        # Normalize so that Ey = c1 + c2, analog to Ey = Eis + Ers
        # For an isotropic half-space, this should return the same matrix 
        # as IsotropicHalfSpace
        c = Psi[1,0] + Psi[1,1]
        if abs(c) == 0:
            c = 1.
        Psi = 2 * Psi / c
        return numpy.matrix(Psi)


class IsotropicHalfSpace(HalfSpace):
    """Homogeneous Isotropic HalfSpace.
 
    * Provides transition matrix L and the inverse.
    
      Can be equally used for the front half-space (Φ = Φi) or for the back 
      half-space (Φ = Φt).

    * Provides relations between incidence angle Φ and reduced wave vector Kx.

      As detailed in the documentation, 'Φ' is the angle of the plane wave 
      traveling to the right (angle measured with respect to z axis and 
      oriented by y). The angle of the wave traveling to the left is '-Φ'.
    """

    def __init__(self, material=None):
        """Create a HalfSpace of the given material.
        
        'material' : IsotropicMaterial
        """
        self.setMaterial(material)

    def get_Kx_from_Phi(self, Phi, k0=1e6):
        """Returns the value of Kx.
        
        'Phi' : incidence angle of the wave (radians)
        'k0'  : wavenumber in vacuum

        As detailed in the documentation, 'Phi' is the angle of the wave 
        traveling to the right with respect to the horizontal.
        
        kx = n k0 sin(Φ) : Real and constant throughout the structure. 
                           If n ∈ ℂ, then Φ ∈ ℂ
        Kx = kx/k0 = n sin(Φ) : Reduced wavenumber.
        """
        n = self.material.getRefractiveIndex(2*pi/k0)
        Kx = n * numpy.sin(Phi)
        return Kx

    def get_Kz_from_Kx(self, Kx, k0=1e6):
        """Returns the value of Kz in the half-space, function of Kx
        
        'Kx' : Reduced wavenumber,      Kx = kx/k0 = n sin(Φ)
        'k0' : wavenumber in vacuum,    kx = n k0 sin(Φ)

        Returns : reduced wave number Kz = kz/k0
        """
        # Not vectorized. Could be? 
        # Test type(Kz2)
        n = self.material.getRefractiveIndex(2*pi/k0)
        Kz2 = n**2 - Kx**2
        return numpy.sqrt(complex(Kz2))

    def get_Phi_from_Kx(self, Kx, k0=1e6):
        """Returns the value of angle Phi according to the value of Kx.
        
        'Kx' : Reduced wavenumber,      Kx = kx/k0 = n sin(Φ)
        'k0' : wavenumber in vacuum,    kx = n k0 sin(Φ)

        Returns : angle Phi in radians.
        """
        # May be vectorized when I have time?
        n = self.material.getRefractiveIndex(2*pi/k0)
        sin_Phi = Kx/n
        if abs(sin_Phi) > 1:
            sin_Phi = complex(sin_Phi)
        Phi = numpy.arcsin(sin_Phi)
        return Phi

    def getTransitionMatrix(self, Kx, k0=1e6, inv=False):
        """Returns transition matrix L.
        
        'Kx' : Reduced wavenumber
        'k0' : wavenumber in vacuum
        'inv' : if True, returns inverse transition matrix L^-1

        Returns : transition matrix L
        """
        n = self.material.getRefractiveIndex(2*pi/k0)
        sin_Phi = Kx/n
        if abs(sin_Phi) > 1:
            sin_Phi = complex(sin_Phi)
        cos_Phi = numpy.sqrt(1 - sin_Phi**2)
        if inv:
            return 0.5 * numpy.matrix( 
                    [[ 0        , 1, -1/(n*cos_Phi),  0   ],
                     [ 0        , 1,  1/(n*cos_Phi),  0   ],
                     [ 1/cos_Phi, 0,  0            ,  1/n ],
                     [ 1/cos_Phi, 0,  0            , -1/n ]])
        else:
            return numpy.matrix( 
                    [[0         , 0        , cos_Phi, cos_Phi],
                     [1         , 1        , 0      , 0      ],
                     [-n*cos_Phi, n*cos_Phi, 0      , 0      ],
                     [0         , 0        , n      , -n     ]])


#########################################################
# Layers...

class Layer:
    """A very general layer (abstract class).
    
    Method that should be implemented in derived classes:
    * getPropagationMatrix(Kx, k0, inv) : returns propagator
      'Kx' : reduced wavenumber along x
      'k0' : wavenumber in vacuum
      'inv': boolean, if True, the propagator is from back to front.
    """

    def __init__(self):
        """Creates a new layer -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def getPermittivityProfile(self, lbda):
        """Returns permittivity tensor profile."""
        raise NotImplementedError("Should be implemented in derived classes")

    def getPropagationMatrix(self, Kx, k0, inv):
        """Returns propagation matrix P for this layer."""
        raise NotImplementedError("Should be implemented in derived classes")


class MaterialLayer(Layer):
    """A layer made of one material (abstract class).
    
    The material may be a Material or an InhomogeneousMaterial object.
    The first is a homogeneous material, the second is inhomogeneous.
    """

    material = None     # Material making the layer
    
    def __init__(self):
        """Creates a new material layer -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def setMaterial(self, material):
        """Defines the material for this layer. """
        self.material = material
   

class HomogeneousLayer(MaterialLayer):
    """Homogeneous layer of dielectric material."""

    h = None                # Thickness of the layer
    material = None         # Material object
    hs_propagator = None    # Function used for the propagator calculation
    hs_order = None         # Approximation order, if useful

    def __init__(self, material=None, h=1e-6, hs_method="eig", hs_order=2):
        """New homogeneous layer of material 'material', with thickness 'h'
        
        'hs_method', 'hs_order': see setMethod()
        """
        self.setMaterial(material)
        self.setMethod(hs_method, hs_order)
        self.setThickness(h)

    def setThickness(self, h):
        """Defines the thickness of this homogeneous layer."""
        self.h = h

    def setMethod(self, hs_method, hs_order=2):
        """Defines how the homogeneous slab propagator is calculated.
        
        "linear" -> first order approximation of exp()
        "Padé"   -> Padé approximation of exp()
        "Taylor" -> Taylor development of exp()
        "eig"    -> calculation with eigenvalue decomposition

        'hs_order' : order of approximation, if useful
        """
        if hs_method == "linear":  
            self.hs_propagator = hs_propagator_lin
        elif hs_method == "Padé":    
            self.hs_propagator = hs_propagator_Pade
        elif hs_method == "Taylor":  
            self.hs_propagator = hs_propagator_Taylor
        elif hs_method == "eig":     
            self.hs_propagator = hs_propagator_eig
        else: 
            raise NotImplementedError("Method " + hs_method + 
                        " not available for propagator calculation")
        self.hs_order = hs_order

    def getPermittivityProfile(self, lbda=1e-6):
        """Returns permittivity tensor profile.
        
        Returns a list containing one tuple: [(h, epsilon)]
        """
        return [(self.h, self.material.getTensor(lbda))]

    def getPropagationMatrix(self, Kx, k0=1e6, inv=False):
        """Returns propagation matrix P 
        
        Psi(z+h) = P * Psi(z)
        P = exp(i h k0 Delta h), where 'exp' is the matrix exponential.

        'Kx' : reduced wavenumber along x
        'k0' : vacuum wavenumber
        'inv' : returns the inverse matrix, BP = exp(-i h k0 Delta)
        """
        epsilon = self.material.getTensor(2*pi/k0)
        Delta = buildDeltaMatrix(Kx, epsilon)
        if inv:
            h = -self.h
        else:
            h = self.h
        return self.hs_propagator(Delta, h, k0, self.hs_order)

    def getDeltaMatrix(self, Kx, k0=1e6):
        """Returns Delta matrix of the homogeneous layer."""
        epsilon = self.material.getTensor(2*pi/k0)
        Delta = buildDeltaMatrix(Kx, epsilon)
        return Delta

class HomogeneousIsotropicLayer(HomogeneousLayer):
    """Homogeneous Isotropic Layer.
    
    Must be made of an isotropic material.

    Provides function get_QWP_thickness(lbda) returning the thickness of a
    Quarter Wave Plate at wavelength 'lbda'.

    Can be created with parameter h = ("QWP", 1e-6), see method setThickness().
    """

    def setThickness(self, h):
        """Defines the thickness of this homogeneous isotropic layer.
        
        If h is a tuple ('QWP', lbda), the thickness 'h' is calculated for a
        quarter-wave plate at wavelength 'lbda'.
        """
        # Special case when a quarter-wave plate is requested
        if isinstance(h, tuple):
            (name, lbda) = h
            if name == "QWP":
                h = self.get_QWP_thickness(lbda)
            else:
                raise ValueError("Thickness not correctly defined.")
        self.h = h

    def get_QWP_thickness(self, lbda=1e-6):
        """Return the thickness of a Quater Wave Plate at wavelength 'lbda'."""
        nr = numpy.real(self.material.getRefractiveIndex(lbda))
        return lbda / (4.*nr)


#########################################################
# Inhomogeneous layers...

class InhomogeneousLayer(MaterialLayer):
    """Inhomogeneous layer.
    
    Must be fabricated with an InhomogemeousMaterial object.
    """

    material = None     # InhomogemeousMaterial object

    # Method used to decompose the inhomogeneous layer into homogeneous slabs:
    getSlicePropagator = None
    # Method used to calculate the propagator of a homogeneous slab:
    hs_propagator = None
    # Order for the above method, if useful:
    hs_order = None

    def __init__(self, material=None, evaluation="midpoint", 
                                      hs_method="Padé", q=2):
        """Creates an inhomogeneous layer.
        
        'material' : InhomogemeousMaterial object

        The propagation matrix is evaluated depending on parameters 
        'evaluation', 'hs_method' and order 'q', see setMethod().
        """
        self.setMaterial(material)
        self.setMethod(evaluation, hs_method, q)

    def setMethod(self, evaluation, hs_method, q=2):
        """Defines the calculation method.

        The propagator for the inhomogeneous layer is decomposed and evaluated
        depending on parameter 'evaluation':
        "midpoint"   -> Evaluation of Δ(z) at midpoint. 
        "symplectic" -> Z. Lu's symplectic method with three evaluation points.
        
        The propagator for a thin and homogeneous slice is calculated according 
        to arguement 'hs_method':
        "linear" -> first order approximation of exp()
        "Padé"   -> Padé approximation of exp()
        "Taylor" -> Taylor development of exp()
        "eig"    -> calculation with eigenvalue decomposition
        
        The midpoint method may use any of these, provided that the 
        approximation is not too bad. For example, the linear approximation 
        is quick but only works if the argument of the exponential is small.
        A "Padé" approximation of order 2 may be a good choice.

        The symplectic method requires P(h)·P(-h) = Id, which is true for
        the "Padé" approximation and the exact "eig" method.
      
        The error on the propagator for an inhomogeneous thin slice due to the 
        replacement by a homogeneous slice is O(h^3) in the midpoint method and 
        O(h^5) in the symplectic method. A Padé approximant of order q gives an
        approximation of the propagator to order O(h^(2q)). Consequently, q = 3
        should be a good enough for the syplectic method.
        """
        if evaluation == "midpoint":
            self.getSlicePropagator = self.getSlicePropagator_mid
            if hs_method == "linear":  
                self.hs_propagator = hs_propagator_lin
            elif hs_method == "Padé":    
                self.hs_propagator = hs_propagator_Pade
            elif hs_method == "Taylor":  
                self.hs_propagator = hs_propagator_Taylor
            elif hs_method == "eig":     
                self.hs_propagator = hs_propagator_eig
            else: 
                raise NotImplementedError("Method " + hs_method + 
                            " not available for midpoint evaluation")
        elif evaluation == "symplectic":
            self.getSlicePropagator = self.getSlicePropagator_sym
            if hs_method == "Padé":    
                self.hs_propagator = hs_propagator_Pade
            elif hs_method == "eig":
                self.hs_propagator = hs_propagator_eig
            else:
                raise NotImplementedError("Method " + hs_method +
                            " not available for symplectic evaluation")
        self.hs_order = q

    def getPermittivityProfile(self, lbda=1e-6):
        """Returns permittivity tensor profile.
        
        Tensor is evaluated in the middle of each slice.
        Returns list [(h1, epsilon1), (h2, epsilon2), ... ]
        """
        z = self.material.getSlices()
        h = numpy.diff(z)
        zmid = (z[:-1] + z[1:]) / 2.
        tensor = [self.material.getTensor(z, lbda) for z in zmid]
        return list(zip(h, tensor))

    def getPropagationMatrix(self, Kx, k0=1e6, inv=False):
        """Returns propagation matrix P."""
        z = self.material.getSlices()
        if inv:
            z = z[::-1]
        P_tot = numpy.matrix(numpy.identity(4))
        for i in range(len(z)-1):
            P = self.getSlicePropagator(z[i+1], z[i], Kx, k0)
            P_tot = P * P_tot
        return P_tot

    def getSlicePropagator_mid(self, z2, z1, Kx, k0=1e6):
        """Returns propagation matrix P(z2,z1) for a thin slice. 

        Evaluates the Delta Matrix at midpoint between z1 and z2. The
        resulting global error is O(h^2).

        Note: The propagation matrix is calculated with one of the 
        hs_propagator_*() functions, pointed by the attribute
        InhomogeneousLayer.midpoint_hs_propagator().
        """
        epsilon = self.material.getTensor((z1+z2)/2., 2*pi/k0)
        Delta = buildDeltaMatrix(Kx, epsilon)
        P = self.hs_propagator(Delta, z2-z1, k0, self.hs_order)
        return P

    # Coefficients from Z. Lu's article for the sympletic method
    s = 2.**(1./3)
    b1 = 1./(2-s)
    b2 = -s/(2-s)
    t1 = 1./(2*(2-s))
    t2 = 1./2
    t3 = 1./2 - (s-1)/(2*(2-s))

    def getSlicePropagator_sym(self, z2, z1, Kx, k0=1e6):
        """Returns propagation matrix P_sym(z2,z1) for a thin slice.

        Uses Z. Lu's symplectic method, leading to a global error in O(h^4).

        Note : We have P_sym(z2,z1) P_sym(z1,z2) = Id. This can be 
        demonstrated by the relations z1 + t1 h = z2 - t3 h and 
        z1 + t2 h = z2 - t2 h.
        """
        h = z2 - z1
        epsilon1 = self.material.getTensor(z1+self.t1*h, 2*pi/k0)
        epsilon2 = self.material.getTensor(z1+self.t2*h, 2*pi/k0)
        epsilon3 = self.material.getTensor(z1+self.t3*h, 2*pi/k0)
        Delta1 = buildDeltaMatrix(Kx, epsilon1)
        Delta2 = buildDeltaMatrix(Kx, epsilon2)
        Delta3 = buildDeltaMatrix(Kx, epsilon3)
        q = self.hs_order
        P1 = self.hs_propagator(Delta1, self.b1*h, k0, q)
        P2 = self.hs_propagator(Delta2, self.b2*h, k0, q)
        P3 = self.hs_propagator(Delta3, self.b1*h, k0, q)
        return P1*P2*P3



#########################################################
# Repeated layers...

class RepeatedLayers(Layer):
    """Repetition of a structure."""

    n = None        # Number of repetitions
    before = None   # additionnal layers before the first period
    after = None    # additionnal layers after the last period
    layers = None   # layers to repeat

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

    def getPermittivityProfile(self, lbda=1e-6):
        """Returns permittivity tensor profile.
        
        Returns list of tuples [(h1, epsilon1), (h2, epsilon2), ... ]
        """
        layers = sum([L.getPermittivityProfile(lbda) for L in self.layers], [])
        if self.before > 0:
            before = layers[-self.before:] 
        else:
            before = []
        return before + self.n * layers + layers[:self.after]

    def getPropagationMatrix(self, Kx, k0=1e6, inv=False):
        """Returns propagation matrix P for the repeated layers."""
        P_list = [L.getPropagationMatrix(Kx,k0,inv) for L in self.layers]
        P_period = P_before = numpy.matrix(numpy.identity(4))
        i_after = self.after
        i_before = len(P_list) - self.before
        if inv:
            for (i,P) in enumerate(P_list):
                if i == i_after:
                    P_after = P_period
                P_period = P_period * P
                if i >= i_before:
                    P_before = P_before * P
            return P_before * P_period**self.n * P_after
        else:
            for (i,P) in enumerate(P_list):
                if i == i_after:
                    P_after = P_period
                P_period = P * P_period
                if i >= i_before:
                    P_before = P * P_before
            return P_after * P_period**self.n * P_before
        


#########################################################
# Structure to simulate...

class Structure:
    """Description of the whole structure.
 
    * front half-space (incident), must be isotropic
    * back half-space (exit), may be anisotropic
    * layer succession
    """
    frontHalfSpace = None
    backHalfSpace = None    
    layers = None               # list of layers
    
    def __init__(self, front=None, layers=None, back=None):
        """Creates an empty structure.
        
        'front' : front half space, see setFrontHalfSpace()
        'layers' : layer list, see setLayers()
        'back' : back half space, see setBackHalfSpace()
        """
        self.layers = []        # list of layers
        if front is not None:
            self.setFrontHalfSpace(front)
        if layers is not None:
            self.setLayers(layers)
        if back is not None:
            self.setBackHalfSpace(back)
        
    def setFrontHalfSpace(self, halfSpace):
        """Defines the front half-space.
        
        'halfSpace' : HalfSpace object
        """
        self.frontHalfSpace = halfSpace

    def setBackHalfSpace(self, halfSpace):
        """Defines the back half-space.
        
        'halfSpace' : HalfSpace object
        """
        self.backHalfSpace = halfSpace

    def setLayers(self, layers):
        """Set list of layers.
        
        'layers' : list of layers, starting from z=0
        """
        self.layers = layers

    def getPermittivityProfile(self, lbda=1e-6):
        """Returns permittivity tensor profile."""
        layers = sum([L.getPermittivityProfile(lbda) for L in self.layers], [])
        front = (float('inf'), self.frontHalfSpace.material.getTensor(lbda))
        back = (float('inf'), self.backHalfSpace.material.getTensor(lbda)) 
        return sum([[front], layers, [back]], [])

    def getPropagationMatrix(self, Kx, k0=1e6, inv=False):
        """Gives the propagation matrix of the structure.

        'Kx' : reduced wavenumber along x
        'k0' : wavenumber in vacuum
        'inv' : returns propagation matrix for decreasing z

        Returns : propagation matrix P(zb,zf) for the full structure 

        Psi(zb) = P_(zb, z_{N-1}) * ... * P(z1,zf) * Psi(zf)
                = P(zb,zf) * Psi(zf)
        """
        if inv:
            layers = reversed(self.layers)
        else:
            layers = self.layers
        P_tot = numpy.matrix(numpy.identity(4))
        # Cumulative products :
        for L in layers:
            P = L.getPropagationMatrix(Kx,k0,inv)
            P_tot = P * P_tot
        return P_tot


    def getIndexProfile(self, lbda=1e-6, v=e_x):
        """Returns refractive index profile.
        
        'v' : unit vector, direction of evaluation
        """
        profile = self.getPermittivityProfile(lbda)
        (h, epsilon) = list(zip(*profile))  # unzip
        n = [ numpy.sqrt((v.T * eps * v)[0,0]) for eps in epsilon ]
        return list(zip(h,n))

    def drawStructure(self, method="graph", lbda=1e-6, margin=0.15):
        """Draw the structure.
        
        'method' : 'graph' or 'section'
        Returns : Axes object
        """
        # Build index profile
        profile = self.getIndexProfile(lbda)
        (h,n) = list(zip(*profile))     # unzip
        n = numpy.array(n)
        z_layers = numpy.hstack((0., numpy.cumsum(h[1:-1])))
        z_max = z_layers[-1]
        if z_max != 0.:
            z_margin = margin * z_max
        else:
            z_margin = 1e-6
        z = numpy.hstack((-z_margin, z_layers, z_max + z_margin))
        # Call specialized methods
        if method == "graph":
            ax = self._drawStructureGraph(z,n)
        elif method == "section":
            ax = self._drawStructureSection(z,n)
        else:
            ax = None
        return ax

    def _drawStructureGraph(self, z, n):
        """Draw a graph of the refractive index profile """
        n = numpy.hstack((n, n[-1]))
        # Draw the graph
        fig = matplotlib.pyplot.figure(figsize=(8,3))
        ax = fig.add_subplot("111")
        fig.subplots_adjust(bottom=0.17)
        ax.step(z, n.real, 'black', where='post')
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xlabel("z (m)")
        ax.set_ylabel("n")
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
        ax.set_xlim(z.min(), z.max())
        ax.set_ylim(bottom=1.0)
        return ax

    def _drawStructureSection(self, z, n):
        """Draw a cross section of the structure"""
        # Prepare arrays for pcolormesh()
        X = z * numpy.ones((2,1))
        Y = numpy.array([0,1]).reshape((2,1)) * numpy.ones_like(z)
        n = numpy.array(n).reshape((1,-1)).real
        # Draw the cross section
        fig = matplotlib.pyplot.figure(figsize=(8,3))
        ax = fig.add_subplot("111")
        fig.subplots_adjust(left=0.05, bottom=0.15)
        ax.set_yticks([])
        ax.set_xlabel("z (m)")
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
        ax.set_xlim(z.min(), z.max())
        stack = ax.pcolormesh(X,Y,n, cmap=matplotlib.cm.gray_r)
        colbar = fig.colorbar(stack, orientation='vertical', anchor=(1.2,0.5), 
                              fraction=0.05)
        colbar.ax.set_xlabel("n", position=(3,0))
        return ax


    def getStructureMatrix(self, Kx, k0=1e6):
        """Returns the transfer matrix T of the structure.

        [Eis, Ers, Eip, Erp].T = T * [c1, c2, c3, c4].T
        T = Lf^-1 * P(zf,zb) * Lb
        """
        ILf = self.frontHalfSpace.getTransitionMatrix(Kx, k0, inv=True)
        P = self.getPropagationMatrix(Kx, k0, inv=True)
        Lb = self.backHalfSpace.getTransitionMatrix(Kx, k0)
        T = ILf * P * Lb
        return T

    def getJones(self,Kx,k0=1e6):
        """Returns the Jones matrices.
        
        Returns : tuple (T_ri, T_ti)

        T_ri is the Jones matrix for reflexion : [[r_pp, r_ps],
                                                  [r_sp, r_ss]]

        T_ti is the Jones matrix for transmission : [[t_pp, t_ps],
                                                     [t_sp, t_ss]]
       
        Naming convention (Fujiwara, p. 220):
        't_ps' : transmitted 'p' component for an 's' incident wave
        't_ss' : transmitted 's' component for an 's' incident wave
        ...

        Note: If all materials are isotropic, r_ps = r_sp = t_sp = t_ps = 0

        See also: 
        * extractCoefficient() to extract the desired coefficients.
        * circularJones() for circular polarization basis
        """
        T = self.getStructureMatrix(Kx,k0)
        # Extraction of T_it out of T. "2::-2" means integers {2,0}.
        T_it = T[2::-2,2::-2]
        # Calculate the inverse and make sure it is a matrix.
        T_ti = numpy.matrix(numpy.linalg.inv(T_it))
        
        # Extraction of T_rt out of T. "3::-2" means integers {3,1}.
        T_rt = T[3::-2,2::-2]
        
        # Then we have T_ri = T_rt * T_ti
        T_ri = numpy.dot(T_rt, T_ti)
        return (T_ri, T_ti)

    def getPowerTransmissionCorrection(self, Kx, k0=1e6):
        """Returns correction coefficient for power transmission

        The power transmission coefficient is the ratio of the 'z' components
        of the Poynting vector:       T = P_t_z / P_i_z
        For isotropic media, we have: T = kb'/kf' |t_bf|^2
        The correction coefficient is kb'/kf' 
        
        Note : For the moment it is only meaningful for isotropic half spaces.
        """
        Kzf = self.frontHalfSpace.get_Kz_from_Kx(Kx, k0)
        if isinstance(self.backHalfSpace, IsotropicHalfSpace):
            Kzb = self.backHalfSpace.get_Kz_from_Kx(Kx, k0)
            return Kzb.real / Kzf.real
        else:
            return None

    def evaluate(self, Kx, k0=1e6):
        """Return the Evaluation of the structure for the given parameters"""
        return Evaluation(self, Kx, k0)


#########################################################
# Record of the evaluation of one structure...

class Evaluation:
    """Record of a simulation result."""
    
    structure = None        # Simulated structure
    Kx = None               # Reduced incidence wavenumber
    k0 = None               # Wavenumber
    T_ri = None             # Jones matrix for reflection
    T_ti = None             # Jones matrix for transmission
    power_corr = None       # Power correction coefficient for transmission
        
    def __init__(self, structure, Kx, k0=1e-6):
        """Record the result of the requested simulation."""
        self.structure = structure
        self.Kx = Kx
        self.k0 = k0
        (self.T_ri, self.T_ti) = structure.getJones(Kx,k0)
        self.power_corr = structure.getPowerTransmissionCorrection(Kx,k0)


#########################################################
# Work with Jones matrices...

class _MonitorChangers:
    """Provides ability to monitor the changes of an object.
    
    Usage : MonitoredClass = _MonitorChangers.monitorized(ClassToMonitor)
   
    * MonitoredClass is a monitorized copy of ClassToMonitor

    ClassToMonitor should expose two attributes:
    
    * 'changed' : a boolean flag that becomes True when a change happens.
      It can be reset to False by other methods of the class, typically in 
      method update()
    
    * '_changer_methods' : a list of method names that are declared as 
      changers. They will be wrapped so that every call to one of these
      methods will turn the 'change' flag to True.
    """

    @staticmethod
    def proxy_decorator(method):
        """Return the wrapped 'method'."""
        def wrapped_method(self, *args, **kw):
            self.changed = True
            return method(self, *args, **kw)
        wrapped_method.__name__ = method.__name__
        return wrapped_method

    @classmethod
    def monitorized(self, cls):
        """Return monitorized class after wrapping 'cls._changer_methods'."""
        # Create new method dictionary and wrap some methods
        new_dict = cls.__dict__.copy()
        for method_name in cls._changer_methods:
            method = getattr(cls, method_name)
            new_dict[method_name] = self.proxy_decorator(method)
        # Return new class
        return type("Monitorized_" + cls.__name__, cls.__bases__, new_dict)

@_MonitorChangers.monitorized
class DataList(list):
    """A class for manipulating the simulation results.
    
    Note : The functions getCircularJones() and getEllipsometryParameters()
    are defined as class methods so that they can be called both from instances
    ans from the class itself.
    """

    # Transformation matrix from the (s,p) basis to the (L,R) basis...
    C = 1 / numpy.sqrt(2) * numpy.matrix([[1, 1], [1j, -1j]])
    D = 1 / numpy.sqrt(2) * numpy.matrix([[1, 1], [-1j, 1j]])
    invC = numpy.linalg.inv(C)
    invD = numpy.linalg.inv(D)

    # For monitoring changes (used by the decorator)
    _changer_methods = ["__setitem__", "__delitem__", "pop", "append", 
                        "extend", "insert", "remove", "__iadd__"]
    changed = False

    # Parameters for table update...
    _evaluation_keys = ("Kx", "k0", "T_ri", "T_ti", "power_corr")
    compute_power_transmission = False
    compute_circular = False
    compute_ellipsometry = False

    # Initialization...
    def __init__(self, *evaluation_seq):
        """Build a data storage from Evaluation objects."""
        list.__init__(self, *evaluation_seq)
        self.changed = True
        self.compute_power_transmission = False
        self.compute_circular = False
        self.compute_ellipsometry = False

    def update(self):
        """Build the data arrays"""
        # Build arrays from the Evaluation objects...
        keys = self._evaluation_keys
        d = self._extract_list(keys, self)
        for k in keys:
            setattr(self, k, numpy.array(d[k]))

        # Rename some data...
        (self.r, self.t) = (self.T_ri, self.T_ti) 

        # Compute additional data...
        self.R  = abs(self.T_ri)**2

        if self.compute_power_transmission:
            self.T  = abs(self.T_ti)**2 * self.power_corr[:,newaxis,newaxis]
       
        if self.compute_circular:
            self.Tc_ri = self.getCircularJones(self.T_ri, "reflection")
            self.Rc = abs(self.Tc_ri)**2
            self.Tc_ti = self.getCircularJones(self.T_ti, "transmission")
            self.Tc = abs(self.Tc_ti)**2 * self.power_corr[:,newaxis,newaxis]

        if self.compute_ellipsometry:
            (self.Psi, self.Delta) = self.getEllipsometryParameters(self.T_ri)
        
        # Reset flag...
        self.changed = False

    @classmethod
    def _extract_list(cls, keys, l):
        """Recursive extraction of the 'keys' from objects in list 'l'.
        
        'l' : List of objects (the list may be nested to any level).
        'keys' : Sequence of strings naming the object attributes to extract

        Returns : Dictionary with the extracted keys, reproducing the structure
                  of the original list.
        """
        d = {k:[] for k in keys}
        if isinstance(l[0], list):
            for ll in l:
                dd = cls._extract_list(keys, ll)
                for k in keys: d[k].append(dd[k])
        else:
            for ob in l:
                for k in keys: d[k].append(getattr(ob, k))
        return d

    @classmethod
    def getCircularJones(cls, J, direction="reflection"):
        """Return the Jones matrix for the circular polarization basis (L,R)
        
        The Jones matrices for reflection and transmission (T_ri, T_ti) are
        based on the (p,s) polarization basis. Their shape is [...,2,2].
       
        The Jones matrices in the (L, R) circular polarizations are 
        Tc_ri = D⁻¹ T_ri C   and   Tc_ti = C⁻¹ T_ti C
        """
        if direction[0] == 'r':
            return numpy.einsum('ij,...jk,kl->...il', cls.invD, J, cls.C)
        if direction[0] == 't':            
            return numpy.einsum('ij,...jk,kl->...il', cls.invC, J, cls.C)

    @classmethod
    def getEllipsometryParameters(cls, J):
        """Calculate the ellipsomerty parameters from Jones matrix 'J'.
        
        The Jones matrix for reflexion is 'T_ri', with shape [...,2,2].
    
        Ellipsometry coefficients are defined by the relation
        T_ri / r_ss = [[ tan(Ψ_pp)*exp(-i Δ_pp) , tan(Ψ_ps)*exp(-i Δ_ps) ]
                       [ tan(Ψ_sp)*exp(-i Δ_sp) ,           1            ]]
    
        The returned arrays are the angles in degrees, in a tuple
           Psi = [[ Ψ_pp, Ψ_ps ]        Delta = [[ Δ_pp, Δ_ps ]
                  [ Ψ_sp, 45°  ]],               [ Δ_sp,  0°  ]].
        
        Note: Convention for ellipsometry is used.
        See Fujiwara, (4.4), (4.6), (6.14), (6.15)     
        """
        r_ss = J[...,1,1]           # Extract 'r_ss' and complement shape for
        r_ss = numpy.array(r_ss)    # element-wise division (the second line
        r_ss.shape += (1,1)         # works around a Numpy bug)
        S = J / r_ss                # Normalize matrix
        S[...,0,:] = -S[...,0,:]    # Change to ellipsometry sign convention
    
        Psi = numpy.arctan(numpy.abs(S))*180/pi
        Delta = -numpy.angle(S, deg=True)
        return (Psi, Delta)


    def get(self, name):
        """Return the data for the requested coefficient 'name'.
        
        Examples for 'name'...
        'r_sp' : Amplitude reflection coefficient from 's' to 'p' polarization.
        'r_LR' : Reflection from circular right to circular left polarization.
        'T_pp' : Power transmission coefficient from 'p' to 'p' polarization.
        'Ψ_ps', 'Δ_pp' : Ellipsometry parameters.

        Note : 'Ψ', 'Δ' are shortcuts for 'Ψ_pp' and 'Δ_pp', which are the only
        non zero parameters for samples with isotropic layers.

        For more information about the definition of the...
        * ellipsomtery parameters see getEllipsometryParameters()
        * circular polarization, see getCircularJones()

        Returns : array of values
        """
        param = name[0]

        # Check if some tables should be activated...
        power_transmission = param == 'T'
        circular = len(name) > 1 and name[2] in ['L','R']
        ellipsometry = param in ['Ψ', 'Δ']

        if not self.compute_power_transmission and power_transmission:
            self.compute_power_transmission = True
            self.changed = True

        if not self.compute_ellipsometry and ellipsometry:
            self.compute_ellipsometry = True
            self.changed = True

        if not self.compute_circular and circular:
            self.compute_circular = True
            self.changed = True

        if self.changed:
            self.update()

        # Read the requested indices...
        (i,j) = map(self._polarIndex, name[2:4]) if len(name) > 1 else (0,0)

        # Select the requested array...
        if   param == 'r':
            M = self.Tc_ri if circular else self.T_ri
        elif param == 't':
            M = self.Tc_ti if circular else self.T_ti
        elif param == 'R':
            M = self.Rc if circular else self.R
        elif param == 'T':
            M = self.Tc if circular else self.T
        elif param == 'Ψ':
            M = self.Psi
        elif param == 'Δ':
            M = self.Delta

        # Return the requested data...
        return M[...,i,j]

    def _polarIndex(self, char):
        """Return polarization index for character 'char'.
        
        Returned value : 'p', 'L' -> 0
                         's', 'R' -> 1
        """
        if   char in ['p', 'L']:
            return 0
        elif char in ['s', 'R']:
            return 1
   

###############################################################################
###############################################################################
# Below is an old chunk of code that is not connected to the current working
# code. I leave it here in case an idea could be reused.

class _TwistedLayer:
    """Twisted layer (like a cholesteric liquid crystal)."""

    """Faire un produit modulo la période, période**n"""
    """Attention : 
        il faut donner la possibilité d'une hélice droite ou gauche.
        p > 0 <=> hélice droite ? à vérifier """

    # From parent class :
    #   h = None            # thickness
    #   epsilon = Tensor()  # permittivity tensor 

    p = +1e-6           # pitch (one helix turn, sign matters) 
    theta_i = None      # Orientation of the tensor at the input plane
    theta_t = None      # and at the output plane
    M = 24              # Discretization per pitch (helix turn)

    def __init__(self,h,tensor=None,pitch=+1e-6,theta_i=0,theta_t=0):
        """New layer of twisted material."""
        self.h = h
        self.theta_i = theta_i
        self.theta_t = theta_t
        self.p = pitch 
        if tensor != None:
            self.epsilon = tensor
            
    def adjust_pitch(self,symmetry=2,pitch=None):
        """Adjusts the value of the pitch to satisfy the boundary conditions.

        The boundary conditions are the values of theta_i and theta_t on
        the left and right surfaces of the twisted layer. 
        The distance between the two surfaces is 'h'.

        'symmetry' is the number of equivalent orientations (the default is 2,
        which is the case of a nematic/cholesteric liquid crystal).
        """
        s = float(symmetry)
        if pitch != None: 
            p = pitch
        else: 
            p = self.p

        # We want to set p to a value p' such that : 
        # h*2pi/p' = theta_t - theta_i [2pi/s]
        # This implies that there exist an integer n such that :
        # h*2pi/p' = theta_t - theta_i - n*2pi/s
        # We calculate the closest integer n with the current value of p
        # and deduce the appropriate value of p'.
        D = (self.theta_t-self.theta_i) / (2 * numpy.pi)
        n = (D - self.h / p) * s
        n = numpy.round(n)
        pp = self.h / (D - n / s)
        self.p = pp
        return pp


    def setSlicing(self,M=24):
        """Defines the number M of slices in one pitch."""
        self.M = M
    
    def getSlicing(self):
        """Returns the number M of slices in one pitch."""
        return self.M

    def optimizeSlicing(self,M_min=14,M_max=24):
        """Optimizes slicing of the pitch of a twisted material.
        
        M_min, M_max : minimum and maximum values allowed for M,
        where M is the number of slices in one pitch.
        """

        # An efficient slicing of the structure requires :
        # p = M dz and h = N dz, where M and N are both integers. 
        # Obviously, this may not be possible.
        # M is definitely taken to be an integer in order to have a good 
        # approximation for a whole pitch (thickness p). 
        # We then want to have : h = N*p/M.
        # This algorithm tries to find the most appropriate value for M. It 
        # should produce an exact slicing when h/p is a 'simple' rational
        # number. In the case of idealized twisted liquid crystal cells, 
        # the values for h/p are often 1/4 (TN) or 3/4 (STN). In the case of
        # a cholesteric liquid crystal, we can have for example h/p = 10.0 or
        # 10.5. If the range M_min..M_max includes a multiple of 4, the 
        # algorithm will then find an exact slicing.

        # See also the function getPropagationMatrix for further details.
        # Note : There may exist a better algorithm, but this one is simple.
        # Note : If the pitch has not been adjusted to the boundary conditions,
        # the program will proceed, based on the value of theta_i, but the value
        # theta_t will not be respected.

        M = numpy.arange(M_min,M_max+1)
        dz = abs(p)/M                       # dz = |p|/M
        dh = numpy.abs(self.h - numpy.round(self.h / dz)*dz)    
        self.M = M[numpy.argmin(dh)]
        return self.M

    def getPropagationMatrix(self, theta=[0.], Kx=[0.], k0=[1e7], backwards=0):
        """ Gives the propagation matrix for the twisted layer.
        
        'theta', 'Kx', 'k0' : lists or arrays
        
        Returns an array of propagation matrices with shape (theta,Kx,k0,4,4).
        """

        # The real twisted material is making a helix where the orientaion 
        # alpha varies continuously. The structure will be approximated 
        # by slices of homogeneous material.

        # Basic slices.
        # A generic pitch is divided in M thin slices with orientations :
        # alpha_m = theta_0 + theta_i + d_alpha*(0.5+m), m=0..M-1
        # (see below for an explanation of the term theta_0)
        # Thickness of a slice : dz = |p|/M
        # Corresponding angle variation : d_alpha = 2pi/M signe(p) = 2pi/p*dz

        # Structure slicing.
        # The real structure is approximated by a succession of the previous
        # basic slices (N slices). If the whole structure is rotated by angle 
        # theta, the average angle of the first slice is : 
        #   average_alpha = theta_i + theta + d_alpha*0.5
        # For this slice to be nicely approximated by one of the basic slices,
        # there should exist an index ms verifying :
        #   average_alpha = alpha_ms = theta_i + theta_0 + d_alpha*(0.5+ms)
        # Thus : ms = ((theta - theta_0) / d_alpha) % M
        # However, the values of theta and theta_i may not allow the
        # fullfilment of the exact situation and the value of ms calculated 
        # above may not be an integer, so the ratio will be rounded beforehand.
        
        # The number theat_0 is an alignment value. The slice approximation
        # will be closer to the real twisted structure if (theta - theta_0) is
        # a multiple of d_alpha, so a good value for theta_0 is to choose 
        # theta[0]. As a consequence, when this function is called with an 
        # array theta[] containing several values for theta, the result will be
        # more accurate for the other theta if they are spaced by d_alpha with
        # respect to theta[0].

        # For the backwards propagation matrix, we inverse dz and d_alpha, 
        # and start with angle theta_t.
        
        # Here we go...
        
        M = self.M
        dz = abs(self.p) / M                # slice thickness
        if backwards: dz = -dz             
        d_alpha = 2*numpy.pi / self.p * dz  # sign matters
            
        # Alignment.
        theta_0 = theta[0]      # I don't see a better choice

        # Basic slices.
        if backwards: 
            theta_start = self.theta_t
        else:
            theta_start = self.theta_i
            
        alpha = theta_0 + theta_start + d_alpha * (0.5 + numpy.arange(M))
        Deltas = self.getDelta(alpha,Kx)
 
        # Structure slicing.
        N = abs(int(round(self.h / dz)))        # h = N |dz|
        theta = numpy.array(theta)
        m_s = numpy.mod(numpy.round((theta-theta_0) / d_alpha), M).astype(int)

        # Propagation matrices of the base slices.
        # Name AP : A for "alpha", P for "propagation matrix"
        left_idx = Deltas.shape[:-2]  
                # left indices of array Deltas : (alpha,Kx)
        ap = [ [ scipy.linalg.expm(1j * k_0 * Deltas[i] * dz, q=3)
                 for k_0 in k0 ]
               for i in numpy.ndindex(left_idx) ]
        AP = numpy.array(ap)            # shape : (prod(left_idx),k0,4,4)
        right_idx = AP.shape[-3:]       # (k0,4,4)
        AP.shape = left_idx + right_idx # (tuple concatenation)
                # shape reconstruction : (alpha,Kx,k0,4,4)

        if N == 0:
           P = ones((len(theta),) + AP.shape[1:]) * numpy.identity(4)
           # Note the tuple concatenation and the broadcasting
           # shape : (theta, Kx, k0, 4, 4)
           return P
        
        if N < 2*M:
            p = []
            # Memory reservation
            s = list(AP.shape)  
            s[0] = 2 * s[0]
            CP = numpy.zeros(s)
            for ms in m_s:
                # Cumulative products of the propagation matrices :
                CP[0] = P[ms]
                for n in range(1,N):           # matrix product :
                    m = (ms + n) % M
                    CP[n] = (AP[m][...,:,:,newaxis] * 
                              CP[n-1][...,newaxis,:,:]).sum(axis=-2)
                p.append(CP[-1])
            P = numpy.array(p)
            return P
            # shape of the returned array : (theta, Kx, k0, 4, 4)
            # à vérifier 

        if N >= 2*M:
            # Here we separate three regions :
            # - left region from n = 0 to the next n1 such that n1%m = M-1
            # - middle region made of full pitches
            # - right region with the rest.
            
            # Cumulative products for one pitch :
            # Name PCP : P for "pitch", CP for "cumulative product"
            CP = numpy.zeros(AP.shape)
            CP[0] = P[0]
            for m in range(1,M):           # matrix product :
                CP[m] = (AP[m][...,:,:,newaxis] * 
                          CP[m-1][...,newaxis,:,:]).sum(axis=-2)
            PCP = CP[-1]                    # shape : (Kx,k0,4,4)
            # Number of guaranteed full pitches :
            fp = N//M - 1
            # Matrix exponent for the succession of full pitches :
            # Name PP : P for "pitches", P for "propagation matrix"
            left_idx = PCP.shape[:-2]
            pp = [ numpy.linalg.matrix_power(PCP[i],fp)
                    for i in numpy.ndindex(left_idx) ]
            PP = numpy.array(pp)
            right_idx = PP.shape[-2:]
            PP.shape = left_idx + right_idx # shape : (Kx,k0,4,4)

            # Cumulative products for the slices on the left
            p = []
            CP = numpy.zeros(AP.shape)
            for ms in m_s:
                # Cumulative products of the propagation matrices :
                CP[ms] = P[ms]
                for m in range(ms+1,M):           # matrix product :
                    CP[m] = (AP[m][...,:,:,newaxis] * 
                              CP[m-1][...,newaxis,:,:]).sum(axis=-2)
                p.append(CP[-1])
            LP = numpy.array(p)
 
            # Cumulative products for the slices on the right
            p = []
            # Preparation of an array of identity matrices.
            ID = ones(AP.shape[1:]) * numpy.identity(4) 
            # shape : (Kx,k0,4,4) ; note the broadcasting. 
            for ms in m_s:
                # Cumulative products of the propagation matrices :
                CP[0] = ZP
                # Number of slices on the right :
                me = (ms+N)%M
                for m in range(me):           # matrix product :
                    CP[m+1] = (AP[m][...,:,:,newaxis] * 
                                CP[m][...,newaxis,:,:]).sum(axis=-2)
                p.append(CP[me])
            RP = numpy.array(p)
            
            # Total propagation matrix for the structure : RP*PP*LP
            P = (PP[...,:,:,newaxis] * LP[...,newaxis,:,:]).sum(axis=-2)
            P = (RP[...,:,:,newaxis] * P[...,newaxis,:,:]).sum(axis=-2)
            return P

  
