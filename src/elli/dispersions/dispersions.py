# Encoding: utf-8
"""The dispersions are the central part of pyElli and the transfer-matrix method.
They describe the change of dielectric function or refractive index with the wavelength.
In pyElli the default wavelength unit is nm.
Each dispersion has two distinct sets of parameters:

    * Parameters which can be given only once (single parameters).
    * Parameters which can be given in multiple sets (repeated parameters),
      e.g. a set of oscillator parameters.

The syntax for each of the parameter sets is different.
For the single parameters they are given in the class constructor:

    .. highlight:: python
    .. code-block:: python

        Cauchy(n0=1.458, n1=3.54e-3, n2=0, k0=0, k1=0, k2=0)

Repeated parameters are added via the add() function:

    .. highlight:: python
    .. code-block:: python

        Sellmeier().add(A=1, B=1).add(A=1, B=2)

For dispersions having both, single and repeated parameters can be used together:

    .. highlight:: python
    .. code-block:: python

        TaucLorentz(Eg=2).add(A=10, E=2.5, C=0.1)

If parameters are not fully provided, they are set to their respective default values.
The available parameters and their respective default values
are given in the respective class documentation.

All classes inherit from the abstract base class `Dispersion`_.
It provides basic functionality, such as returning dataframes or arrays
containing the wavelength dependent dielectric function of the
dispersion relation at current parameter set.

Dispersions can be added with the `+` operator, or if you want to chain
more than two dispersions together you may have a look at the `DispersionSum`_ class.
"""
import numpy as np
import numpy.typing as npt
from numpy.lib.scimath import sqrt
import scipy.constants as sc

# pylint: disable=no-name-in-module
from scipy.special import gamma, digamma, dawsn
import scipy.interpolate

from .base_dispersion import Dispersion, InvalidParameters
from ..math import conversion_wavelength_energy


class ConstantRefractiveIndex(Dispersion):
    r"""Constant refractive index.

    Single parameters:
        :n: The constant value of the refractive index. Defaults to 1.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(\lambda) = \boldsymbol{n}^2
    """

    single_params_template = {"n": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("n") ** 2


class EpsilonInf(Dispersion):
    r"""Constant epsilon infinity.

    Single parameters:
        :eps: Constant value for the constant epsilon. Defaults to 1.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(\lambda) = \textbf{eps}
    """

    single_params_template = {"eps": 1}
    rep_params_template = {}

    def dielectric_function(self, _: npt.ArrayLike) -> npt.NDArray:
        return self.single_params.get("eps")


class Cauchy(Dispersion):
    r"""Cauchy dispersion.

    Single parameters:
        :n0: Defaults to 1.5.
        :n1: Defaults to 0. Unit in nm\ :sup:`2`.
        :n2: Defaults to 0. Unit in nm\ :sup:`4`.
        :k0: Defaults to 0.
        :k1: Defaults to 0. Unit in nm\ :sup:`2`.
        :k2: Defaults to 0. Unit in nm\ :sup:`4`.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon^2(\lambda) =
            \boldsymbol{n_0} + 100  \boldsymbol{n_1}/\lambda^2 + 10^7 \boldsymbol{n_2}/\lambda^4
            + i (\boldsymbol{k_0} + 100 \boldsymbol{k_1}/\lambda^2
            + 10^7 \boldsymbol{k_2}/\lambda^4)
    """

    single_params_template = {"n0": 1.5, "n1": 0, "n2": 0, "k0": 0, "k1": 0, "k2": 0}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        refr_index = (
            self.single_params.get("n0")
            + 1e2 * self.single_params.get("n1") / lbda**2
            + 1e7 * self.single_params.get("n2") / lbda**4
            + 1j
            * (
                self.single_params.get("k0")
                + 1e2 * self.single_params.get("k1") / lbda**2
                + 1e7 * self.single_params.get("k2") / lbda**4
            )
        )
        return refr_index**2


class Sellmeier(Dispersion):
    r"""Sellmeier dispersion.

    Single parameters:
        --

    Repeated parameters:
        :A: Coefficient for n\ :sup:`2` contribution. Defaults to 0.
        :B: Resonance wavelength. Defaults to 0. Unit in µm\ :sup:`-2`.

    Output:
        .. math::
            \varepsilon(\lambda) = 1 + \sum_j \boldsymbol{A}_j
            \cdot \lambda^2 /(\lambda^2 - \boldsymbol{B}_j)

        With :math:`j` as the index of the respective oscillator.
    """

    single_params_template = {}
    rep_params_template = {"A": 0, "B": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        lbda = lbda / 1e3
        return 1 + sum(
            c.get("A") * lbda**2 / (lbda**2 - c.get("B")) for c in self.rep_params
        )


class DrudeEnergy(Dispersion):
    r"""Drude dispersion model with parameters in units of energy.
    Drude models in the literature typically contain an additional epsilon infinity value.
    Use `EpsilonInf` to add this parameter or simply add a number, e.g. DrudeEnergy() + 2, where
    2 is the value of epsilon infinity.

    Single parameters:
        :A: Amplitude of Drude oscillator. Defaults to 0. Unit in eV\ :sup:`2`
        :gamma: Broadening of Drude oscillator. Defaults to 0. Unit in eV.

    Repeated parameters:
        --

    Output:
        .. math::
            \varepsilon(E)
            = \boldsymbol{A} / (E^2 - i \cdot \boldsymbol{gamma} \cdot E)
    """

    single_params_template = {"A": 0, "gamma": 0}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        return self.single_params.get("A") / (
            energy**2 - 1j * self.single_params.get("gamma") * energy
        )


class DrudeResistivity(Dispersion):
    r"""Drude dispersion model with resistivity based parameters.
    Drude models in the literature typically contain an additional epsilon infinity value.
    Use `EpsilonInf` to add this parameter or simply do DrudeEnergy() + eps_inf.

    Single parameters:
        :rho_opt: Optical resistivity. Defaults to 1. Unit in Ω-cm.
        :tau: Mean scattering time. Defaults to 1. Unit in s.

    Repeated parameters:
        --

    Output:

        .. math::
            \varepsilon(E) = \hbar / (\varepsilon_0  \cdot
            \boldsymbol{rho\_opt} \cdot \boldsymbol{tau} \cdot E^2
            - i \cdot \hbar \cdot E)

       where :math:`\hbar` is the planck constant divided by :math:`2\pi`
       and :math:`\varepsilon_0` is the vacuum dielectric permittivity.
    """

    single_params_template = {"rho_opt": 1, "tau": 1}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        hbar = sc.value("Planck constant in eV/Hz") / 2 / np.pi
        eps0 = sc.value("vacuum electric permittivity") * 1e-2

        return hbar**2 / (
            eps0
            * self.single_params.get("rho_opt")
            * (self.single_params.get("tau") * energy**2 - 1j * hbar * energy)
        )


class LorentzLambda(Dispersion):
    r"""Lorentz dispersion law with parameters in units of wavelengths.

    Single parameters:
        --

    Repeated parameters:
        :A: Amplitude of the oscillator. Defaults to 1.
        :lambda_r: Resonance wavelength. Defaults to 0. Unit in nm.
        :gamma: Broadening of the oscillator. Defaults to 0. Unit in nm.

    Output:

        .. math::
            \varepsilon(\lambda) = 1 + \sum_j \boldsymbol{A}_j
            \cdot \lambda^2 / (\lambda^2 - \boldsymbol{lambda\_r}_j^2
            + i \cdot \boldsymbol{gamma}_j \cdot \lambda)

        The summation index :math:`j` refers to the respective oscillator.
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "lambda_r": 0, "gamma": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return 1 + sum(
            c.get("A")
            * lbda**2
            / (lbda**2 - c.get("lambda_r") ** 2 - 1j * c.get("gamma") * lbda)
            for c in self.rep_params
        )


class LorentzEnergy(Dispersion):
    r"""Lorentz dispersion law with parameters in units of energy.

    Single parameters:
        --

    Repeated parameters:
        :A: Amplitude of the oscillator. Defaults to 1.
        :E: Resonance energy. Defaults 0. Unit in eV.
        :gamma: Broadening of the oscillator. Defaults to 0. Unit in eV.

    Output:
        .. math::
            \varepsilon(E) = 1 + \sum_j \boldsymbol{A}_j / \left(E^2-\boldsymbol{E}_j^2
            + i \cdot \boldsymbol{gamma}_j \cdot E\right)

        With :math:`j`  as the index for the respective oscillator.
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 0, "gamma": 0}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        return 1 + sum(
            c.get("A") / (c.get("E") ** 2 - energy**2 - 1j * c.get("gamma") * energy)
            for c in self.rep_params
        )


class Gaussian(Dispersion):
    r"""Gauss dispersion law.

    Single parameters:
        --

    Repeated parameters:
        :A: Amplitude of the oscillator. Defaults to 1.
        :E: Central energy. Defaults to 1. Unit in eV.
        :sigma: Broadening of the Gaussian. Defaults to 1. Unit in eV.

    Output:

        .. math::
            \varepsilon(E) = \sum_j & \; 2 \cdot \boldsymbol{A}_j / \sqrt{π} \cdot
                    (D\left(2 \cdot \sqrt{2 \cdot \ln(2)} \cdot (E + \boldsymbol{E}_j)
                    / \boldsymbol{sigma}_j\right) \\
                    &- D\left(2 \cdot \sqrt{2 \cdot \ln(2)} \cdot (E - \boldsymbol{E}_j)
                    / \boldsymbol{sigma}_j\right) \\
                    &+ i \cdot \Bigl(\boldsymbol{A}_j \cdot \exp\left(-(4 \cdot \ln(2) \cdot
                    (E - \boldsymbol{E}_j)/ \boldsymbol{sigma}_j\right)^2 \\
                    &- \boldsymbol{A}_j \cdot \exp\left(-(4 \cdot ln(2) \cdot
                    (E + \boldsymbol{E}_j)/ \boldsymbol{sigma}_j\right)^2\Bigr)

        D is the
        `Dawson function
        <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.dawsn.html>`_.
        The summation index :math:`j` is the index of the respective oscillator.

    References:
        * De Sousa Meneses, Malki, Echegut, J. Non-Cryst. Solids 351, 769-776 (2006)
        * Peiponen, Vartiainen, Phys. Rev. B. 44, 8301 (1991)
        * Fujiwara, Collins, Spectroscopic Ellipsometry for Photovoltaics Volume 1,
          Springer International Publishing AG, 2018, p. 137
    """

    single_params_template = {}
    rep_params_template = {"A": 1, "E": 1, "sigma": 1}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
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
        :Eg: Bandgap energy (eV). Defaults to 1.

    Repeated parameters:
        :A: Strength of the absorption. Typically 10 < A < 200. Defaults to 20.
        :E: Lorentz resonance energy (eV). Always keep E > Eg!!. Defaults to 1.5.
        :C: Lorentz broadening (eV). Typically 0 < Ci < 10. Defaults to 1.

    Output:
        The Tauc lorentz dispersion. Please refer to the references for a full formula.

    References:
        * G.E. Jellision and F.A. Modine, Appl. Phys. Lett. 69 (3), 371-374 (1996)
        * Erratum, G.E. Jellison and F.A. Modine, Appl. Phys. Lett 69 (14), 2137 (1996)
        * H. Chen, W.Z. Shen, Eur. Phys. J. B. 43, 503-507 (2005)
    """

    single_params_template = {"Eg": 1}
    rep_params_template = {"A": 20, "E": 1.5, "C": 1}

    @staticmethod
    def eps1(E, Eg, Ai, Ei, Ci):
        gamma2 = sqrt(Ei**2 - Ci**2 / 2) ** 2
        alpha = sqrt(4 * Ei**2 - Ci**2)
        aL = (
            (Eg**2 - Ei**2) * E**2
            + Eg**2 * Ci**2
            - Ei**2 * (Ei**2 + 3 * Eg**2)
        )
        aA = (E**2 - Ei**2) * (Ei**2 + Eg**2) + Eg**2 * Ci**2
        zeta4 = (E**2 - gamma2) ** 2 + alpha**2 * Ci**2 / 4

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
        energy = conversion_wavelength_energy(lbda)
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
                        (energy**2 - c.get("E") ** 2) ** 2
                        + c.get("C") ** 2 * energy**2
                    )
                    / energy
                )
                * np.heaviside(energy - energy_g, 0)
                + self.eps1(energy, energy_g, c.get("A"), c.get("E"), c.get("C"))
            )
            for c in self.rep_params
        )


class Tanguy(Dispersion):
    r"""Fractional dimensional Tanguy model.
    This model is an analytical expression of Wannier excitons, including
    bound and unbound states.

    Single parameters:
          :A: Amplitude (eV). Defaults to 1.
          :d: Dimensionality 1 < d <= 3. Defaults to 3.
          :gamma: Excitonic broadening (eV). Defaults to 0.1.
          :R: Excitonic binding energy (eV). Defaults to 0.1.
          :Eg: Optical band gap energy (eV). Defaults to 1.
          :a: Sellmeier coefficient for background dielectric constant (eV²).
            Defaults to 0.
          :b: Sellmeier coefficient for background dielectric constant (eV²).
            Defaults to 0.

    Repeated parameters.
        --

    Output:
        The Tanguy dispersion. Since the formula is rather long it is not written here.
        Please refer to the references for a full formula.

    References:
        * C. Tanguy, Phys. Rev. Lett. 75, 4090 (1995). Errata, Phys. Rev. Lett. 76, 716 (1996).
        * C. Tanguy, Phys. Rev. B. 60. 10660 (1990).
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
        E = conversion_wavelength_energy(lbda)
        A = self.single_params.get("A")
        d = self.single_params.get("d")
        gam = self.single_params.get("gamma")
        R = self.single_params.get("R")
        Eg = self.single_params.get("Eg")
        a = self.single_params.get("a")
        b = self.single_params.get("b")

        return (
            1
            + a / (b - E**2)
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
    r"""Dispersion law for an UV and IR pole,
    i.e. Lorentz oscillators outside the fitting spectral range and zero broadening.

    Single parameters:
        :A_ir: IR Pole amplitude. Defaults to 1. Unit in eV\ :sup:`2`.
        :A_uv: UV Pole amplitude. Defaults to 1. Unit in eV\ :sup:`2`.
        :E_uv: UV Pole energy. Defaults to 6. Unit in eV.

    Repeated parameters:
        --

    Output:
        .. math::
                \varepsilon(E) = \boldsymbol{A\_ir} / E^2
                + \boldsymbol{A\_uv} / (\boldsymbol{E\_uv}^2 - E^2)
    """

    single_params_template = {"A_ir": 1, "A_uv": 1, "E_uv": 6}
    rep_params_template = {}

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        energy = conversion_wavelength_energy(lbda)
        return self.single_params.get("A_ir") / energy**2 + self.single_params.get(
            "A_uv"
        ) / (self.single_params.get("E_uv") ** 2 - energy**2)


class Table(Dispersion):
    """Dispersion specified by a table of wavelengths (nm) and refractive index values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        :lbda (list): Wavelengths in nm. Defaults to np.linspace(0, 3000, 1000).
        :epsilon: Complex refractive index values in the convention n + ik.
            Defaults to np.ones(1000).

    Repeated parameters:
        --

    Output:
        The interpolation in the given wavelength range.
    """

    single_params_template = {"lbda": np.linspace(0, 3000, 1000), "n": np.ones(1000)}
    rep_params_template = {}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if len(self.single_params.get("lbda")) == 0:
            raise InvalidParameters("Wavelength array cannot be of length zero.")

        if len(self.single_params.get("n")) != len(self.single_params.get("lbda")):
            raise InvalidParameters(
                "Wavelength and refractive index arrays must have the same length."
            )

        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("n") ** 2,
            kind="cubic",
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)


class TableEpsilon(Dispersion):
    r"""Dispersion specified by a table of wavelengths (nm) and dielectric function values.
    Please not that this model will produce errors for wavelengths outside the provided
    wavelength range.

    Single parameters:
        :lbda (list): Wavelengths in nm. Defaults to np.linspace(0, 3000, 1000).
        :epsilon: Complex dielectric function values in the convention ε1 + iε2.
            Defaults to np.ones(1000).

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
        super().__init__(*args, **kwargs)

        if len(self.single_params.get("lbda")) == 0:
            raise InvalidParameters("Wavelength array cannot be of length zero.")

        if len(self.single_params.get("epsilon")) != len(
            self.single_params.get("lbda")
        ):
            raise InvalidParameters(
                "Wavelength and epsilon arrays must have the same length."
            )

        self.interpolation = scipy.interpolate.interp1d(
            self.single_params.get("lbda"),
            self.single_params.get("epsilon"),
            kind="cubic",
        )

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self.interpolation(lbda)
