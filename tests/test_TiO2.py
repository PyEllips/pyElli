from __future__ import unicode_literals
import numpy as np
from distutils import dir_util
from pytest import fixture
import os
import elli


class TestTiO2:

    params = elli.ParamsHist()
    params.add('SiO2_n0', value=1.452, min=-100, max=100, vary=False)
    params.add('SiO2_n1', value=36.0, min=-40000, max=40000, vary=False)
    params.add('SiO2_n2', value=0, min=-40000, max=40000, vary=False)
    params.add('SiO2_k0', value=0, min=-100, max=100, vary=False)
    params.add('SiO2_k1', value=0, min=-40000, max=40000, vary=False)
    params.add('SiO2_k2', value=0, min=-40000, max=40000, vary=False)
    params.add('SiO2_d', value=276.36, min=0, max=40000, vary=False)

    params.add('TiO2_n0', value=2.23183200, min=-100, max=100, vary=True)
    params.add('TiO2_n1', value=449.066847, min=-40000, max=40000, vary=True)
    params.add('TiO2_n2', value=199.774450, min=-40000, max=40000, vary=True)
    params.add('TiO2_k0', value=0, min=-100, max=100, vary=False)
    params.add('TiO2_k1', value=0, min=-40000, max=40000, vary=False)
    params.add('TiO2_k2', value=0, min=-40000, max=40000, vary=False)

    params.add('TiO2_d', value=24.8772291, min=0, max=40000, vary=True)

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
             elli.Layer(SiO2, params['SiO2_d'])]

    @fixture
    def datadir(self, tmpdir, request):
        '''
        Fixture responsible for searching a folder with the same name of test
        module and, if available, moving all contents to a temporary directory so
        tests can use them freely.
        '''
        filename = request.module.__file__
        test_dir, _ = os.path.splitext(filename)

        if os.path.isdir(test_dir):
            dir_util.copy_tree(test_dir, str(tmpdir))

        return tmpdir

    def test_solver2x2(self, datadir):
        sr = elli.SpectraRay(datadir)
        Si = elli.IsotropicMaterial(sr.loadDispersionTable('\\Si_Aspnes.mat'))

        meas_data = elli.SpectraRay.read_rho(datadir.join('TiO2_400cycles.txt')).loc[400:800]
        sim_data = elli.Structure(elli.AIR, self.Layer, Si).evaluate(meas_data.index, 70, solver=elli.Solver2x2).rho

        chisqr_real = ((np.real(meas_data) - np.real(sim_data))**2).sum()
        chisqr_imag = ((np.imag(meas_data) - np.imag(sim_data))**2).sum()

        assert(chisqr_real + chisqr_imag < 0.0456)

    def test_solver4x4_torch(self, datadir):
        sr = elli.SpectraRay(datadir)
        Si = elli.IsotropicMaterial(sr.loadDispersionTable('\\Si_Aspnes.mat'))

        meas_data = elli.SpectraRay.read_rho(datadir.join('TiO2_400cycles.txt')).loc[400:800]
        sim_data = elli.Structure(elli.AIR, self.Layer, Si).evaluate(
            meas_data.index, 
            70,
            solver=elli.Solver4x4,
            propagator=elli.PropagatorExpmTorch()
        ).rho

        chisqr_real = ((np.real(meas_data) - np.real(sim_data))**2).sum()
        chisqr_imag = ((np.imag(meas_data) - np.imag(sim_data))**2).sum()

        assert(chisqr_real + chisqr_imag < 0.0456)

    def test_solver4x4_scipy(self, datadir):
        sr = elli.SpectraRay(datadir)
        Si = elli.IsotropicMaterial(sr.loadDispersionTable('\\Si_Aspnes.mat'))

        meas_data = elli.SpectraRay.read_rho(datadir.join('TiO2_400cycles.txt')).loc[400:800]
        sim_data = elli.Structure(elli.AIR, self.Layer, Si).evaluate(
            meas_data.index, 
            70,
            solver=elli.Solver4x4,
            propagator=elli.PropagatorExpmScipy()
        ).rho

        chisqr_real = ((np.real(meas_data) - np.real(sim_data))**2).sum()
        chisqr_imag = ((np.imag(meas_data) - np.imag(sim_data))**2).sum()

        assert(chisqr_real + chisqr_imag < 0.0456)

    def test_solver4x4_eig(self, datadir):
        sr = elli.SpectraRay(datadir)
        Si = elli.IsotropicMaterial(sr.loadDispersionTable('\\Si_Aspnes.mat'))

        meas_data = elli.SpectraRay.read_rho(datadir.join('TiO2_400cycles.txt')).loc[400:800]
        sim_data = elli.Structure(elli.AIR, self.Layer, Si).evaluate(
            meas_data.index, 
            70,
            solver=elli.Solver4x4,
            propagator=elli.PropagatorEig()
        ).rho

        chisqr_real = ((np.real(meas_data) - np.real(sim_data))**2).sum()
        chisqr_imag = ((np.imag(meas_data) - np.imag(sim_data))**2).sum()

        assert(chisqr_real + chisqr_imag < 0.0456)
