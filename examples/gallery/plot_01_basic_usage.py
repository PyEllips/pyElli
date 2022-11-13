"""
Basic usage
===========

Basic usage of building a model and fitting it to measurement data of SiO2 on Si.

"""
# %%
import elli
from elli.fitting import ParamsHist, fit

# sphinx_gallery_thumbnail_path = '_static/basic_usage.png'


# %%
# Reading data
# ------------------------
#
# We load the data from the generated
# `NeXus file <https://manual.nexusformat.org/classes/contributed_definitions/NXellipsometry.html#nxellipsometry>`_
# and select the angle we want to analyse.
# You may set the ANGLE constant to 50 or 60 to select
# other angles of incidence from the example file.
# Additionally, we're cutting the wavelength axis to be in between 210 nm and 800 nm.
# This is because we're using literature values for Si,
# which are only defined in this wavelength range.
ANGLE = 70
psi_delta = elli.read_nexus_psi_delta("SiO2onSi.ellips.nxs").loc[ANGLE].loc[210:800]

# %%
# Setting parameters
# ------------------------
#
# As an example we analyse an oxidation layer of SiO2 on Si.
# Prior to defining our model, we have to set the parameters we want to use.
# We're going to use a :ref:`Cauchy model <cauchy>` for SiO2 and load the Si values from
# `literature values <https://refractiveindex.info/?shelf=main&book=Si&page=Aspnes>`_.
# The parameter names can be choosen freely,
# but you have to use the exact same name in the later model definition.
# The package uses lmfit as fitting tool and you may refer to their
# `documentation <https://lmfit.github.io/lmfit-py/parameters.html#lmfit.parameter.Parameters.add>`_
# for details on parameter definition.

params = ParamsHist()
params.add("SiO2_n0", value=1.452, min=-100, max=100, vary=False)
params.add("SiO2_n1", value=36.0, min=-40000, max=40000, vary=False)
params.add("SiO2_n2", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_k0", value=0, min=-100, max=100, vary=False)
params.add("SiO2_k1", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_k2", value=0, min=-40000, max=40000, vary=False)
params.add("SiO2_d", value=20, min=0, max=40000, vary=True)

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
# ------------------------
#
# For simple parameter estimation,
# the fit decorator (**@fit**) in conjuction with the model definition is used.
# The fitting decorator takes a pandas dataframe containing
# the psi/delta measurement data (**psi_delta**) and the model parameters (**params**) as an input.
# It then passes the wavelength from measurement dataframe (**lbda**)
# and the parameters to the actual model function.
#
# Inside the model function the optical model is built,
# i.e. the Si literature values are loaded
# and the fitting parameters are filled into the Cauchy dispersion.
# For details on how to insert data into the Cauchy model or other optical dispersion models,
# you may refer to the documentation of pyElli.
# Please keep in mind that the parameters you use here
# have to be defined in the parameter object **param**.
#
# From the dispersion model isotropic materials are generated
# (could also be an anisotropic material, refer to the docs for an overview).
# This is done by calling the :code:`elli.IsotropicMaterial(...)` function
# with a dispersion model as a parameter
# or simply calling :code:`.get_mat()` on a dispersion model.
# These two approaches are equivalent.From these materials the layer is build,
# which only consists of the SiO2 layer in this example.
# The final structure consists of an incoming half-space,
# the layers and an outgoing half space. Specifically,
# typically the light is coming from air and finally gets absorbed by the bulk material,
# in our example this is Si, i.e. we call :code:`elli.Structure(elli.AIR, Layer, Si)`.
#
# To provide simulated data, we have to evaluate the structure
# by calling the :code:`evaluate(...)` function,
# which takes the experimental wavelength array **lbda**, **ANGLE** under which the experiment
# was performed and the solver to be used to solve the transfer-matrix problem.
# Here, we use a simple 2x2 matrix approach,
# which splits the interaction in s and p-parts and therefore cannot account for anisotropy.
# There exist 4x4 matrix solvers as well.
# You may refer to the :ref:`solver documentation <solvers>` for further details.
#
# Executing the cell below in a jupyter notebook displays a comparison of the simulated Ψ / Δ values
# at the current parameter values with their measured counterparts.
# Additionally, input fields for each model parameter are shown.
# You may change the parameters and the calcualted data will change accordingly.
# For clarification the modeled data is shown with `_calc` postfix in the legend.
@fit(psi_delta, params)
def model(lbda, params):
    # Generate the cauchy model from the current lmfit parameters
    SiO2 = elli.Cauchy(
        params["SiO2_n0"],
        params["SiO2_n1"],
        params["SiO2_n2"],
        params["SiO2_k0"],
        params["SiO2_k1"],
        params["SiO2_k2"],
    ).get_mat()
    # get_mat() generates an IsotropicMaterial from the dispersion relation

    # Construct the layers you expect in your sample
    # Here, it only consists of one layer SiO2 in between air and Si.
    # We build the structure coming from air, through the layers,
    # represented as an array, and having Si as bulk material.
    structure = elli.Structure(
        elli.AIR,  # Input medium
        [elli.Layer(SiO2, params["SiO2_d"])],  # Overlayer structure
        Si,
    )  # Output medium / Substrate

    # The model should return the evaluation of the structure at the experimental wavelengths lbda,
    # the experimental angle ANGLE and it should define a solver to calculate the transfer matrix.
    return structure.evaluate(lbda, ANGLE, solver=elli.Solver2x2)


# %%
# Fit and plot fit results
# ------------------------
#
# The fit of the data can be executed by calling the fit() function on the model function,
# which automatically gets attached by the @fit decorator in the cell above.
# The following cell basically executes the fit and plots
# a comparison between the measurement and fitted data.
fit_stats = model.fit()
model.plot()

# %%
# Extracting the optical properties from the fit
# ----------------------------------------------
#
# Since we want to extract the dispersion relation of a layer in our measured stack,
# we can use our fitted parameters.
# The fit parameters are contained in the fits output :code:`params` attribute,
# i.e. :code:`fit_stats.params` for our example.
# We can use it to call our dispersion relation we used in our model
# (here it is a Cauchy dispersion relation)
# and fill in our fitted value.
# By calling :code:`get_dielectric_df()` we can get the dielectric function of the material,
# which is plotted here as an example. :code:`get_dielectric_df` uses a default wavelength range
# which can also be changed by inputting a wavelength array as a parameter.
fitted_model = elli.Cauchy(
    fit_stats.params["SiO2_n0"],
    fit_stats.params["SiO2_n1"],
    fit_stats.params["SiO2_n2"],
    fit_stats.params["SiO2_k0"],
    fit_stats.params["SiO2_k1"],
    fit_stats.params["SiO2_k2"],
)

fitted_model.get_dielectric_df().plot(backend="plotly")

# %%
# We can also call :code:`get_refractive_index_df()`
# to get the refractive index of the material as dataframe.
fitted_model.get_refractive_index_df().plot(backend="plotly")

# %%
# If you want to write your data to a file you simply call pandas :code:`to_csv(...)`
# function to write a csv file, i.e. for the dielectric function this writes as
fitted_model.get_dielectric_df().to_csv("SiO2_diel_func.csv")

# %%
# You may also access a single value of your optical model
fit_stats.params["SiO2_n0"].value

# %%
# Our simply print the fitted values in a list together with their fitting errors
fit_stats.params

# %%
# Show fit statistics
# --------------------
# Now, we may also print out the fit statictics from the model fit in the cell above.
# The fit statistics are simple `lmfit fit statistics <https://lmfit.github.io/lmfit-py/fitting.html#>`_, too.
# Typically, one uses chi square values as a figure of merit for the fit quality.
# It is stored in the chisqr attribute of the fit_stats variable we defined above.
fit_stats.chisqr

# %%
# We can print the full fit statistics, too.
fit_stats

# %%
# References
# ----------
# `Here <https://github.com/PyEllips/pyElli/tree/master/examples/Basic%20Usage>`_
# you can find the latest jupyter notebook and data files of this example.
