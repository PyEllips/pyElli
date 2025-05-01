"""Tests for a TiO2/SiO2/Si reference layer"""

from __future__ import unicode_literals

import os
from shutil import copytree, rmtree

import elli
import numpy as np
from elli.fitting import ParamsHist
from pytest import fixture


@fixture
def datadir(tmpdir, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        rmtree(tmpdir)
        copytree(test_dir, str(tmpdir))

    return tmpdir


@fixture
def meas_data(datadir):
    """Fixture for getting the reference measurement data from the file."""
    return (
        elli.read_spectraray_rho(datadir.join("TiO2_400cycles.txt"))
        .loc[70.06]
        .loc[400:800]
    )


@fixture
def si_dispersion(datadir):
    """Fixture to load the silicon dispersion from file."""
    sr = elli.TableSpectraRay(datadir)
    silicon = elli.IsotropicMaterial(sr.load_dispersion_table(f"{os.sep}Si_Aspnes.mat"))

    return silicon


class TestTiO2:
    """Test cases for TiO2/SiO2/Si reference layers"""

    params = ParamsHist()
    params.add("SiO2_n0", value=1.452, min=-100, max=100, vary=False)
    params.add("SiO2_n1", value=36.0, min=-40000, max=40000, vary=False)
    params.add("SiO2_n2", value=0, min=-40000, max=40000, vary=False)
    params.add("SiO2_k0", value=0, min=-100, max=100, vary=False)
    params.add("SiO2_k1", value=0, min=-40000, max=40000, vary=False)
    params.add("SiO2_k2", value=0, min=-40000, max=40000, vary=False)
    params.add("SiO2_d", value=276.36, min=0, max=40000, vary=False)

    params.add("TiO2_n0", value=2.23183200, min=-100, max=100, vary=True)
    params.add("TiO2_n1", value=449.066847, min=-40000, max=40000, vary=True)
    params.add("TiO2_n2", value=199.774450, min=-40000, max=40000, vary=True)
    params.add("TiO2_k0", value=0, min=-100, max=100, vary=False)
    params.add("TiO2_k1", value=0, min=-40000, max=40000, vary=False)
    params.add("TiO2_k2", value=0, min=-40000, max=40000, vary=False)

    params.add("TiO2_d", value=24.8772291, min=0, max=40000, vary=True)

    SiO2 = elli.IsotropicMaterial(
        elli.Cauchy(
            n0=params["SiO2_n0"],
            n1=params["SiO2_n1"],
            n2=params["SiO2_n2"],
            k0=params["SiO2_k0"],
            k1=params["SiO2_k1"],
            k2=params["SiO2_k2"],
        )
    )
    TiO2 = elli.IsotropicMaterial(
        elli.Cauchy(
            n0=params["TiO2_n0"],
            n1=params["TiO2_n1"],
            n2=params["TiO2_n2"],
            k0=params["TiO2_k0"],
            k1=params["TiO2_k1"],
            k2=params["TiO2_k2"],
        )
    )

    Layer = [elli.Layer(TiO2, params["TiO2_d"]), elli.Layer(SiO2, params["SiO2_d"])]

    @staticmethod
    def chisqr(meas_data, sim_data):
        """Calculates the chi square value between two arrays.

        Args:
            meas_data (pd.DataFrame): Measurement data array
            sim_data (pd.DataFrame): Simulation data array

        Returns:
            pd.DataFrame:
                The chi square difference between the measurement and simulation array data.
        """
        chisqr_real = ((np.real(meas_data) - np.real(sim_data)) ** 2).sum()
        chisqr_imag = ((np.imag(meas_data) - np.imag(sim_data)) ** 2).sum()

        return chisqr_real + chisqr_imag

    def test_solver2x2(self, si_dispersion, meas_data):
        """The solver2x2 is within chi square accuracy"""
        sim_data = (
            elli.Structure(elli.AIR, self.Layer, si_dispersion)
            .evaluate(meas_data.index, 70, solver=elli.Solver2x2)
            .rho
        )

        assert TestTiO2.chisqr(meas_data, sim_data) < 0.0456

    def test_solver4x4_expm(self, si_dispersion, meas_data):
        """The solver4x4 with scipy propagator is within chi square accuracy"""
        sim_data = (
            elli.Structure(elli.AIR, self.Layer, si_dispersion)
            .evaluate(
                meas_data.index,
                70,
                solver=elli.Solver4x4,
                propagator=elli.PropagatorExpm(backend="scipy"),
            )
            .rho
        )

        assert TestTiO2.chisqr(meas_data, sim_data) < 0.0456

    def test_solver4x4_expm_torch(self, si_dispersion, meas_data):
        """The solver4x4 with pytorch propagator is within chi square accuracy"""
        sim_data = (
            elli.Structure(elli.AIR, self.Layer, si_dispersion)
            .evaluate(
                meas_data.index,
                70,
                solver=elli.Solver4x4,
                propagator=elli.PropagatorExpm(backend="torch"),
            )
            .rho
        )

        assert TestTiO2.chisqr(meas_data, sim_data) < 0.0456

    def test_solver4x4_eig(self, si_dispersion, meas_data):
        """The solver4x4 with eig propagator is within chi square accuracy"""
        sim_data = (
            elli.Structure(elli.AIR, self.Layer, si_dispersion)
            .evaluate(
                meas_data.index,
                70,
                solver=elli.Solver4x4,
                propagator=elli.PropagatorEig(),
            )
            .rho
        )

        assert TestTiO2.chisqr(meas_data, sim_data) < 0.0456
