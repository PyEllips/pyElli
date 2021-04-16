# Encoding: utf-8
import numpy as np
import scipy.constants as sc
from scipy.special import gamma, digamma, dawsn
import scipy.interpolate
from numpy.lib.scimath import sqrt

UnitConversion = {
    'm': 1,
    'cm': 1e-2,
    'mm': 1e-3,
    'µm': 1e-6,
    'um': 1e-6,
    'nm': 1e-9,
    'A': 1e-10,
    'Å': 1e-10,
    'pm': 1e-12
}

def lambda2E(value, unit='nm'):
    '''Returns the Energy in eV of the given wavelength in [unit] (default 'nm')'''
    return 1239.8419840550368 / (value * UnitConversion[unit] / 1e-9)

class DispersionLaw:
    """Dispersion law (abstract class).

    Funktions provided for derived classes:
    * getDielectric(lbda) : returns dielectric constant for wavelength 'lbda'
    * getRefractiveIndex(lbda) : returns refractive index for wavelength 'lbda'
    """

    dielectricFunction = lambda lbda, unit: 0 * 1j       # Complex dielectric function

    def __init__(self):
        """Creates a new dispersion law -- abstract class"""
        raise NotImplementedError("Should be implemented in derived classes")

    def __add__(self, other):
        """Add up the dielectric function of multiple models"""
        return DispersionSum(self, other)

    def getDielectricConj(self, lbda, unit='nm'):
        """Returns the conjugated dielectric constant for wavelength 'lbda' default unit (nm)
        in the convention ε1 - iε2."""
        return np.conjugate(self.dielectricFunction(lbda, unit))

    def getRefractiveIndexConj(self, lbda, unit='nm'):
        """Returns the conjugated refractive index for wavelength 'lbda' default unit (nm)
        in the convention n - ik."""
        return sqrt(np.conjugate(self.dielectricFunction(lbda, unit)))

    def getDielectric(self, lbda, unit='nm'):
        """Returns the dielectric constant for wavelength 'lbda' default unit (nm)
        in the convention ε1 + iε2."""
        return self.dielectricFunction(lbda, unit)

    def getRefractiveIndex(self, lbda, unit='nm'):
        """Returns the refractive index for wavelength 'lbda' default unit (nm)
        in the convention n + ik."""
        return sqrt(self.dielectricFunction(lbda, unit))


class DispersionSum(DispersionLaw):
    """Representation for a sum of two dispersions"""

    def __init__(self, disp1, disp2):

        self.dielectricFunction = lambda lbda, unit: \
            disp1.dielectricFunction(lbda, unit) + disp2.dielectricFunction(lbda, unit)


class DispersionLess(DispersionLaw):
    """Constant Dispersion law, therefor no dispersion. """

    def __init__(self, n=None):
        """Create a dispersion law with a constant refraction index.

        'n'     : Refractive index value (can be complex)
                  (n" > 0 for an absorbing material)
        """
        self.n = n

        def dielectricFunction(lbda, unit):
            return self.n**2

        self.dielectricFunction = dielectricFunction


class DispersionCauchy(DispersionLaw):
    """Sellmeier dispersion law equation."""

    def __init__(self, n0=1.5, n1=0, n2=0, k0=0, k1=0, k2=0):
        """Creates a Cauchy dispersion law.

        Cauchy coefficients: n0, n1, n2, k0, k1, k2
        coefficients defined for λ in nm

        n(λ) = n0 + 100 * n1/λ² + 10e7 n2/λ^4
        k(λ) = k0 + 100 * k1/λ² + 10e7 k2/λ^4
        """
        self.n0 = n0
        self.n1 = n1
        self.n2 = n2
        self.k0 = k0
        self.k1 = k1
        self.k2 = k2

        def dielectricFunction(lbda, unit='nm'):
            # Convert wavelength to nm
            lbda = lbda * UnitConversion[unit] / UnitConversion['nm']

            N = self.n0 + 1e2 * self.n1/lbda**2 + 1e7 * self.n2/lbda**4 \
                + 1j * (self.k0 + 1e2 * self.k1/lbda**2 + 1e7 * self.k2/lbda**4)
            return N**2

        self.dielectricFunction = dielectricFunction


class DispersionSellmeier(DispersionLaw):
    """Sellmeier dispersion law equation."""

    def __init__(self, *coeffs):
        """Creates a Sellmeier dispersion law.

        Sellmeier coefficients [A1, B1], [A1, B1],...
          Ai : coefficient for n² contribution
          Bi : resonance wavelength (µm^-2)

        ε(λ) = 1 + Σi Ai × λ²/(λ² - Bi)
        """
        self.coeffs = coeffs

        def dielectricFunction(lbda, unit='nm'):
            lbda = lbda * UnitConversion[unit] / UnitConversion['µm']

            return 1 + sum(Ai * lbda**2 / (lbda**2 - Bi)
                           for Ai, Bi in self.coeffs)

        self.dielectricFunction = dielectricFunction


class DispersionDrudeEnergy(DispersionLaw):
    """Drude dispersion with energy paramters."""

    def __init__(self, *coeffs):
        """Creates a Drude model.

        Drude coefficients ϵinf, A, Γ
        ϵinf : epsilon infinity
        A : Amplitude of Drude oscillator (eV^2)
        Γ : Broadening of Drude oscillator (eV)
        """
        self.coeffs = coeffs

        def dielectricFunction(lbda, unit='nm'):
            E = lambda2E(lbda, unit)
            return self.coeffs[0] + self.coeffs[1] / (E**2 - 1j * self.coeffs[2] * E)

        self.dielectricFunction = dielectricFunction


class DispersionDrudeResistivity(DispersionLaw):
    """Drude dispersion with resistivity paramters."""

    def __init__(self, *coeffs):
        """Creates a Drude model.

        Drude coefficients ϵinf, ρopt, τ
        ϵinf : epsilon infinity
        ρopt : optical resistivity (Ω-cm)
        τ : Mean scattering time (s)
        """
        self.coeffs = coeffs
        hbar = sc.value("Planck constant in eV/Hz") / 2 / np.pi
        eps0 = sc.value("vacuum electric permittivity") * 1e-2

        def dielectricFunction(lbda, unit='nm'):
            E = lambda2E(lbda, unit)
            return self.coeffs[0] + hbar**2 / (eps0 * self.coeffs[1] * (self.coeffs[2] * E**2 - 1j * hbar * E))

        self.dielectricFunction = dielectricFunction


class DispersionLorentzLambda(DispersionLaw):
    """Lorentz dispersion law equation, with wavelength coefficients."""

    def __init__(self, *coeffs):
        """Creates a Lorentz dispersion law, with wavelength coefficients.

        Lorentz coefficients [A1, λ1, ζ1], [A2, λ2, ζ2],...
          Bi : coefficient
          λi : resonance wavelength (nm)
          ζi :

        ε(λ) = 1 + Σi Ai × λ² / (λ² - λi² + j ζi λ)
        """
        self.coeffs = coeffs

        def dielectricFunction(lbda, unit='nm'):
            lbda = lbda * UnitConversion[unit] / UnitConversion['nm']

            return 1 + sum(Ai * lbda**2 / (lbda**2 - Li**2 - 1j * Zi * lbda)
                           for Ai, Li, Zi in self.coeffs)

        self.dielectricFunction = dielectricFunction


class DispersionLorentzEnergy(DispersionLaw):
    """Lorentz dispersion law equation, with energy coefficients."""

    def __init__(self, *coeffs):
        """Creates a Lorentz dispersion law, with energy coefficients.

        Lorentz coefficients [A1, E1, Γ1], [A2, E2, Γ2],...
          Ai : coefficient
          Ei : resonance Energy (eV)
          Γi :

        ε(E) = 1 + Σi Ai /(E²-Ei²+j Γi E)
        """
        self.coeffs = coeffs

        def dielectricFunction(lbda, unit='nm'):
            E = lambda2E(lbda, unit)
            return 1 + sum(Ai / (Ei**2 - E**2 - 1j * Ci * E)
                           for Ai, Ei, Ci in self.coeffs)

        self.dielectricFunction = dielectricFunction


class DispersionGauss(DispersionLaw):
    """Gauss model with energy parameters.
        References:
        D. De Sousa Meneses, M. Malki, P. Echegut, J. Non-Cryst. Solids 351, 769-776 (2006)
        K.-E. Peiponen, E.M. Vartiainen, Phys. Rev. B. 44, 8301 (1991)
        H. Fujiwara, R. W. Collins, Spectroscopic Ellipsometry for Photovoltaics Volume 1, Springer International Publishing AG, 2018, p. 137
    """

    def __init__(self, eps_inf, *coeffs):
        """Creates a Gauss model

        Gauss coefficients ϵinf, [A1, E1, Γ1], [A2, E2, Γ2],...
        ϵinf : infinity dielectric constant
        Ai : Amplitude of ith Gaussian
        Ei : Central energy of ith Gaussian (eV)
        Γ1 : Broadening of ith Gaussian (eV)
        """
        self.coeffs = coeffs
        ftos = 2 * sqrt(np.log(2))

        def dielectricFunction(lbda, unit='nm'):
            E = lambda2E(lbda, unit)
            return eps_inf + sum(2 * Ai / sqrt(np.pi) * (dawsn(ftos * (E + Ei) / gami) - dawsn(ftos * (E - Ei) / gami)) -
                                 1j * (Ai * np.exp(-(ftos * (E - Ei) / gami)**2) - Ai * np.exp(-(ftos * (E + Ei) / gami)**2))
                                 for Ai, Ei, gami in self.coeffs)

        self.dielectricFunction = dielectricFunction


class DispersionTaucLorentz(DispersionLaw):
    """Tauc-Lorentz model by Jellison and Modine
        Literature:
            G.E. Jellision and F.A. Modine, Appl. Phys. Lett. 69 (3), 371-374 (1996)
            Erratum, G.E. Jellison and F.A. Modine, Appl. Phys. Lett 69 (14), 2137 (1996)
            H. Chen, W.Z. Shen, Eur. Phys. J. B. 43, 503-507 (2005)
    """

    def __init__(self, *coeffs):
        """Creates a Tauc-Lorentz model.

        Tauc-Lorentz coefficients Eg, eps_inf, [A1, E1, C1], [A2, E2, C2],...
          Eg : optical band gap energy (eV)
          eps_inf : epsilon infinity
          Ai : Strength of ith absorption (eV). Typically 10 < Ai < 200
          Ei : lorentz resonance energy (eV). Always Eg < Ei
          Ci : lorentz broadening (eV). Typically 0 < Ci < 10
        """
        self.coeffs = coeffs

        def eps2(E, Eg, Ai, Ei, Ci):
            gamma2 = sqrt(Ei**2 - Ci**2 / 2)**2
            alpha = sqrt(4 * Ei**2 - Ci**2)
            aL = (Eg**2 - Ei**2) * E**2 + Eg**2 * Ci**2 - Ei**2 * (Ei**2 + 3 * Eg**2)
            aA = (E**2 - Ei**2) * (Ei**2 + Eg**2) + Eg**2 * Ci**2
            zeta4 = (E**2 - gamma2)**2 + alpha**2 * Ci**2 / 4

            return Ai*Ci*aL/2.0/np.pi/zeta4/alpha/Ei*np.log((Ei**2 + Eg**2 + alpha*Eg)/(Ei**2 + Eg**2 - alpha*Eg)) - \
                Ai*aA/np.pi/zeta4/Ei*(np.pi - np.arctan((2.0*Eg + alpha)/Ci) + np.arctan((alpha - 2.0*Eg)/Ci)) + \
                2.0*Ai*Ei*Eg/np.pi/zeta4/alpha*(E**2 - gamma2)*(np.pi + 2.0*np.arctan(2.0/alpha/Ci*(gamma2 - Eg**2))) - \
                Ai*Ei*Ci*(E**2 + Eg**2)/np.pi/zeta4/E*np.log(abs(E - Eg)/(E + Eg)) + \
                2.0*Ai*Ei*Ci*Eg/np.pi/zeta4*np.log(abs(E - Eg) * (E + Eg) / sqrt((Ei**2 - Eg**2)**2 + Eg**2 * Ci**2))

        def dielectricFunction(lbda, unit='nm'):
            E = lambda2E(lbda, unit)
            Eg = self.coeffs[0]
            eps_inf = self.coeffs[1]
            return eps_inf + np.conjugate(sum(1j * (Ai * Ei * Ci * (E - Eg)**2 / ((E**2 - Ei**2)**2 + Ci**2 * E**2) / E) * np.heaviside(E - Eg, 0) +
                                              eps2(E, Eg, Ai, Ei, Ci)
                                              for Ai, Ei, Ci in self.coeffs[2:]))

        self.dielectricFunction = dielectricFunction


class DispersionTanguy(DispersionLaw):
    """Fractional dimensional Tanguy model"""

    def __init__(self, A, d, gam, R, Eg, a, b):
        """Creates a Tanguy dispersion model

        Tanguy coefficients A, d, gamma, R, Eg, a, b
          A : Amplitude (eV)
          d : dimensionality 1 < d <= 3
          gam: excitonic broadening (eV)
          R : excitonic binding energy (eV²)
          Eg : optical band gap energy (eV)
          a : Sellmeier coefficient for background dielectric constant (eV²)
          b : Sellmeier coefficient for background dielectric constant (eV²)
        """
        def dielectricFunction(lbda, unit='nm'):
            E = lambda2E(lbda, unit)
            return np.conjugate(1 + a / (b - E**2) +
                                A * R**(d/2 - 1) / (E + 1j * gam)**2 *
                                (DispersionTanguy.g(DispersionTanguy.xsi(E + 1j * gam, R, Eg), d) +
                                 DispersionTanguy.g(DispersionTanguy.xsi(-E - 1j * gam, R, Eg), d) -
                                 2 * DispersionTanguy.g(DispersionTanguy.xsi(E*0, R, Eg), d)))

        self.dielectricFunction = dielectricFunction

    @staticmethod
    def xsi(z, R, Eg):
        return sqrt(R / (Eg - z))

    @staticmethod
    def g(xsi, d):
        if d == 2:
            return 2 * np.log(xsi) - 2 * digamma(0.5 - xsi)
        if d == 3:
            return 2 * np.log(xsi) - 2 * digamma(1 - xsi) - 1 / xsi

        D = d - 1
        return 2 * np.pi * gamma(D/2 + xsi) / gamma(D/2)**2 / gamma(1 - D/2 + xsi) / xsi**(d - 2) * \
            (1 / np.tan(np.pi * (D/2 - xsi)) - 1 / np.tan(np.pi * D))


class DispersionTable(DispersionLaw):
    """Dispersion law specified by a table"""

    def __init__(self, lbda=None, n=None, unit='nm'):
        """Create a dispersion law from a refraction index list.

        'lbda'  : Wavelength list (nm)
        'n'     : Refractive index values (can be complex)
                  (n" > 0 for an absorbing material)
        """
        self.interpolation = scipy.interpolate.interp1d(
            lbda * UnitConversion[unit], n**2, kind='cubic')

        def dielectricFunction(lbda, unit='nm'):
            lbda = lbda * UnitConversion[unit]
            return self.interpolation(lbda)

        self.dielectricFunction = dielectricFunction


class DispersionTableEpsilon(DispersionLaw):
    """Dispersion law specified by a table"""

    def __init__(self, lbda=None, epsilon=None, unit='nm'):
        """Create a dispersion law from a dielectric constant list.

        'lbda'  : Wavelength list (nm)
        'ε'     : Refractive index values (can be complex)
        """
        self.interpolation = scipy.interpolate.interp1d(
            lbda * UnitConversion[unit], epsilon, kind='cubic')

        def dielectricFunction(lbda, unit='nm'):
            lbda = lbda * UnitConversion[unit]
            return self.interpolation(lbda)

        self.dielectricFunction = dielectricFunction
