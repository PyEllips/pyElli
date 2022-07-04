======
pyElli
======

PyElli is an open-source numerical solver for spectral ellipsometry employing well-known 
2x2 and 4x4 solver algorithms. It is intended for a broad range of problems
such as simple fitting of layered structures, anisotropic layers and any
other polarized light interaction with layered 1D structures.
It serves as a system for the day to day ellipsometry task at hand
and aims to make optical model generation standardized and reproducible.

PyElli can be easily extended with further optical models and the ones
available are clearly documented and editable to your needs.
However, pyElli comes with batteries included and already offers a wide range
of :doc:`dispersion models<dispersions>`. All the models presented in the
comprehensive book of Fujiwara and Colllins [1]_ are present and additionally
a lot of other models used by ellipsometry vendor softwares are included.

To start of you may want to dive into :ref:`Install<installation>` and have a look 
at the :ref:`Basic usage<usage>` or the :ref:`Examples<examples>` section.

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
   usage
   examples
   modules

Misc
====

.. toctree::
   :maxdepth: 1

   Contributions & Help <contributing>
   License <license>
   Authors <authors>
   Changelog <changelog>
