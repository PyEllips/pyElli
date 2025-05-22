---
title: "pyElli: An open source ellipsometry analysis tool for FAIR data"
tags:
  - Python
  - spectroscopy
  - ellipsometry
  - solid state physics
  - transfer matrix method
authors:
  - name: Marius J. Müller
    orcid: 0009-0005-2187-0122
    affiliation: 1
  - name: Sangam Chatterjee
    orcid: 0000-0002-0237-5880
    affiliation: 1
  - name: Florian Dobener
    orcid: 0000-0003-1987-6224
affiliations:
  - name: Institute of Experimental Physics I and Center for Materials Research (ZfM/LaMa), Justus Liebig University Giessen, Heinrich-Buff-Ring 16, Giessen, D-35392 Germany
    index: 1
date: 24 April 2023
bibliography: paper.bib
---

# Summary

**pyElli** is an open-source Python-based analysis tool for evaluating the linear optical interaction of layered materials.
The code primarily targets spectroscopic ellipsometry (SE).
In addition, it is adaptable to various transmission and reflection experiments featuring spectral and polarization resolution.

Various scientific fields use SE to determine the optical functions of materials and multiple-layer stacks often referred to simply as "optical constants" or "material parameters".
The respective experimental "as-measured" SE data requires numerical analysis to deduce physically meaningful quantities.
Typical approaches apply transfer-matrix methods (TMM) [@tompkins2005; @WVASEguide].
Here, an interaction matrix describes the optical response of each individual material layer.
Determining the optical response of a multilayer system then requires matrix multiplication of the individual layers' matrices.

Ellipsometer hardware typically supports bundled proprietary software solutions enabling such analyses.
Unfortunately, each manufacturer supplies their own adapted software solution.
This approach promises efficient laboratory workflows - if working flawlessly.
However, it binds scientists to specific optical models available and limits experiments to the ones supported in the provided software.
Furthermore, data interchange can be cumbersome.
For example, results may even be hard to reproduce on competitive systems due to the use of other models or parameters.
In addition, limitations of the specific software included with each instrument may stimulate scientists to use third-party software:
bundled software packages may not support specific desirable kinds of analyses, such as including the response of optically anisotropic materials or simultaneous fitting of external experimental parameters.

**pyElli** offers an open-source alternative extending the capabilities of existing solutions, while aiming to remain as compatible as possible, by providing data imports from various manufacturers (Woollam VWASE, Woollam CompleteEASE, Sentech, Accurion).
The code is designed with extensibility and adaptability in mind enabling the implementation of individually adapted models as well as data evaluation with custom tools.
Typical examples for advanced use-cases are implementations of custom experimental geometries not covered by other software [@eberheim2022], imaging ellipsometry, or as a full FAIR data automated analysis pipeline for SE measurements.
**pyElli** also supports recent advances in the standardization of ellipsometry data and models, addressing the need for FAIR data [@Wilkinson2016].

**pyElli** aims to provide a straight-forward database of predefined dispersion models for analyzing materials.
All optical models adhere closely to the literature [@Hilfiker2018].
The software easily includes the popular public-domain database for optical constants [refractiveindex.info](https://refractiveindex.info) [@rii].
This allows the inclusion of literature dispersions with a single line of code.
Additional dispersion relations can be either hard coded, which is more efficient, or parsed from a text-based domain-specific language into a dispersion which can be fitted, e.g., polynomially.

**pyElli** supports multiple solving algorithms with different characteristics.
Currently, two algorithms using different formulations are available: a fast algorithm based on a 2x2 matrix formulation [@byrnes2020multilayer] and a more complex 4x4 matrix formulation [@Berreman72; @berreman4x4_doku; @berreman4x4_software].
The 2x2 matrix algorithm divides the light into two perpendicular linearly polarized beams, which are solved separately.
One of its limitations is eliminating the possibility to include birefringent materials.
The 4x4 matrix approach fully solves Maxwell's equations.
These equations describe the complete electromagnetic field inside each layer of the sample and couple these together using the matrix formalism.
This allows finding solutions to more complex problems such as anisotropic materials, active media or magneto-optic samples.

**pyElli** ensures fast processing through fully vectorized algorithms for multiple wavelengths and by leveraging numerical algebra libraries like [NumPy](https://numpy.org) [@harris2020array] and [SciPy](https://scipy.org) [@2020SciPy-NMeth].
Together, these runtime advantages enable the practical use of advanced fitting algorithms such as global optimizers while maintaining reasonable evaluation times.
As a result, **pyElli** enables integrated in-situ monitoring and real-time data analysis of overlayer growth.
Furthermore, the use of Python and vectorization libraries also facilitates the development of artificial intelligence-based SE data analysis.

# Statement of need

The importance of publishing data according to the FAIR principles is growing [@Wilkinson2016].
Many research journals already require authors to add supporting data, and there is a growing expectation from sponsors for institutes and researchers to implement data governance.
The FAIR principles have recently been extended to apply to research software as well since reproducing data requires not only the data itself but also the software used to create it [@Barker2022].
Producing FAIR data and using a FAIR and open analysis pipeline is especially important for SE, as the results are tightly related and dependent on the algorithms and models used for evaluation.

An open-source toolkit, **pyElli** has many inherent benefits over proprietary software.
For SE, optical models vary between manufacturers and translation can be difficult without comprehensive documentation.
**pyElli's** open-source nature makes optical models extendable, auditable, and fully comprehensive.
Each version of **pyElli** is associated with a DOI and a Zenodo upload, allowing for reliable referencing and reproducibility of analysis results.
It supports reading and writing standardized files in the [nexus format](https://nexusformat.org) and is also integrated as an example in the research data management software NOMAD [@Scheidgen2023].

In summary, **pyElli** aims to provide the means of more straight-forward data analysis, reproducibility, and FAIR data management within the ellipsometry community.

# Software with similar functionalities

Other notable Python open-source software for solving transfer-matrices is available, but tends to focus on different aspects:

- [PyGTM](https://pygtm.readthedocs.io) [@Passler17; @Passler19] provides a non-vectorized, extensive general transfer matrix approach. It allows calculation of additional parameters, like the local strength of the electric field at any position in the multilayer stack.
- [PyLlama](https://pyllama.readthedocs.io) [@Bay2022] focuses on the simulation of liquid crystals and uses non-vectorized TMM and a scattering matrix algorithm (rigorous coupled-wave analysis, RCWA).
- [RayFlare](https://rayflare.readthedocs.io) [@Pearce2021] is a complete toolkit to simulate the physical and electrical properties of solar cells. It provides the same 2x2 algorithm[@byrnes2020multilayer] and a scattering matrix approach (S4).
- [tmm_fast](https://github.com/MLResearchAtOSRAM/tmm_fast) [@Luce22] is a vectorized variant of Byrnes' algorithm for artificial intelligence-based analysis of multilayer stacks.
- [tmmax](https://github.com/bahremsd/tmmax) [@tmmax] is a JIT-compilable version of the 2x2 matrix method, leveraging the _JAX_ toolkit.
- [PyMoosh](https://github.com/AnMoreau/PyMoosh) [@Langevin:24] is a comprehensive toolkit for computing the optical properties of multilayered structures, with a plethora of available scattering and transfer matrix algorithms.

# Example: Building a model for an oxide layer on silicon

This example aims to illustrate the straight-forward implementation and building of an optical model in **pyElli**.
The chosen model system is a thin SiO$_2$ layer on bulk Si.
A Cauchy dispersion function describes the SiO$_2$.
Tabulated literature values for Si are loaded from the refractiveindex.info database.

The necessary libraries are loaded before building the model:
**pyElli** is imported from the module `elli`.
The `ParamsHist` wrapper around the `Parameters` class from [lmfit](https://lmfit.github.io/lmfit-py/index.html) [@matt_newville_2024_12785036] is imported from `elli.fitting`.
It adds history functionality to revert any undesired model changes and to return to an earlier set of parameters.
Importing `linspace` from `numpy` enables the generation of a wavelength axis.

```python
from numpy import linspace
import elli
from elli.fitting import ParamsHist, fit
```

Initially, we define the fit parameters.
The Cauchy model for SiO$_2$ is defined by the `SiO2_n0` and `SiO2_n1` parameters along with its layer thickness measured in nanometers.
Optionally, additional settings for _lmfit_ parameters like constraints or bounds might be added; refer to _lmfit's_ documentation for a list of parameter arguments or consult our verbose [basic example](https://pyElli.readthedocs.io/en/stable/auto_examples/plot_01_basic_usage.html#sphx-glr-auto-examples-plot-01-basic-usage-py).

```python
params = ParamsHist()
params.add("SiO2_n0", value=1.452)
params.add("SiO2_n1", value=36.0)
params.add("SiO2_thickness", value=20)
```

Next, the Cauchy model is created using the `Cauchy` class and the defined parameters.
All undefined Cauchy coefficients are kept at their default value of zero in this particular case.
Subsequently, the `.get_mat()` method is called on the created object to automatically convert the dispersion into an isotropic material.
A list of different dispersion classes and their usage is given in the [documentation](https://pyElli.readthedocs.io/en/stable/dispersions.html).

```python
SiO2 = elli.Cauchy(
  params["SiO2_n0"],
  params["SiO2_n1"],
).get_mat()
```

Next, tabulated literature values for silicon is read from a database.
Therefor, the code instantiates the refractiveindex.info database and queries it for the material (`Si`) and author (`Aspnes`).
It is also possible to search the database to get a list of matching entries.
See the [documentation](https://pyElli.readthedocs.io/en/stable/database.html) for details.

```python
rii_db = elli.db.RII()
Si = rii_db.get_mat("Si", "Aspnes")
```

All materials are now instantiated and enable the build of the layered structure.
The `Structure` class takes three arguments:

- The incident half-space, which is typically air.
- The layer stack as a list of `Layer` objects. The `Layer` object is created by adding the material and the layer thickness.
- The lower half-space, which represents the substrate.

The incident and lower half-space are modeled as infinite to terminate the calculation.
Consequently, the calculation inherently cannot capture backside scattering from the bottom substrate surface.

```python
structure = elli.Structure(
    elli.AIR,
    [elli.Layer(SiO2, params["SiO2_thickness"])],
    Si,
)
```

Finally, calling the `evaluate(...)` method of the `structure` object triggers the calculation.
The example uses a `wavelengths` array from $210$ nm to $800$ nm for the calculation range and an angle of incidence of $70°$ degree.

```python
wavelengths = linspace(210, 800, 100)
angle = 70
result = structure.evaluate(wavelengths, angle)
```

The calculation is stored in the `result` variable, which is a [`Result` object](https://pyElli.readthedocs.io/en/stable/result.html).
This object can hold all input parameters and the calculation results.
Methods like `psi`, `delta`, `R`, etc., will deliver the desired output.
Alternatively, the `@fit` decorator in `elli.fitting` automatically calls a widget-based fitting GUI for Jupyter notebooks.
\autoref{fig:fit_dec_example} shows the output when used with this example model and some experimental data.

![The ipywidgets based fitting GUI.\label{fig:fit_dec_example}](fit_decorator_example.png)

The [examples](https://pyElli.readthedocs.io/en/stable/auto_examples/index.html) provide additional information.

# Acknowledgements

Financial support is provided by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation), under grant No. 398143140 (FOR 2824).
SC also acknowledges the LOEWE Transferprofessur "HIMAT".

We thank Olivier Castany and Céline Molinaro for their implementation of the Berreman formalism, Steven J. Byrnes for his 2x2 transfer-matrix-method, and Mikhail Polyanskiy for curating the refractiveindex.info database.

# References

<!-- Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:

- `@author:2001` -> "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)" -->
