"""Benchmark for using the formula dispersion"""

from pytest import fixture
import numpy as np

import elli
from elli.fitting import ParamsHist


wavelength = np.linspace(400, 800, 500)
PHI = 70


@fixture
def structure():
    """Build a structure with a formula dispersion"""
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

    SiO2 = elli.FormulaIndex(
        "n = n0 + 1e2 * n1 / lbda ** 2 + 1e7 * n2 / lbda ** 4 + "
        "1j * (k0 + 1e2 * k1 / lbda ** 2 + 1e7 * k2 / lbda ** 4)",
        "lbda",
        {
            "n0": params["SiO2_n0"].value,
            "n1": params["SiO2_n1"].value,
            "n2": params["SiO2_n2"].value,
            "k0": params["SiO2_k0"].value,
            "k1": params["SiO2_k1"].value,
            "k2": params["SiO2_k2"].value,
        },
        {},
        "nm",
    ).get_mat()
    TiO2 = elli.FormulaIndex(
        "n = n0 + 1e2 * n1 / lbda ** 2 + 1e7 * n2 / lbda ** 4 + "
        "1j * (k0 + 1e2 * k1 / lbda ** 2 + 1e7 * k2 / lbda ** 4)",
        "lbda",
        {
            "n0": params["TiO2_n0"].value,
            "n1": params["TiO2_n1"].value,
            "n2": params["TiO2_n2"].value,
            "k0": params["TiO2_k0"].value,
            "k1": params["TiO2_k1"].value,
            "k2": params["TiO2_k2"].value,
        },
        {},
        "nm",
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


def test_formula_solver2x2(benchmark, structure):
    """Benchmarks solver2x2"""
    benchmark.pedantic(
        structure.evaluate,
        args=(wavelength, PHI),
        kwargs={"solver": elli.Solver2x2},
        iterations=1,
        rounds=10,
    )


def test_formula_solver4x4_expm(benchmark, structure):
    """Benchmarks solver2x2"""
    benchmark.pedantic(
        structure.evaluate,
        args=(wavelength, PHI),
        kwargs={"solver": elli.Solver4x4, "propagator": elli.PropagatorExpm()},
        iterations=1,
        rounds=10,
    )
