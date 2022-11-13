"""
Multilayer fit
==============

Fits a multilayer model to an ALD grown TiO2 sample on SiO2 / Si.
"""

# %%
import elli
from elli.fitting import ParamsHist, fit

# sphinx_gallery_thumbnail_path = '_static/multilayer.png'

# %%
# Load data
# ---------
#
# Load data collected with Sentech Ellipsometer and cut the spectral range (to use Si Aspnes file)
#
# The sample is an ALD grown TiO2 sample (with 400 cycles)
# on commercially available SiO2 / Si substrate.
tss = elli.read_spectraray_psi_delta("TiO2_400cycles.txt").loc[400:800]

# %%
# Set start parameters
# --------------------
# Here we set the start parameters for the TiO2 and SiO2 layer.
# We set the SiO2 layer parameters to a fixed value from another
# fit of the substrate. See the :ref:`Basic usage` example for details
# on how to perform such a fit.
# In general it is a good idea to fit your data layer-wise if possible
# to yield a better fit quality.
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

# %%
# Load silicon dispersion from the refractiveindexinfo database
# -------------------------------------------------------------
# You can load any material from the index
# `refractiveindex.info <https://refractiveindex.info>`__, which is
# embedded into the software (so you may use it offline, too). Here, we
# are interested in the literature values for the silicon substrate.
# First we need to load the database with ``rii_db = elli.db.RII()`` and
# then we can query it with ``rii_db.get_mat("Si", "Aspnes")`` to load
# this
# `entry <https://refractiveindex.info/?shelf=main&book=Si&page=Aspnes>`__.
rii_db = elli.db.RII()
Si = rii_db.get_mat("Si", "Aspnes")

# %%
# Building the model
# ------------------
# Here the model is build and the experimental structure is returned.
# For details on this process please refer to the :ref:`Basic usage` example.
# When executed in an jupyter notebook this displays an interactive graph
# with which you can select the start parameters before fitting the data.
@fit(tss, params)
def model(lbda, params):
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

    Layer = [elli.Layer(TiO2, params["TiO2_d"]), elli.Layer(SiO2, params["SiO2_d"])]

    return elli.Structure(elli.AIR, Layer, Si).evaluate(lbda, 70, solver=elli.Solver2x2)
    # Alternative: Use 4x4 Solver with scipy propagator
    # return elli.Structure(elli.AIR, Layer, Si).evaluate(lbda, 70, solver=elli.Solver4x4, propagator=elli.PropagatorExpm())


# %%
# Plot & Fit model
# ----------------
# We plot the model to see the deviation with the initial parameters.
model.plot()


# %%
# Now lets perform the fit and plot the comparison of
# calculation and experimental data afterwards.
fit_stats = model.fit()
model.plot()

# %%
# We can also have a look at the fit statistics.
fit_stats

# %%
# References
# ----------
# `Here <https://github.com/PyEllips/pyElli/tree/master/examples/TiO2%20Fit>`_
# you can find the latest jupyter notebook and data files of this example.
