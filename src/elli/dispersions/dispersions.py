# Encoding: utf-8
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt
import scipy.constants as sc
from scipy.special import gamma, digamma, dawsn
import scipy.interpolate

from .base_dispersion import Dispersion
from ..math import lambda2E


class ConstantRefractiveIndex(Dispersion):
    """Constant refractive index."""

    single_params_template = {"n": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("n") ** 2


class EpsilonInf(Dispersion):
    """Constant epsilon infinity."""

    single_params_template = {"eps": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("eps")


class Cauchy(Dispersion):
    """Cauchy dispersion law.

    Cauchy coefficients: n0, n1, n2, k0, k1, k2
    coefficients defined for λ in nm

    n(λ) = n0 + 100 * n1/λ² + 10e7 n2/λ^4
    k(λ) = k0 + 100 * k1/λ² + 10e7 k2/λ^4
    """

    single_params_template = {"n0": 1.5, "n1": 0, "n2": 0, "k0": 0, "k1": 0, "k2": 0}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        refr_index = (
            self.single_params.get("n0")
            + 1e2 * self.single_params.get("n1") / lbda ** 2
            + 1e7 * self.single_params.get("n2") / lbda ** 4
            + 1j
            * (
                self.single_params.get("k0")
                + 1e2 * self.single_params.get("k1") / lbda ** 2
                + 1e7 * self.single_params.get("k2") / lbda ** 4
            )
        )
        return refr_index ** 2


class Sellmeier(Dispersion):
    """Creates a Sellmeier dispersion law.

    Sellmeier coefficients [A1, B1], [A1, B1],...
      Ai : coefficient for n² contribution
      Bi : resonance wavelength (µm^-2)

    ε(λ) = 1 + Σi Ai × λ²/(λ² - Bi)
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "B": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        lbda = lbda / 1e3
        return 1 + sum(
            c.get("A") * lbda ** 2 / (lbda ** 2 - c.get("B")) for c in self.rep_params
        )


class DrudeEnergy(Dispersion):
    """Creates a Drude model.

    Drude coefficients ϵinf, A, Γ
    ϵinf : epsilon infinity
    A : Amplitude of Drude oscillator (eV^2)
    Γ : Broadening of Drude oscillator (eV)
    """

    single_params_template = {"A": 1, "gamma": 1}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        return self.single_params.get("A") / (
            energy ** 2 - 1j * self.single_params.get("gamma") * energy
        )


class DrudeResistivity(Dispersion):
    """Creates a Drude model.

    Drude coefficients ϵinf, ρopt, τ
    ϵinf : epsilon infinity
    ρopt : optical resistivity (Ω-cm)
    τ : Mean scattering time (s)
    """

    single_params_template = {"rho_opt": 1, "tau": 1}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        hbar = sc.value("Planck constant in eV/Hz") / 2 / np.pi
        eps0 = sc.value("vacuum electric permittivity") * 1e-2

        return hbar ** 2 / (
            eps0
            * self.single_params.get("rho_opt")
            * (self.single_params.get("tau") * energy ** 2 - 1j * hbar * energy)
        )


class LorentzLambda(Dispersion):
    """Creates a Lorentz dispersion law, with wavelength coefficients.

    Lorentz coefficients [A1, λ1, ζ1], [A2, λ2, ζ2],...
      Bi : coefficient
      λi : resonance wavelength (nm)
      ζi :

    ε(λ) = 1 + Σi Ai × λ² / (λ² - λi² + j ζi λ)
    """

    single_params_templage = {}
    rep_params_template = {"A": 1, "lambda": 1, "gamma": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return 1 + sum(
            c.get("A")
            * lbda ** 2
            / (lbda ** 2 - c.get("lambda") ** 2 - 1j * c.get("gamma") * lbda)
            for c in self.rep_params
        )


class LorentzEnergy(Dispersion):
    """Creates a Lorentz dispersion law, with energy coefficients.

    Lorentz coefficients [A1, E1, Γ1], [A2, E2, Γ2],...
      Ai : coefficient
      Ei : resonance Energy (eV)
      Γi :

    ε(E) = 1 + Σi Ai /(E²-Ei²+j Γi E)
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 1, "gamma": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        return 1 + sum(
            c.get("A") / (c.get("E") ** 2 - energy ** 2 - 1j * c.get("gamma") * energy)
            for c in self.rep_params
        )


class Gauss(Dispersion):
    """Gauss model with energy parameters.
    Gauss coefficients ϵinf, [A1, E1, Γ1], [A2, E2, Γ2],...
        ϵinf : infinity dielectric constant
        Ai : Amplitude of ith Gaussian
        Ei : Central energy of ith Gaussian (eV)
        Γ1 : Broadening of ith Gaussian (eV)

    References:
    D. De Sousa Meneses, M. Malki, P. Echegut, J. Non-Cryst. Solids 351, 769-776 (2006)
    K.-E. Peiponen, E.M. Vartiainen, Phys. Rev. B. 44, 8301 (1991)
    H. Fujiwara, R. W. Collins, Spectroscopic Ellipsometry for Photovoltaics Volume 1, Springer International Publishing AG, 2018, p. 137
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 1, "gamma": 1}

    def dielectricFunction(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        ftos = 2 * sqrt(np.log(2))
        return sum(
            2
            * c.get("A")
            / sqrt(np.pi)
            * (
                dawsn(ftos * (energy + c.get("E")) / c.get("gamma"))
                - dawsn(ftos * (energy - c.get("E")) / c.get("gamma"))
            )
            + 1j
            * (
                c.get("A")
                * np.exp(-((ftos * (energy - c.get("E")) / c.get("gamma")) ** 2))
                - c.get("A")
                * np.exp(-((ftos * (energy + c.get("E")) / c.get("gamma")) ** 2))
            )
            for c in self.rep_params
        )


class TaucLorentz(Dispersion):
    """Tauc-Lorentz model by Jellison and Modine

    Tauc-Lorentz coefficients Eg, eps_inf, [A1, E1, C1], [A2, E2, C2],...
          Eg : optical band gap energy (eV)
          eps_inf : epsilon infinity
          Ai : Strength of ith absorption (eV). Typically 10 < Ai < 200
          Ei : lorentz resonance energy (eV). Always Eg < Ei
          Ci : lorentz broadening (eV). Typically 0 < Ci < 10
    Literature:
        G.E. Jellision and F.A. Modine, Appl. Phys. Lett. 69 (3), 371-374 (1996)
        Erratum, G.E. Jellison and F.A. Modine, Appl. Phys. Lett 69 (14), 2137 (1996)
        H. Chen, W.Z. Shen, Eur. Phys. J. B. 43, 503-507 (2005)
    """

    single_params_template = {"Eg": 1}
    rep_params_template = {"A": 1, "E": 1, "C": 1}

    @staticmethod
    def eps2(E, Eg, Ai, Ei, Ci):
        gamma2 = sqrt(Ei ** 2 - Ci ** 2 / 2) ** 2
        alpha = sqrt(4 * Ei ** 2 - Ci ** 2)
        aL = (
            (Eg ** 2 - Ei ** 2) * E ** 2
            + Eg ** 2 * Ci ** 2
            - Ei ** 2 * (Ei ** 2 + 3 * Eg ** 2)
        )
        aA = (E ** 2 - Ei ** 2) * (Ei ** 2 + Eg ** 2) + Eg ** 2 * Ci ** 2
        zeta4 = (E ** 2 - gamma2) ** 2 + alpha ** 2 * Ci ** 2 / 4

        # fmt: off
        return (
            Ai*Ci*aL/2.0/np.pi/zeta4/alpha/Ei*np.log((Ei**2 + Eg**2 + alpha*Eg)/(Ei**2 + Eg**2 - alpha*Eg)) - \
            Ai*aA/np.pi/zeta4/Ei*(np.pi - np.arctan((2.0*Eg + alpha)/Ci) + np.arctan((alpha - 2.0*Eg)/Ci)) + \
            2.0*Ai*Ei*Eg/np.pi/zeta4/alpha*(E**2 - gamma2)*(np.pi + 2.0*np.arctan(2.0/alpha/Ci*(gamma2 - Eg**2))) - \
            Ai*Ei*Ci*(E**2 + Eg**2)/np.pi/zeta4/E*np.log(abs(E - Eg)/(E + Eg)) + \
            2.0*Ai*Ei*Ci*Eg/np.pi/zeta4 * \
            np.log(abs(E - Eg) * (E + Eg) / sqrt((Ei**2 - Eg**2)**2 + Eg**2 * Ci**2))
        )
        # fmt: on

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        energy_g = self.single_params.get("Eg")
        return sum(
            1j
            * (
                c.get("A")
                * c.get("E")
                * c.get("gamma")
                * (energy - energy_g) ** 2
                / (
                    (energy ** 2 - c.get("E") ** 2) ** 2
                    + c.get("gamma") ** 2 * energy ** 2
                )
                / energy
            )
            * np.heaviside(energy - energy_g, 0)
            + self.eps2(energy, energy_g, c.get("A"), c.get("E"), c.get("gamma"))
            for c in self.rep_params
        )


class HighEnergyBands(Dispersion):
    single_params_template = {"A": 1, "E_xsi": 1}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)

        a = -((self.single_params.get("E_xsi") - E) ** 2) / E ** 3
        b = (self.single_params.get("E_xsi") + E) ** 2 / E ** 3

        eps_r = (
            3
            * self.single_params.get("E_xsi")
            / np.pi
            / E ** 2
            * (
                a * np.log(np.abs(1 - E / self.single_params.get("E_xsi")))
                + b * np.log(np.abs(1 + E / self.single_params.get("E_xsi")))
                - 2 / 3 / self.single_params.get("E_xsi")
                - 2 * self.single_params.get("E_xsi") / E ** 2
            )
        )
        eps_i = (
            3
            * self.single_params.get("E_xsi")
            * (np.abs(E) - self.single_params.get("E_xsi")) ** 2
            / E ** 5
            * np.heaviside(np.abs(E) - self.single_params.get("E_xsi"), 0)
        )

        return self.single_params.get("A") * (eps_r + 1j * eps_i)


class Tanguy(Dispersion):
    """Fractional dimensional Tanguy model

    Tanguy coefficients A, d, gamma, R, Eg, a, b
          A : Amplitude (eV)
          d : dimensionality 1 < d <= 3
          gam: excitonic broadening (eV)
          R : excitonic binding energy (eV²)
          Eg : optical band gap energy (eV)
          a : Sellmeier coefficient for background dielectric constant (eV²)
          b : Sellmeier coefficient for background dielectric constant (eV²)
    """

    single_params_template = {
        "A": 1,
        "d": 3,
        "gamma": 1,
        "R": 1,
        "Eg": 1,
        "a": 0,
        "b": 0,
    }
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        E = lambda2E(lbda)
        A = self.single_params.get("A")
        d = self.single_params.get("d")
        gam = self.single_params.get("gamma")
        R = self.single_params.get("R")
        Eg = self.single_params.get("Eg")
        a = self.single_params.get("a")
        b = self.single_params.get("b")

        return (
            1
            + a / (b - E ** 2)
            + A
            * R ** (d / 2 - 1)
            / (E + 1j * gam) ** 2
            * (
                Tanguy.g(Tanguy.xsi(E + 1j * gam, R, Eg), d)
                + Tanguy.g(Tanguy.xsi(-E - 1j * gam, R, Eg), d)
                - 2 * Tanguy.g(Tanguy.xsi(E * 0, R, Eg), d)
            )
        )

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
        return (
            2
            * np.pi
            * gamma(D / 2 + xsi)
            / gamma(D / 2) ** 2
            / gamma(1 - D / 2 + xsi)
            / xsi ** (d - 2)
            * (1 / np.tan(np.pi * (D / 2 - xsi)) - 1 / np.tan(np.pi * D))
        )


class Poles(Dispersion):
    """Disperion law for an UV and IR pole,
    i.e. Lorentz oscillators outside the fitting spectral range"""

    single_params_template = {"A_ir": 1, "A_uv": 1, "E_uv": 3}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        return self.single_params.get("A_ir") / energy ** 2 + self.single_params.get(
            "A_uv"
        ) / (self.single_params.get("E_uv") ** 2 - energy ** 2)


class Table(Dispersion):
    """Dispersion law specified by a table"""

    single_params_template = {"lbda": [], "n": []}
    rep_params_template = {}

    def __init__(self, **kwargs) -> None:
        """Create a dispersion law from a refraction index list.

        'lbda'  : Wavelength list (in nm)
        'n'     : Refractive index values (can be complex)
                  (n" > 0 for an absorbing material)
        """
        super().__init__(**kwargs)
        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("n") ** 2,
            kind="cubic",
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)


class TableEpsilon(Dispersion):
    """Dispersion law specified by a table"""

    single_params_template = {"lbda": [], "epsilon": []}
    rep_params_template = {}

    def __init__(self, **kwargs) -> None:
        """Create a dispersion law from a dielectric constant list.

        'lbda'  : Tuple with (Wavelength list, unit), or Wavelength list (in nm)
        'ε'     : Refractive index values (can be complex)
        """
        super().__init__(**kwargs)

        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("epsilon"),
            kind="cubic",
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
