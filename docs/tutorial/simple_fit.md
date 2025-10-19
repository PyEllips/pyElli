# Performing a Simple Fit

```python
import elli
from elli.fitting import ParamsHist, fit
```

## Reading data

```python
ANGLE = 70
psi_delta = elli.read_nexus_psi_delta("SiO2onSi.ellips.nxs").loc[ANGLE].loc[210:800]
```

## Setting parameters

```python
params = ParamsHist()
params.add("SiO2_n0", value=1.452, min=-100, max=100, vary=False)
params.add("SiO2_n1", value=36.0, min=-40000, max=40000, vary=False)
params.add("SiO2_n2", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_k0", value=0, min=-100, max=100, vary=False)
params.add("SiO2_k1", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_k2", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_d", value=20, min=0, max=40000, vary=True)
```

```python
rii_db = elli.db.RII()
Si = rii_db.get_mat("Si", "Aspnes")
```

## Building the Fitting Model

```python
SiO2_dispersion = elli.Cauchy(
    params["SiO2_n0"],
    params["SiO2_n1"],
    params["SiO2_n2"],
    params["SiO2_k0"],
    params["SiO2_k1"],
    params["SiO2_k2"],
)
```

```python
SiO2 = SiO2_dispersion.get_mat()
```

```python
structure = elli.Structure(
    elli.AIR,
    [elli.Layer(SiO2, params["SiO2_d"])],
    Si,
)
```

```python
structure.evaluate(lbda, ANGLE, solver=elli.Solver2x2)
```

## Putting it all together

```python
@fit(psi_delta, params)
def model(lbda, params):
    SiO2 = elli.Cauchy(
        params["SiO2_n0"],
        params["SiO2_n1"],
        params["SiO2_n2"],
        params["SiO2_k0"],
        params["SiO2_k1"],
        params["SiO2_k2"],
    ).get_mat()

    structure = elli.Structure(
        elli.AIR,
        [elli.Layer(SiO2, params["SiO2_d"])],
        Si,
    )

    return structure.evaluate(lbda, ANGLE, solver=elli.Solver2x2)
```

```python
fit_stats = model.fit()
model.plot()
```