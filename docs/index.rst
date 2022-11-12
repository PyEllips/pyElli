======
pyElli
======

PyElli is an open-source numerical solver for spectral ellipsometry employing well-known
2x2 and 4x4 solver algorithms. It is intended for a broad range of problems
such as simple fitting of layered structures, anisotropic layers and any
other polarized light interaction with layered 1D structures.
It serves as a system for the day to day ellipsometry task at hand
and aims to make optical model generation standardized and reproducible.

PyElli is build to be easily extendable by optical models.
However, pyElli comes with batteries included and already offers a wide range
of :doc:`dispersion models<dispersions>` and the material database of Refractiveindex.info.

Most of the models presented in the
comprehensive book of Fujiwara and Colllins [1]_ are present and additionally
a lot of other models used by ellipsometry vendor softwares are included.

The material database offers the dispersions seen on the `website <https://refractiveindex.info/>`_
and can be accessed by using the :class:`elli.db.RII<elli.db.RII>` module.

To start you may want to dive into :ref:`install<installation>`.
The bast way to start is to have a look at the :doc:`basic usage<auto_examples/plot_01_basic_usage>` or
the :doc:`other examples<auto_examples/index>`.

PyElli consists of a set of classes which work together to create a full
light interaction experiment.
In the image below you see the set of different classes and how they work together
to evaluate a modeled system.

.. mermaid::

   graph LR
        Dx(Dispersion x) --> AM
        Dy(Dispersion y) --> AM
        Dz(Dispersion z) --> AM
        D(Dispersion) --> M
        M(Material) --> L
        AM(AnisotropicMaterial) --> L
        M -- front Material --> S
        AM -- back Material --> S
        L(Layers) --> S & S
        S(Structure) --> E(Experiment)
        S --> |evaluate| R(Result)
        E --> R

It starts by building a set of dispersions and plugging them into materials classes the specific
number of dispersions depends on whether it is an :class:`IsotropicMaterial<elli.materials.IsotropicMaterial>` or an :class:`AnisotropicMaterial<elli.materials.UniaxialMaterial>`.
These materials classes also support creating effective medium layers for inclusions or roughnesses.
The next step is building a :class:`Structure<elli.structure.Structure>` from these materials.
The :class:`Structure<elli.structure.Structure>` needs as least two materials for the incoming and outgoing materials,
but can contain arbitrary more :class:`layers<elli.structure.Layer>` which are only limited by the computational resources.
The :class:`VaryingMixtureLayer<elli.structure.VaryingMixtureLayer>` class can also account for gradient changes of materials in z-direction
of a layer, which is useful for gradient layers or roughness modeling.
As the last step the :class:`Structure<elli.structure.Structure>` is plugged into an :class:`Experiment<elli.experiment.Experiment>`, which contains
the experimental conditions, such as light polarizations.
By evaluating the experiment a :class:`Result<elli.result.Result>` class containing the calculated data is returned.
The creation of an experiment can be skipped by calling the :meth:`evaluate<elli.structure.Structure.evaluate>` method directly
on a :class:`Structure<elli.structure.Structure>` class if you want to use standard experimental settings.

.. rubric:: References

.. [1] H. Fujiwara and R. W. Collins,
   Spectroscopic Ellipsometry for Photovoltaics,
   Volume 1: Fundamental Principles and Solar Cell Characterization,
   Ed. 1, Springer Series in Optical Sciences 212 (2018).
   https://doi.org/10.1007/978-3-319-75377-5



Contents
========

.. toctree::
   :maxdepth: 2

   installation
   auto_examples/index
   modules

Misc
====

.. toctree::
   :maxdepth: 1

   Contributions & Help <contributing>
   License <license>
   Authors <authors>
   Changelog <changelog>
