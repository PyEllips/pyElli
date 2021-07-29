---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import berreman4x4 as bm
from lmfit import minimize, Parameters, fit_report

bm.settings['ExpmBackend'] = 'tensorflow'
bm.settings['solver'] = 'berreman4x4'
```

# Load data
Load data collected with Sentech Ellipsometer and cut the spectral range (to use Si Aspnes file)

The sample is an ALD grown TiO2 sample (with 400 cycles) on commercially available SiO2 / Si substrate.

```python
tss = bm.SpectraRay.read_psi_delta_file('TiO2_400cycles.txt').loc[400:800]
ρ = bm.SpectraRay.read_rho('TiO2_400cycles.txt').loc[400:800]
```

# Estimate Parameters and build model

```python
params = bm.ParamsHist()
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
```

```python
@bm.manual_parameters(tss, params)
def model(lbda, params):
    sr = bm.SpectraRay('./')
    Si = bm.IsotropicMaterial(sr.loadDispersionTable('Si_Aspnes.mat'))

    SiO2 = bm.IsotropicMaterial(bm.DispersionCauchy(params['SiO2_n0'], 
                                                    params['SiO2_n1'], 
                                                    params['SiO2_n2'], 
                                                    params['SiO2_k0'], 
                                                    params['SiO2_k1'], 
                                                    params['SiO2_k2']))
    TiO2 = bm.IsotropicMaterial(bm.DispersionCauchy(params['TiO2_n0'], 
                                                    params['TiO2_n1'], 
                                                    params['TiO2_n2'], 
                                                    params['TiO2_k0'], 
                                                    params['TiO2_k1'], 
                                                    params['TiO2_k2']))
    
    Layer = [bm.Layer(TiO2, params['TiO2_d']), 
             bm.Layer(SiO2, params['SiO2_d'])]

    return bm.Structure(bm.AIR, Layer, Si).evaluate(lbda, 70)
```

# Fit to experimental data

```python
out = model['fit'](ρ, method='leastsq')
out
```

# Show fits

```python
model['plot'](out.params)
```

```python
model['plot_rho'](ρ, out.params)
```

```python

```
