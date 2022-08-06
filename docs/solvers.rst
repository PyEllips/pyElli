*******
Solvers
*******

For calculation of light interaction in material stacks the transfer matrix method is used.
In pyElli the :class:`Solver<elli.solver.Solver>` classes provide the necessary toolset for two kinds of transfer matrix algorithms.
They are not intended to be used directly, but rather to be provided in the evaluation in the :class:`Structure<elli.structure.Structure>` class.
The :class:`Solver2x2<elli.solver2x2.Solver2x2>` is a simple and fast algorithm for isotropic materials.
It splits the calculation into two 2x2 matrices, one for the s and one for the p polarized light.

The :class:`Solver4x4<elli.solver4x4.Solver4x4>` is a more complex algorithm for anisotropic materials.
It employs a full 4x4 matrix formulation for all light interaction.
It is based on the Berreman matrix formalism [1]_.
In the Berreman formalism a propagator for matrix exponentials is needed.
pyElli provides different implementations to be used in the calculation of the transfer matrices.
The :class:`PropagatorEig<elli.solver4x4.PropagatorEig>` is based on solving the eigenvalues of the first order approximation of the matrix exponential.
Although, it is very fast it is not very accurate.
The :class:`PropagatorExpm<elli.solver4x4.PropagatorExpm>` is solving the matrix exponential by the Pade approximation.

.. rubric:: References

.. [1] Dwight W. Berreman, "Optics in Stratified and Anisotropic Media: 4×4-Matrix Formulation," J. Opt. Soc. Am. 62, 502-510 (1972)



Solver base class (Solver)
==========================

.. automodule:: elli.solver
   :members:
   :undoc-members:
   :show-inheritance:

2x2 Matrix Solver (Solver2x2)
=============================

.. automodule:: elli.solver2x2
   :members:
   :undoc-members:
   :show-inheritance:

4x4 Matrix Solver (Solver4x4)
=============================

.. automodule:: elli.solver4x4
   :members:
   :undoc-members:
   :show-inheritance:
