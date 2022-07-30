===========
Dispersions
===========

.. automodule:: elli.dispersions.dispersions


Constant Refractive Index
=========================
.. autoclass:: elli.dispersions.dispersions.ConstantRefractiveIndex

Epsilon Infinity
================
.. autoclass:: elli.dispersions.dispersions.EpsilonInf

Cauchy
======
.. autoclass:: elli.dispersions.dispersions.Cauchy

.. plotly::

   fig = elli.Cauchy(n0=1.45, n1=36).get_dielectric_df().plot(backend="plotly")
   fig.update_xaxes(title="Wavelength (nm)")
   fig.update_yaxes(title="Dielectric function")
   fig.data[1].visible = "legendonly"
   fig.update_layout(title="Cauchy dispersion with n0=1.45 and n1=36")


Sellmeier
=========
.. autoclass:: elli.dispersions.dispersions.Sellmeier

.. plotly::

   fig = elli.Sellmeier().add(A=1, B=1e-2).get_dielectric_df().plot(backend="plotly")
   fig.update_xaxes(title="Wavelength (nm)")
   fig.update_yaxes(title="Dielectric function")
   fig.data[1].visible = "legendonly"
   fig.update_layout(title="Sellmeier dispersion with A=1 and B=1e-2")

Drude
=====

Energy parameters
-----------------
.. autoclass:: elli.dispersions.dispersions.DrudeEnergy

Resistivity parameters
----------------------
.. autoclass:: elli.dispersions.dispersions.DrudeResistivity

Lorentz
=======

Wavelength parameters
---------------------
.. autoclass:: elli.dispersions.dispersions.LorentzLambda

.. plotly::

   fig = elli.LorentzLambda().add(1, 500, 100).get_dielectric_df().plot(backend="plotly")
   fig.update_xaxes(title="Wavelength (nm)")
   fig.update_yaxes(title="Dielectric function")
   fig.update_layout(title="Lorentz dispersion with A=1, lambda_r=500 and gamma=100")


Energy parameters
-----------------
.. autoclass:: elli.dispersions.dispersions.LorentzEnergy

Tauc-Lorentz
============
.. autoclass:: elli.dispersions.dispersions.TaucLorentz


Gaussian
========
.. autoclass:: elli.dispersions.dispersions.Gaussian

Tanguy
======
.. autoclass:: elli.dispersions.dispersions.Tanguy

Poles
=====
.. autoclass:: elli.dispersions.dispersions.Poles

Tabulated values
=================

Refractive index values
-----------------------
.. autoclass:: elli.dispersions.dispersions.Table

Epsilon values
--------------
.. autoclass:: elli.dispersions.dispersions.TableEpsilon
   :members:


Abstract classes
================
These classes serve as basic interfaces for dispersions and
convenient + generalised handling.

Dispersion
----------
This is the abstract base class which is the parent class of all dispersions.
It supplies basic functionalities, such as extracting wavelength dependent
epsilon or refractive index values.

.. autoclass:: elli.dispersions.base_dispersion.Dispersion
   :members:

DispersionFactory
-----------------
This factory class returns a fully initialized class identified
by a string.
This is useful if you determine the appropriate dispersion relation
during runtime of your program.

.. autoclass:: elli.dispersions.base_dispersion.DispersionFactory
   :members:

DispersionSum
-------------
This object can be used to add an arbitrary number of dispersions.
The overloaded `+` operator of the dispersion base class creates an instance
of this object with two classes as parameters.
If you want to chain a lot of dispersions it may be more performant to use
this class directly.

.. autoclass:: elli.dispersions.base_dispersion.DispersionSum
   :members:


InvalidParameters
-----------------
This exception is thrown whenever a dispersions got invalid parameters.

.. autoexception:: elli.dispersions.base_dispersion.InvalidParameters
