====================
Fitting and plotting
====================

Interactive fitting
-------------------
PyElli offers several classes and decorators to make fitting easy.
The central idea is to construct a class containing the measurement data and an optical model
which is fitted to the data with `lmfit <https://lmfit.github.io/lmfit-py/index.html>`_.
Since pyElli uses lmfit under the hood you may take advantage of it's vast capabilities.

To make creation of the fitting classes as easy as possible pyElli contains decorators to
automatically instantiate the class by providing a function containing the optical model.

Here you see an example of invoking such a decorator with a measurement dataframe **psi_delta** and
parameters **params**, an lmfit `Parameter <https://lmfit.github.io/lmfit-py/parameters.html#lmfit.parameter.Parameter>`_
or :class:`ParamsHist<elli.fitting.params_hist.ParamsHist>` object to create a
:class:`FitRho<elli.fitting.decorator_psi_delta.FitRho>` class.

.. code-block:: python

    @fit(psi_delta, params)
    def model(lbda, params):
        ...

In the :code:`model` function the actual optical model should be constructed and an
:class:`Experiment<elli.experiment.Experiment>` object
should be returned.
A detailed example on how to use this decorator you find in the :doc:`basic usage<auto_examples/plot_01_basic_usage>` example.

Psi/Delta fitting
^^^^^^^^^^^^^^^^^
Fitting decorator and class to fit Psi/Delta experiments.

.. automodule:: elli.fitting.decorator_psi_delta
    :members:
    :show-inheritance:

Mueller matrix fitting
^^^^^^^^^^^^^^^^^^^^^^
Fitting decorator and class to fit mueller matrix experiments.

.. automodule:: elli.fitting.decorator_mmatrix
    :members:
    :show-inheritance:

Fitting base class
^^^^^^^^^^^^^^^^^^
This is the base class providing basic fitting features.
This class is not intended to be used directly, it rather should
be inherited from in additional fitting classes.

.. automodule:: elli.fitting.decorator
    :members:
    :show-inheritance:

Parameter class
---------------
The parameter class extending lmfits Parameter class by a history
of parameter changes.

.. automodule:: elli.fitting.params_hist
    :members:
    :show-inheritance:

Plotting
--------

Mueller matrix
^^^^^^^^^^^^^^
This is a helper class to plot a mueller matrix dataframe.

.. automodule:: elli.plot.mueller_matrix
    :members:
    :show-inheritance:

Structure
^^^^^^^^^
Plots a refractive index slice through a stack of materials.

.. automodule:: elli.plot.structure
    :members:
    :show-inheritance:








