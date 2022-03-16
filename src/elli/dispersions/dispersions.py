# Encoding: utf-8
"""The dispersions are the central part of pyElli and the transfer-matrix method.
They describe the change of dielectric function or refractive index with wavlength.
In pyElli the default wavelength unit is nm.
Each dispersion has two distinct sets of parameters:
    * Parameters which can be given only once (single parameters).
    * Parameters which can be given in multiple sets (repeated parameters), e.g.
        a set of oscillator parameters.

The syntax for each of the parameter sets is different.
For the single parameters they are given in the class constructor:
    .. highlight:: python
    .. code-block:: python

        Cauchy(n0=1.458, n1=3.54e-3, n2=0, k0=0, k1=0, k2=0)

Repeated parameters are added via the add() function:
    .. highlight:: python
    .. code-block:: python

        Sellmeier().add(A=1, B=1).add(A=1, B=2)

For dispersions having single and repeated parameters both are used:
    .. highlight:: python
    .. code-block:: python

        TaucLorentz(Eg=2).add(A=10, E=2.5, C=0.1)

If parameters are not fully provided, they are set to their respective default values.
The available parameters and their respective default values
are given in the respective class documentation.
"""
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt
import scipy.constants as sc
from scipy.special import gamma, digamma, dawsn
import scipy.interpolate

from .base_dispersion import Dispersion
from ..math import lambda2E


class ConstantRefractiveIndex(Dispersion):
    """Constant refractive index.

    Single parameters:
        n: 1

    Repeated parameters:
        --

    Output:
        ε(λ) = `n`^2"""

    single_params_template = {"n": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("n") ** 2


class EpsilonInf(Dispersion):
    """Constant epsilon infinity.

    Single parameters:
        eps: 1

    Repeated parameters:
        --

    Output:
        ε(λ) = `eps`"""

    single_params_template = {"eps": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("eps")


class Cauchy(Dispersion):
    """Cauchy dispersion.

    Single parameters:
        n0: Defaults to 1.5.
        n1: Defaults to 0. Unit in nm^2.
        n2: Defaults to 0. Unit in nm^4.
        k0: Defaults to 0.
        k1: Defaults to 0. Unit in nm^2.
        k2: Defaults to 0. Unit in nm^4.

    Repeated parameters:
        --

    Output:
        ε(λ)^2 = (
            n0 + 100 * n1/λ² + 10^7 n2/λ^4
            + 1j * (k0 + 100 * k1/λ² + 10^7 k2/λ^4)
        )
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
    """Sellmeier dispersion.

    Single parameters:
        --

    Repeated parameters:
        A: Coefficient for n² contribution. Defaults to 0.
        B: Resonance wavelength (µm^-2). Defaults to 0.

    Output:
        ε(λ) = 1 + Σi Ai × λ²/(λ² - Bi)
    """

    single_params_template = {}
    rep_params_template = {"A": 0, "B": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        lbda = lbda / 1e3
        return 1 + sum(
            c.get("A") * lbda ** 2 / (lbda ** 2 - c.get("B")) for c in self.rep_params
        )


class DrudeEnergy(Dispersion):
    """Drude dispersion model with parameters in units of energy.
    Drude models in the literature typically contain an additional epsilon infinity value.
    Use `EpsilonInf` to add this parameter or simply do DrudeEnergy() + eps_inf.

    Single parameters:
        A: Amplitude of Drude oscillator (eV^2). Defaults to 0.
        gamma: Broadening of Drude oscillator (eV). Defaults to 0.

    Repeated parameters:
        --

    Output:
        ε(E) = `A` / (E^2 - 1j * `gamma` * E)
    """

    single_params_template = {"A": 0, "gamma": 0}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        return self.single_params.get("A") / (
            energy ** 2 - 1j * self.single_params.get("gamma") * energy
        )


class DrudeResistivity(Dispersion):
    """Drude dispersion model with resistivity based parameters.
    Drude models in the literature typically contain an additional epsilon infinity value.
    Use `EpsilonInf` to add this parameter or simply do DrudeEnergy() + eps_inf.

    Single parameters:
        rho_opt: Optical resistivity (Ω-cm). Defaults to 1.
        tau: Mean scattering time (s). Defaults to 1.

    Repeated parameters:
        --

    Output:
       ε(E) = hbar / (eps0 * `rho_opt` * `tau` E^2 - 1j * hbar * E)
       where hbar is the planck constant divided by 2pi
       and eps0 is the vacuum dielectric permittivity.
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
    """Lorentz disperison law with parameters in units of wavelengths.

    Single parameters:
        --

    Repeated parameters:
        A: Amplitude of the oscillator. Defaults to 1.
        lambda: Resonance wavelength (nm). Defaults to 0.
        gamma: Broadening of the oscillator (nm). Defaults to 0.

    Output:
        ε(λ) = 1 + Σi `A`i * λ² / (λ² - `lambda`i² + 1j * `gamma`i * λ)
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "lambda": 0, "gamma": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return 1 + sum(
            c.get("A")
            * lbda ** 2
            / (lbda ** 2 - c.get("lambda") ** 2 - 1j * c.get("gamma") * lbda)
            for c in self.rep_params
        )


class LorentzEnergy(Dispersion):
    """Lorentz disperison law with parameters in units of energy.

    Single parameters:
        --

    Repeated parameters:
        A: Amplitude of the  oscillator. Defaults to 1.
        E: Resonance energy (eV). Defaults 0.
        gamma: Broadening of the oscillator (eV). Defaults to 0.

    Output:
        ε(E) = 1 + Σi `A`i / (E²-`E`i²+1j * `gamma`i * E)
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 0, "gamma": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        return 1 + sum(
            c.get("A") / (c.get("E") ** 2 - energy ** 2 - 1j * c.get("gamma") * energy)
            for c in self.rep_params
        )


class Gauss(Dispersion):
    """Gauss dispersion law.

    Single parameters:
        --

    Repeated parameters:
        A: Amplitude of the oscillator
        E: Central energy (eV)
        sigma: Broadening of the Gaussian (eV)

    Output:
        ε(E) = Σi 2 * `A`i / sqrt(π) *
                (D(2 * sqrt(2 * ln(2)) * (E + `E`i) / `sigma`) - D(2 * sqrt(2 * ln(2)) * (E - `E`i) / `sigma`)
                +1j * (`A` * exp(-(4*ln(2) * (E - `E`i)/ `sigma`)^2 - `A` * exp(-(4*ln(2) * (E + `E`i)/ `sigma`)^2)
        D is the Dawson function.

    References:
        D. De Sousa Meneses, M. Malki, P. Echegut, J. Non-Cryst. Solids 351, 769-776 (2006)
        K.-E. Peiponen, E.M. Vartiainen, Phys. Rev. B. 44, 8301 (1991)
        H. Fujiwara, R. W. Collins, Spectroscopic Ellipsometry for Photovoltaics Volume 1, Springer International Publishing AG, 2018, p. 137
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 1, "sigma": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        ftos = 2 * sqrt(np.log(2))
        return sum(
            2
            * c.get("A")
            / sqrt(np.pi)
            * (
                dawsn(ftos * (energy + c.get("E")) / c.get("sigma"))
                - dawsn(ftos * (energy - c.get("E")) / c.get("sigma"))
            )
            + 1j
            * (
                c.get("A")
                * np.exp(-((ftos * (energy - c.get("E")) / c.get("sigma")) ** 2))
                - c.get("A")
                * np.exp(-((ftos * (energy + c.get("E")) / c.get("sigma")) ** 2))
            )
            for c in self.rep_params
        )


class TaucLorentz(Dispersion):
    """Tauc-Lorentz dispersion law. Model by Jellison and Modine.

    Single parameters:
        Eg: Bandgap energy. Defaults to 1.

    Repeated parameters:
        A: Strength of the absorption. Typically 10 < A < 200. Defaults to 20.
        E: Lorentz resonance energy (eV). Always keep Eg < E!!. Defaults to 1.5.
        C: Lorentz broadening (eV). Typically 0 < Ci < 10. Defaults to 1.

    Output:
        The Tauc lorentz dispersion. Please refer to the references for a full formula.

    References:
        G.E. Jellision and F.A. Modine, Appl. Phys. Lett. 69 (3), 371-374 (1996)
        Erratum, G.E. Jellison and F.A. Modine, Appl. Phys. Lett 69 (14), 2137 (1996)
        H. Chen, W.Z. Shen, Eur. Phys. J. B. 43, 503-507 (2005)
    """

    single_params_template = {"Eg": 1}
    rep_params_template = {"A": 20, "E": 1.5, "C": 1}

    @staticmethod
    def eps1(E, Eg, Ai, Ei, Ci):
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
            (
                1j
                * (
                    c.get("A")
                    * c.get("E")
                    * c.get("C")
                    * (energy - energy_g) ** 2
                    / (
                        (energy ** 2 - c.get("E") ** 2) ** 2
                        + c.get("C") ** 2 * energy ** 2
                    )
                    / energy
                )
                * np.heaviside(energy - energy_g, 0)
                + self.eps1(energy, energy_g, c.get("A"), c.get("E"), c.get("C"))
            )
            for c in self.rep_params
        )


class Tanguy(Dispersion):
    """Fractional dimensional Tanguy model.
    This model is an analytical expression of Wannier excitons, including
    bound and unbound states.

    Single parameters:
          A: Amplitude (eV). Defaults to 1.
          d: Dimensionality 1 < d <= 3. Defaults to 3.
          gamma: Excitonic broadening (eV). Defaults to 0.1.
          R : excitonic binding energy (eV). Defaults to 0.1.
          Eg : optical band gap energy (eV). Defaults to 1.
          a : Sellmeier coefficient for background dielectric constant (eV²).
            Defaults to 0.
          b : Sellmeier coefficient for background dielectric constant (eV²).
            Defaults to 0.

    Repeated parameters.
        --

    Output:
        The Tanguy dispersion. Please refer to the references for a full formula.

    References:
        C. Tanguy, Phys. Rev. Lett. 75, 4090 (1995). Errata, Phys. Rev. Lett. 76, 716 (1996).
        C. Tanguy, Phys. Rev. B. 60. 10660 (1990).
    """

    single_params_template = {
        "A": 1,
        "d": 3,
        "gamma": 0.1,
        "R": 0.1,
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
    i.e. Lorentz oscillators outside the fitting spectral range and zero broadening.

    Single parameters:
        A_ir: IR Pole amplitude (eV^2). Defaults to 1.
        A_uv: UV Pole amplitude (eV^2). Defaults to 1.
        E_uv: UV Pole energy (eV). Defaults to 6.

    Repeated parameters:
        --

    Output:
        ε(E) = `A_ir` / E^2 + `A_uv` / (`E_uv`**2 - E**2)
    """

    single_params_template = {"A_ir": 1, "A_uv": 1, "E_uv": 6}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = lambda2E(lbda)
        return self.single_params.get("A_ir") / energy ** 2 + self.single_params.get(
            "A_uv"
        ) / (self.single_params.get("E_uv") ** 2 - energy ** 2)


class Table(Dispersion):
    """Dispersion specified by a table of wavelengths (nm) and refractive index values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        lbda (list): Wavelengths in nm. Defaults to [].
        epsilon: Complex refractive index values in the convention n + ik.
            Defaults to [].

    Repeated parameters:
        --

    Output:
        The interpolation in the given wavelength range.
    """

    single_params_template = {"lbda": np.linspace(0, 3000, 1000), "n": np.ones(1000)}
    rep_params_template = {}

    def __init__(self, *args, **kwargs) -> None:
        """Create a dispersion law from a refraction index list.

        'lbda'  : Wavelength list (in nm)
        'n'     : Complex refractive index values.
                  (n > 0 for an absorbing material)
        """
        super().__init__(*args, **kwargs)
        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("n") ** 2,
            kind="cubic",
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)


class TableEpsilon(Dispersion):
    """Dispersion specified by a table of wavelengths (nm) and dielectric function values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        lbda (list): Wavelengths in nm. Defaults to [].
        epsilon: Complex dielectric function values in the convention ε1 + iε2.
            Defaults to [].

    Repeated parameters:
        --

    Output:
        The interpolation in the given wavelength range.
    """

    single_params_template = {
        "lbda": np.linspace(0, 3000, 1000),
        "epsilon": np.ones(1000),
    }
    rep_params_template = {}

    def __init__(self, *args, **kwargs) -> None:
        """Create a dispersion law from a dielectric constant list.

        'lbda'  : Tuple with (Wavelength list, unit), or Wavelength list (in nm)
        'ε'     : Refractive index values (can be complex)
        """
        super().__init__(*args, **kwargs)

        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("epsilon"),
            kind="cubic",
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
