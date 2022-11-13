"""
Mueller matrix
==============

Mueller matrix fit to a SiO2 on Si measurement.
"""
# %%
import elli
from elli.fitting import ParamsHist, fit_mueller_matrix

# sphinx_gallery_thumbnail_path = '_static/mueller_matrix.png'


# %%
# Read data
# ---------
#
# We load the data from an ascii file containing each of the mueller matrix elements.
# The wavelength range is cut to be in between 210 nm and 820 nm,
# to stay in the range of the provided literature values for Si.
# The data is expected to be in a pandas dataframe containing the columns Mxy,
# where x and y refer to the matrix element inside the mueller matrix.
# The data is scaled by the M11 element, such that :math:`M_{11} = 1` for all wavelengths.
# To show the structure we print the `MM` dataframe.
# If you load your data from another source make sure it adheres to this form.
MM = elli.read_spectraray_mmatrix("Wafer_MM_70.txt").loc[210:820]
print(MM)

# %%
# Setting start parameters
# ------------------------
# Here we set the start parameters for the SiO2 cauchy dispersion
# and thickness of the layer.
params = ParamsHist()
params.add("SiO2_n0", value=1.452, min=-100, max=100, vary=True)
params.add("SiO2_n1", value=36.0, min=-40000, max=40000, vary=True)
params.add("SiO2_n2", value=0, min=-40000, max=40000, vary=True)
params.add("SiO2_k0", value=0, min=-100, max=100, vary=True)
params.add("SiO2_k1", value=0, min=-40000, max=40000, vary=True)
params.add("SiO2_k2", value=0, min=-40000, max=40000, vary=True)
params.add("SiO2_d", value=120, min=0, max=40000, vary=True)

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
@fit_mueller_matrix(MM, params, display_single=False, sharex=True, full_scale=False)
def model(lbda, params):
    SiO2 = elli.Cauchy(
        params["SiO2_n0"],
        params["SiO2_n1"],
        params["SiO2_n2"],
        params["SiO2_k0"],
        params["SiO2_k1"],
        params["SiO2_k2"],
    ).get_mat()

    Layer = [elli.Layer(SiO2, params["SiO2_d"])]

    return elli.Structure(elli.AIR, Layer, Si).evaluate(
        lbda, 70, solver=elli.Solver4x4, propagator=elli.PropagatorExpm()
    )


# %%
# Plot & Fit the model
# --------------------
# Here we plot the model at the initial parameter set vs. the experimental data.
model.plot()

# %%
# We can also plot the residual between measurement and model.
model.plot_residual()

# %%
# Now we execute a fit and plot the model afterwards.
fit_stats = model.fit()
model.plot(full_scale=False)

# %%
# For comparison we plot the residual again to have a figure of merit
# for the fit quality
model.plot_residual()

# %%
# We may also print the fit statistics.
fit_stats

# %%
# References
# ----------
# `Here <https://github.com/PyEllips/pyElli/tree/master/examples/SiO2_Si%20Mueller%20Matrix>`_
# you can find the latest jupyter notebook and data files of this example.
