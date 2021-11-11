# Encoding: utf-8
from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt
import scipy.constants as sc
from scipy.special import gamma, digamma, dawsn
import scipy.interpolate
import pandas as pd

from .math import lambda2E


class DispersionLaw(ABC):
    """Dispersion law (abstract class).

    Functions provided for derived classes:
    * dielectricFunction(lbda) : returns dielectric constant for wavelength 'lbda'
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        pass

    def __add__(self, other: "DispersionLaw") -> "DispersionLaw":
        """Add up the dielectric function of multiple models"""
        return DispersionSum(self, other)

    def getDielectric(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns the dielectric constant for wavelength 'lbda' default unit (nm)
        in the convention ε1 + iε2."""
        return np.asarray(self.dielectricFunction(lbda), dtype=np.complex128)

    def getRefractiveIndex(self, lbda: npt.ArrayLike) -> npt.NDArray:
        """Returns the refractive index for wavelength 'lbda' default unit (nm)
        in the convention n + ik."""
        return sqrt(self.dielectricFunction(lbda))

    def getDielectric_df(self, lbda: npt.ArrayLike = None, conjugate=False) -> pd.DataFrame:
        lbda = np.linspace(200, 1000, 500) if lbda is None else lbda
        eps = self.getDielectricConj(lbda) if conjugate else self.getDielectric(lbda)

        return pd.DataFrame({'ϵ1': eps.real,
                             'ϵ2': eps.imag}, index=pd.Index(lbda, name='Wavelength'))

    def getRefractiveIndex_df(self, lbda: npt.ArrayLike = None, conjugate=False) -> pd.DataFrame:
        lbda = np.linspace(200, 1000, 500) if lbda is None else lbda
        eps = self.getRefractiveIndexConj(lbda) if conjugate else self.getRefractiveIndex(lbda)

        return pd.DataFrame({'ϵ1': eps.real,
                             'ϵ2': eps.imag}, index=pd.Index(lbda, name='Wavelength'))


class DispersionSum(DispersionLaw):
    """Representation for a sum of two dispersions"""

    def __init__(self, *dispersions: DispersionLaw) -> None:
        self.dispersions = dispersions

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        dielectricFunction = np.sum(disp.dielectricFunction(lbda) for disp in self.dispersions)
        return dielectricFunction


class DispersionLess(DispersionLaw):
    """Constant Dispersion law, therefor no dispersion. """

    def __init__(self, n: float) -> None:
        """Create a dispersion law with a constant refraction index.

        'n'     : Refractive index value (can be complex)
                  (n" > 0 for an absorbing material)
        """
        self.n = n

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.n**2


class DispersionCauchy(DispersionLaw):
    """Sellmeier dispersion law equation."""

    def __init__(self, n0: float = 1.5, n1: float = 0, n2: float = 0, k0: float = 0, k1: float = 0, k2: float = 0) -> None:
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

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        N = self.n0 + 1e2 * self.n1/lbda**2 + 1e7 * self.n2/lbda**4 \
            + 1j * (self.k0 + 1e2 * self.k1/lbda**2 + 1e7 * self.k2/lbda**4)
        return N**2


class DispersionSellmeier(DispersionLaw):
    """Sellmeier dispersion law equation."""

    def __init__(self, *coeffs) -> None:
        """Creates a Sellmeier dispersion law.

        Sellmeier coefficients [A1, B1], [A1, B1],...
          Ai : coefficient for n² contribution
          Bi : resonance wavelength (µm^-2)

        ε(λ) = 1 + Σi Ai × λ²/(λ² - Bi)
        """
        self.coeffs = coeffs

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        lbda = lbda / 1e3
        return 1 + sum(Ai * lbda**2 / (lbda**2 - Bi)
                       for Ai, Bi in self.coeffs)


class DispersionMgO(DispersionLaw):
    """Alternative form of the Sellmeier dispersion law equation"""

    def __init__(self, *coeffs) -> None:
        self.coeffs = coeffs

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        lbda = lbda / 1e3
        return self.coeffs[0] + \
            self.coeffs[1] * lbda ** 2 + \
            self.coeffs[2] * lbda**4 + \
            self.coeffs[3] / (lbda**2 - self.coeffs[4])


class DispersionDrudeEnergy(DispersionLaw):
    """Drude dispersion with energy paramters."""

    def __init__(self, *coeffs) -> None:
        """Creates a Drude model.

        Drude coefficients ϵinf, A, Γ
        ϵinf : epsilon infinity
        A : Amplitude of Drude oscillator (eV^2)
        Γ : Broadening of Drude oscillator (eV)
        """
        self.coeffs = coeffs

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        return self.coeffs[0] + self.coeffs[1] / (E**2 - 1j * self.coeffs[2] * E)


class DispersionDrudeResistivity(DispersionLaw):
    """Drude dispersion with resistivity paramters."""

    def __init__(self, *coeffs) -> None:
        """Creates a Drude model.

        Drude coefficients ϵinf, ρopt, τ
        ϵinf : epsilon infinity
        ρopt : optical resistivity (Ω-cm)
        τ : Mean scattering time (s)
        """
        self.coeffs = coeffs

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        hbar = sc.value("Planck constant in eV/Hz") / 2 / np.pi
        eps0 = sc.value("vacuum electric permittivity") * 1e-2

        return self.coeffs[0] + hbar**2 / (eps0 * self.coeffs[1] * (self.coeffs[2] * E**2 - 1j * hbar * E))


class DispersionLorentzLambda(DispersionLaw):
    """Lorentz dispersion law equation, with wavelength coefficients."""

    def __init__(self, *coeffs) -> None:
        """Creates a Lorentz dispersion law, with wavelength coefficients.

        Lorentz coefficients [A1, λ1, ζ1], [A2, λ2, ζ2],...
          Bi : coefficient
          λi : resonance wavelength (nm)
          ζi :

        ε(λ) = 1 + Σi Ai × λ² / (λ² - λi² + j ζi λ)
        """
        self.coeffs = coeffs

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return 1 + sum(Ai * lbda**2 / (lbda**2 - Li**2 - 1j * Zi * lbda)
                       for Ai, Li, Zi in self.coeffs)


class DispersionLorentzEnergy(DispersionLaw):
    """Lorentz dispersion law equation, with energy coefficients."""

    def __init__(self, *coeffs) -> None:
        """Creates a Lorentz dispersion law, with energy coefficients.

        Lorentz coefficients [A1, E1, Γ1], [A2, E2, Γ2],...
          Ai : coefficient
          Ei : resonance Energy (eV)
          Γi :

        ε(E) = 1 + Σi Ai /(E²-Ei²+j Γi E)
        """
        self.coeffs = coeffs

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        return 1 + sum(Ai / (Ei**2 - E**2 - 1j * Ci * E)
                       for Ai, Ei, Ci in self.coeffs)


class DispersionGauss(DispersionLaw):
    """Gauss model with energy parameters.
        References:
        D. De Sousa Meneses, M. Malki, P. Echegut, J. Non-Cryst. Solids 351, 769-776 (2006)
        K.-E. Peiponen, E.M. Vartiainen, Phys. Rev. B. 44, 8301 (1991)
        H. Fujiwara, R. W. Collins, Spectroscopic Ellipsometry for Photovoltaics Volume 1, Springer International Publishing AG, 2018, p. 137
    """

    def __init__(self, eps_inf, *coeffs) -> None:
        """Creates a Gauss model

        Gauss coefficients ϵinf, [A1, E1, Γ1], [A2, E2, Γ2],...
        ϵinf : infinity dielectric constant
        Ai : Amplitude of ith Gaussian
        Ei : Central energy of ith Gaussian (eV)
        Γ1 : Broadening of ith Gaussian (eV)
        """
        self.eps_inf = eps_inf
        self.coeffs = coeffs

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        ftos = 2 * sqrt(np.log(2))
        return self.eps_inf + sum(2 * Ai / sqrt(np.pi) *
                            (dawsn(ftos * (E + Ei) / gami) - dawsn(ftos * (E - Ei) / gami)) +
                            1j * (Ai * np.exp(-(ftos * (E - Ei) / gami)**2) -
                                    Ai * np.exp(-(ftos * (E + Ei) / gami)**2))
                            for Ai, Ei, gami in self.coeffs)


class DispersionTaucLorentz(DispersionLaw):
    """Tauc-Lorentz model by Jellison and Modine
        Literature:
            G.E. Jellision and F.A. Modine, Appl. Phys. Lett. 69 (3), 371-374 (1996)
            Erratum, G.E. Jellison and F.A. Modine, Appl. Phys. Lett 69 (14), 2137 (1996)
            H. Chen, W.Z. Shen, Eur. Phys. J. B. 43, 503-507 (2005)
    """

    def __init__(self, *coeffs) -> None:
        """Creates a Tauc-Lorentz model.

        Tauc-Lorentz coefficients Eg, eps_inf, [A1, E1, C1], [A2, E2, C2],...
          Eg : optical band gap energy (eV)
          eps_inf : epsilon infinity
          Ai : Strength of ith absorption (eV). Typically 10 < Ai < 200
          Ei : lorentz resonance energy (eV). Always Eg < Ei
          Ci : lorentz broadening (eV). Typically 0 < Ci < 10
        """
        self.coeffs = coeffs

    @staticmethod
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
            2.0*Ai*Ei*Ci*Eg/np.pi/zeta4 * \
            np.log(abs(E - Eg) * (E + Eg) / sqrt((Ei**2 - Eg**2)**2 + Eg**2 * Ci**2))

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        Eg = self.coeffs[0]
        eps_inf = self.coeffs[1]
        return eps_inf + sum(1j * (Ai * Ei * Ci * (E - Eg)**2 / ((E**2 - Ei**2)**2 + Ci**2 * E**2) / E) * np.heaviside(E - Eg, 0) +
                             self.eps2(E, Eg, Ai, Ei, Ci)
                             for Ai, Ei, Ci in self.coeffs[2:])


class DispersionHighEnergyBands(DispersionLaw):

    def __init__(self, A, E_xsi) -> None:
        self.A = A
        self.E_xsi = E_xsi

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)

        a = -(self.E_xsi - E)**2 / E**3
        b = (self.E_xsi + E)**2 / E**3

        eps_r = 3 * self.E_xsi / np.pi / E**2 * (a * np.log(np.abs(1 - E / self.E_xsi)) +
                                                 b * np.log(np.abs(1 + E / self.E_xsi))
                                                 - 2 / 3 / self.E_xsi
                                                 - 2 * self.E_xsi / E**2)
        eps_i = 3 * self.E_xsi * (np.abs(E) - self.E_xsi)**2 / E**5 * \
            np.heaviside(np.abs(E) - self.E_xsi, 0)

        return self.A * (eps_r + 1j * eps_i)


class DispersionTanguy(DispersionLaw):
    """Fractional dimensional Tanguy model"""

    def __init__(self, A, d, gam, R, Eg, a, b) -> None:
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
        self.A = A
        self.d = d
        self.gam = gam
        self.R = R
        self.Eg = Eg
        self.a = a
        self.b = b

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        return (1 + self.a / (self.b - E**2) +
                self.A * self.R**(self.d/2 - 1) / (E + 1j * self.gam)**2 *
                (DispersionTanguy.g(DispersionTanguy.xsi(E + 1j * self.gam, self.R, self.Eg), self.d) +
                    DispersionTanguy.g(DispersionTanguy.xsi(-E - 1j * self.gam, self.R, self.Eg), self.d) -
                    2 * DispersionTanguy.g(DispersionTanguy.xsi(E*0, self.R, self.Eg), self.d)))

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


class DispersionPoles(DispersionLaw):
    """Disperion law for an UV and IR pole, i.e. Lorentz oscillators outside the fitting spectral range"""

    def __init__(self, A_ir, A_uv, E_uv) -> None:
        self.A_ir = A_ir
        self.A_uv = A_uv
        self.E_uv = E_uv

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        return self.A_ir / E**2 + self.A_uv / (self.E_uv**2 - E**2)


class DispersionTable(DispersionLaw):
    """Dispersion law specified by a table"""

    def __init__(self, lbda: npt.ArrayLike, n: npt.ArrayLike) -> None:
        """Create a dispersion law from a refraction index list.

        'lbda'  : Wavelength list (in nm)
        'n'     : Refractive index values (can be complex)
                  (n" > 0 for an absorbing material)
        """
        self.interpolation = scipy.interpolate.interp1d(lbda, n**2, kind='cubic')

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)


class DispersionTableEpsilon(DispersionLaw):
    """Dispersion law specified by a table"""

    def __init__(self, lbda: npt.ArrayLike, epsilon: npt.ArrayLike) -> None:
        """Create a dispersion law from a dielectric constant list.

        'lbda'  : Tuple with (Wavelength list, unit), or Wavelength list (in nm)
        'ε'     : Refractive index values (can be complex)
        """
        self.interpolation = scipy.interpolate.interp1d(lbda, epsilon, kind='cubic')

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
