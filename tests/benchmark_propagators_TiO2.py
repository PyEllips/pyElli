"""Testing benchmark for each solver"""
import numpy as np
import elli


params = elli.ParamsHist()
params.add('SiO2_n0', value=1.452, min=-100, max=100, vary=False)
params.add('SiO2_n1', value=36.0, min=-40000, max=40000, vary=False)
params.add('SiO2_n2', value=0, min=-40000, max=40000, vary=False)
params.add('SiO2_k0', value=0, min=-100, max=100, vary=False)
params.add('SiO2_k1', value=0, min=-40000, max=40000, vary=False)
params.add('SiO2_k2', value=0, min=-40000, max=40000, vary=False)
params.add('SiO2_d', value=276.36, min=0, max=40000, vary=False)

params.add('TiO2_n0', value=2.236, min=-100, max=100, vary=True)
params.add('TiO2_n1', value=451, min=-40000, max=40000, vary=True)
params.add('TiO2_n2', value=251, min=-40000, max=40000, vary=True)
params.add('TiO2_k0', value=0, min=-100, max=100, vary=False)
params.add('TiO2_k1', value=0, min=-40000, max=40000, vary=False)
params.add('TiO2_k2', value=0, min=-40000, max=40000, vary=False)

params.add('TiO2_d', value=20, min=0, max=40000, vary=True)


SiO2 = elli.IsotropicMaterial(elli.DispersionCauchy(params['SiO2_n0'],
                                                params['SiO2_n1'],
                                                params['SiO2_n2'],
                                                params['SiO2_k0'],
                                                params['SiO2_k1'],
                                                params['SiO2_k2']))
TiO2 = elli.IsotropicMaterial(elli.DispersionCauchy(params['TiO2_n0'],
                                                params['TiO2_n1'],
                                                params['TiO2_n2'],
                                                params['TiO2_k0'],
                                                params['TiO2_k1'],
                                                params['TiO2_k2']))

Layer = [elli.Layer(TiO2, params['TiO2_d']),
         elli.Layer(SiO2, params['SiO2_d']),
         elli.Layer(TiO2, params['TiO2_d']),
         elli.Layer(SiO2, params['SiO2_d']),
         elli.Layer(TiO2, params['TiO2_d']),
         elli.Layer(SiO2, params['SiO2_d']),
         elli.Layer(TiO2, params['TiO2_d']),
         elli.Layer(SiO2, params['SiO2_d'])]

s = elli.Structure(elli.AIR, Layer, elli.AIR)
lbda = np.linspace(400, 800, 500)
PHI = 70


def test_solver4x4_eig(benchmark):
    """Benchmarks eignvalue propagator with solver4x4"""
    benchmark.pedantic(s.evaluate,
              args=(lbda, PHI),
              kwargs={'solver': elli.Solver4x4, 'propagator': elli.PropagatorEig()},
              iterations=1,
              rounds=10)

def test_solver4x4_scipy(benchmark):
    """Benchmarks expm-scipy propagator with solver4x4"""
    benchmark.pedantic(s.evaluate,
              args=(lbda, PHI),
              kwargs={'solver': elli.Solver4x4, 'propagator': elli.PropagatorExpmScipy()},
              iterations=1,
              rounds=10)

def test_solver4x4_torch(benchmark):
    """Benchmarks expm-torch propagator with solver4x4"""
    benchmark.pedantic(s.evaluate,
              args=(lbda, PHI),
              kwargs={'solver': elli.Solver4x4, 'propagator': elli.PropagatorExpmTorch()},
              iterations=1,
              rounds=10)

# def test_solver4x4_tf(benchmark):
#     """Benchmarks expm-tf propagator with solver4x4"""
#     benchmark.pedantic(s.evaluate,
#               args=(lbda, PHI),
#               kwargs={'solver': elli.Solver4x4, 'propagator': elli.PropagatorExpmTF()},
#               iterations=1,
#               rounds=10)

def test_solver4x4_linear(benchmark):
    """Benchmarks linear propagator with solver4x4"""
    benchmark.pedantic(s.evaluate,
              args=(lbda, PHI),
              kwargs={'solver': elli.Solver4x4, 'propagator': elli.PropagatorLinear()},
              iterations=1,
              rounds=10)

def test_solver2x2(benchmark):
    """Benchmarks solver2x2"""
    benchmark.pedantic(s.evaluate,
              args=(lbda, PHI),
              kwargs={'solver': elli.Solver2x2},
              iterations=1,
              rounds=10)
