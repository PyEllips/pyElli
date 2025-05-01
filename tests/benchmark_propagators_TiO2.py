"""Testing benchmark for each solver"""

import elli
import numpy as np
from elli.fitting import ParamsHist
from pytest import fixture


@fixture
def structure():
    """Build a structure"""
    params = ParamsHist()
    params.add("SiO2_n0", value=1.452, min=-100, max=100, vary=False)
    params.add("SiO2_n1", value=36.0, min=-40000, max=40000, vary=False)
    params.add("SiO2_n2", value=0, min=-40000, max=40000, vary=False)
    params.add("SiO2_k0", value=0, min=-100, max=100, vary=False)
    params.add("SiO2_k1", value=0, min=-40000, max=40000, vary=False)
    params.add("SiO2_k2", value=0, min=-40000, max=40000, vary=False)
    params.add("SiO2_d", value=276.36, min=0, max=40000, vary=False)

    params.add("TiO2_n0", value=2.236, min=-100, max=100, vary=True)
    params.add("TiO2_n1", value=451, min=-40000, max=40000, vary=True)
    params.add("TiO2_n2", value=251, min=-40000, max=40000, vary=True)
    params.add("TiO2_k0", value=0, min=-100, max=100, vary=False)
    params.add("TiO2_k1", value=0, min=-40000, max=40000, vary=False)
    params.add("TiO2_k2", value=0, min=-40000, max=40000, vary=False)

    params.add("TiO2_d", value=20, min=0, max=40000, vary=True)

    SiO2 = elli.Cauchy(
        params["SiO2_n0"],
        params["SiO2_n1"],
        params["SiO2_n2"],
        params["SiO2_k0"],
        params["SiO2_k1"],
        params["SiO2_k2"],
    ).get_mat()
    TiO2 = elli.Cauchy(
        params["TiO2_n0"],
        params["TiO2_n1"],
        params["TiO2_n2"],
        params["TiO2_k0"],
        params["TiO2_k1"],
        params["TiO2_k2"],
    ).get_mat()

    Layer = [
        elli.Layer(TiO2, params["TiO2_d"]),
        elli.Layer(SiO2, params["SiO2_d"]),
        elli.Layer(TiO2, params["TiO2_d"]),
        elli.Layer(SiO2, params["SiO2_d"]),
        elli.Layer(TiO2, params["TiO2_d"]),
        elli.Layer(SiO2, params["SiO2_d"]),
        elli.Layer(TiO2, params["TiO2_d"]),
        elli.Layer(SiO2, params["SiO2_d"]),
    ]

    return elli.Structure(elli.AIR, Layer, elli.AIR)


lbda = np.linspace(400, 800, 500)
PHI = 70


def test_solver4x4_eig(benchmark, structure):
    """Benchmarks eignvalue propagator with solver4x4"""
    benchmark.pedantic(
        structure.evaluate,
        args=(lbda, PHI),
        kwargs={"solver": elli.Solver4x4, "propagator": elli.PropagatorEig()},
        iterations=1,
        rounds=10,
    )


def test_solver4x4_expm(benchmark, structure):
    """Benchmarks expm-scipy propagator with solver4x4"""
    benchmark.pedantic(
        structure.evaluate,
        args=(lbda, PHI),
        kwargs={
            "solver": elli.Solver4x4,
            "propagator": elli.PropagatorExpm(backend="scipy"),
        },
        iterations=1,
        rounds=10,
    )


def test_solver4x4_expm_pytorch(benchmark, structure):
    """Benchmarks expm-torch propagator with solver4x4"""
    benchmark.pedantic(
        structure.evaluate,
        args=(lbda, PHI),
        kwargs={
            "solver": elli.Solver4x4,
            "propagator": elli.PropagatorExpm(backend="torch"),
        },
        iterations=1,
        rounds=10,
    )


def test_solver4x4_linear(benchmark, structure):
    """Benchmarks linear propagator with solver4x4"""
    benchmark.pedantic(
        structure.evaluate,
        args=(lbda, PHI),
        kwargs={"solver": elli.Solver4x4, "propagator": elli.PropagatorLinear()},
        iterations=1,
        rounds=10,
    )


def test_solver2x2(benchmark, structure):
    """Benchmarks solver2x2"""
    benchmark.pedantic(
        structure.evaluate,
        args=(lbda, PHI),
        kwargs={"solver": elli.Solver2x2},
        iterations=1,
        rounds=10,
    )
