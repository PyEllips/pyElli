# Performing a Simple Fit

In this tutorial we will perform a simple fit with pyElli.
We determine the thickness of a silicon dioxide layer on top of silicon.
This fit is often carried out as calibration and benchmark fit for ellipsometers and
is widely used for quality control of silicon wafers.
Here, we will use it to make our first steps with pyElli.

Please make sure you meet the following prerequesits:

- You are in a python environment with pyElli [installed](../index.md).
- We recommend to run the code in a jupyter or jupyter compatible environment.
However, you _can_ run this code in a repl or python file directly as well.
It will just not display the fitting widgets.
- An understanding of ellipsometry, in particular Psi/Delta measurement data.

## Importing the packages

First, we need to import pyElli itself.
Additionally, we import the `ParamsHist` class, which is a small wrapper around lmfit's `Parameter` class.
It stores a parameter history to retrieve previous fit configurations.
We'll also import the function `fit` from pyEllis fitting module.
This is a function decorator, which we will use to display our interactive fitting widget.

```python
import numpy as np
import elli
from elli.fitting import ParamsHist, fit
```

## Reading data

We need some measurement data to perform a fit on and load an example [data set](https://github.com/PyEllips/pyElli/blob/master/examples/Basic%20Usage/SiO2onSi.ellips.nxs) of a psi delta measurement in the standardized [NeXus format](https://manual.nexusformat.org/classes/contributed_definitions/NXellipsometry.html#nxellipsometry) with pyElli's included `read_nexus_psi_delta` function.
Lets select a measurement angle of 70 degrees (`.loc[ANGLE]`) from the data and
restrict the wavelength range in between 210 nm and 800 nm (`.loc[210:800]`).
The restriction is necessary because we're using tabulated literature values for silicon, which are only provided in this wavelength range.

```python
ANGLE = 70
psi_delta = (
    elli.read_nexus_psi_delta("SiO2onSi.ellips.nxs")
    .loc[ANGLE]
    .loc[210:800]
)
```

## Setting parameters

To fit our data we need some actual fitting parameters.
We'll use our `ParamsHist` class which is a wrapper around lmfit's Parameters class.
The names of the paramters are freely choosable but we recommend to use some material and parameter name combination.
We'll use standard literature values for the silicon dioxide dispersion parameters $n_0$ (`SiO2_n0`) and $n_1$ (`SiO2_n1`).
For now, we won't vary these parameters in the fit, hence we set `vary=False` in the parameter definition.
Last but not least, we'll add a thickness parameter of the silicon dioxide layer with an initial guess of the materials thickness.
We set the `min` and `max` values to reasonable values and `vary=True` since we want to fit the thickness of the layer.

```python
params = ParamsHist()
params.add("SiO2_n0", value=1.452, vary=False)
params.add("SiO2_n1", value=36.0, vary=False)
params.add("SiO2_d", value=20, min=1, max=1000, vary=True)
```

## Building the Fit Model

We're ready to build a model!
First we need to construct our materials.
We have a silicon substrate which we load from the included [refractiveindex.info](https://refractiveindex.info) material database.
We are going to use the tabulated values from [Aspnes et al.](https://refractiveindex.info/?shelf=main&book=Si&page=Aspnes).

```python
rii_db = elli.db.RII()
Si = rii_db.get_mat("Si", "Aspnes")
```

For the silicon dioxide layer we need a formula to insert our fitting values.
Here, we could also use tabulated values since we won't vary the parameters of the Cauchy model but in general it's a good practice to fit the material parameters, too.

```python
SiO2_dispersion = elli.Cauchy(
    params["SiO2_n0"], params["SiO2_n1"], 0, 0, 0, 0,
)
```

The above snippet created a dispersion and now we need to generate a material from it. For anisotropic materials this can be done by calling `get_mat()`.

```python
SiO2 = SiO2_dispersion.get_mat()
```

Now, we we put our materials together in a `Structure`.
It consists of a front-layer, which is air (`elli.AIR`) in this case (but will be air in most experiments you do) and a back layer which is silicon here.
In between is the most important part: the array of layers.
Here, we only have a single layer of silicon dioxide.
In the `Layer` specify the material and the thickness (`SiO2_d`).

```python
structure = elli.Structure(
    elli.AIR,
    [elli.Layer(SiO2, params["SiO2_d"])],
    Si,
)
```

In the last step we just need to evaluate our model for a set of wavelengths (`lbda`) at a given angle (`ANGLE`).
Additionally, we need the specify the solver (`elli.Solver2x2` in this case).

```python
lbda = np.linspace(210, 800, 100)
structure.evaluate(lbda, ANGLE, solver=elli.Solver2x2)
```

## Putting it all together

In this section we simply put the parts together: building the materials, the structure and evaluating it with the appropriate parameters.
We use the `@fit` decorator here, which takes the measurement data `psi_delta` and our fit parameter class `params`.
The `@fit` decorator generates a fit class to perform fitting on.
If this code snippet is executed in a jupyter environment it will display a fit widget in which you can alter the parameter and see the direct feedback as well as performing the fit.

```python
@fit(psi_delta, params)
def model(lbda, params):
    SiO2 = elli.Cauchy(
        params["SiO2_n0"], params["SiO2_n1"], 0, 0, 0, 0,
    ).get_mat()

    structure = elli.Structure(
        elli.AIR,
        [elli.Layer(SiO2, params["SiO2_d"])],
        Si,
    )

    return structure.evaluate(lbda, ANGLE, solver=elli.Solver2x2)
```

By calling `fit()` we perform the fit and with `plot()` we can generate a plot of the resulting fit.
This part is optional if you used the fitting widget of the `@fit` decorator, since the widget will call these for you.
```python
fit_stats = model.fit()
model.plot()
```

Finally, we extract the actual thickness of the silicon dioxide layer by extracting the parameter from `fit_stats`.
```
fit_stats.params["SiO2_d].value
```

It should return a value $\approx 2.066\,\text{nm}$.

## Congrats 🎉

You have sucessfully performed a simple fit with pyElli.
Feel free to explore with this code, e.g., you may want to try varying the material parameters during the fit or using different angles from the measurement (50 or 60 degrees is also available).
