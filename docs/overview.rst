.. _overview:

===========
Overview
===========

PyElli supplies a sophisticated class system to work with different dispersions, materials
structures and experiment settings.
In the image below you find a diagram how the classes are supposed to work together.

.. mermaid::
    
    graph TD
        Dx(Dispersion x) --> AM
        Dy(Dispersion y) --> AM
        Dz(Dispersion z) --> AM
        D(Dispersion) --> M
        M(Material) --> S
        AM(AnisotropicMaterial) --> S
        S(Structure) --> E(Experiment)
        E --> |evaluate| R(Result)