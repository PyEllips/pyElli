---
title: "pyElli: A reproducibly and comprehensible open source ellipsometry analysis tool"
tags:
  - Python
  - spectroscopy
  - ellipsometry
  - solid state physics
  - transfer matrix method
authors:
  - name: Marius Müller
    equal-contrib: true
    affiliation: 1
  - name: Florian Dobener
    orcid: 0000-0003-1987-6224
    equal-contrib: true
    affiliation: 1
affiliations:
  - name: Institute of Experimental Physics I and Center for Materials Research (ZfM/LaMa), Justus Liebig University Giessen, Heinrich-Buff-Ring 16, Giessen, D-35392 Germany
    index: 1
date: 31 July 2022
bibliography: paper.bib
---

# Summary

PyElli is an open source analysis tool for linear optical interaction of layered materials written in python.
It mainly targets spectroscopic ellipsometry, but is easily adaptable to transmission or reflection experiments.

Spectroscopic ellipsometry (SE) is used throughout various scientific fields to determine the optical constants of layered material stacks.
To deduce actual material parameters from an SE experiment, numerical analysis needs to be performed.
This is typically done with the transfer-matrix method (tmm), which associates an interaction matrix to the optical response of each material layer. The full optical response of a material system is then determined by matrix multiplication of the layers matrices.

Proprietary software for such analysis is mostly shipped with ellipsometers, where each ellipsometer manufacturer supplies their own adapted version.
While this is great for a laboratory workflow, it ties scientists to the optical models and experiments available in the software, is hard to reproduce with other systems and makes data interchange cumbersome.
If software does not support a specific kind of analysis, e.g., calculating anisotropic materials or simultaneous fitting of external experimental parameters, scientists need to use third party software.

PyElli offers an open source alternative to existing solutions while staying as compatible as possible.
This allows scientist to adapt pyElli to their needs, either for custom experiments not covered by other software or as a full FAIR data [FAIRpaper] analysis pipeline for SE measurements.
It is designed with extensibility and adaptability in mind, to allow scientists to easily develop their custom analysis pipelines.
It also serves the need of FAIR data by supporting recent advances in standardization of ellipsometry data and models.

The optical models used, try to stay as close as possible to literature [fujiwara].
It is possible to add new dispersions or use a generic formula dispersion, which is able to parse a text-based formula into a fittable dispersion.

To analyse materials it is helpful to have a database of pre-defined models to use.
For this purpose, pyElli includes the popular public domain database for optical constants [refractiveindex.info], which allows users to load literature dispersions with a single line of code.

PyElli supports using mutliple solving algorithms, which allows for specialized applications.
Currently, two algorithms using different formulations are available.
The first one is a simple algorithm based on a 2x2 matrix formulation [byrnes] and second one a more complex 4x4 formulation [berreman].
While the 2x2 algorithm splits the light into two perpendicular polarized beams and solves them separately, the 4x4 matrix approach solves the complete electromagnetic field, which allows solving more complex problems, e.g., anistropic materials or active media.

For fast processing pyElli's algorithms are fully vectorized for multiple wavelengths and leverage the numerical algebra libraries [NumPy] and [SciPy].
This allows the usage of advanced fitting algorithms, i.e., global optimizers, in reasonable evaluation times and enables embedded in-situ monitoring of overlayer growth possible.
The usage of python and vectorization libraries allows for easy adoption for artificial intelligence based analysis of SE data.

# Statement of need

The importance of publishing data according to the FAIR principles [FAIRpaper] is growing.
Many research journals already require authors to add supporting data and sponsors are starting to demand data governance from institutes and researchers.
Since not only the data itself is necessary to reproduce data, but also the software the data was created with, the FAIR principles were recently extended to apply to research software, too [FAIR4RS].
We believe that producing FAIR data and using a FAIR and open analysis pipeline is especially important for SE as the results are tightly related and dependent on the algorithms and models used for evaluation.

An open source toolkit has many inherent benefits over proprietary software.
For SE the optical models vary between manufacturers and the translation may be difficult, if clear documentation is not available.
PyElli's open source nature makes optical models extendable, auditable and occurring changes comprehensible.
Each version of pyElli is associated a doi and a zenodo upload, which allows for reliable referencing and reproducing of analysis results.
It supports NXellipsometry [NXellipsometry], a recent advancement in standardization of SE data.
The standard is developed by the german consortium FAIRmat [link_to_fairmat] within the german National Research Data Infrastracture (NFDI) and is accepted by the NeXus International Advisory Committee (NIAC), which is maintaining beamline-standards in the NeXus format since 20+ years.
PyElli is also available as an example [example] and a cloud-based analysis tool [link_to_north] in the research data management software NOMAD [NOMADpaper].

In summary, we believe and hope that pyElli will further contribute to easier analysis, reproducibility as well as FAIR data management within the ellipsometry community.

# Software with similar functionalities

Other notable python open source software for solving transfer-matrices are available, but tend to focus on different aspects:

- [PyGTM]: Slower, but more extensive general transfer matrix approach, calculates additional parameters, like the electric field strengths in the multilayer stack.
- [PyLlama]: Provides transfer and scattering matrix algorithms (RCWA), better suited to simulate liquid crystals. Non vectorized.
- [RayFlare]: Complete toolkit to simulate solar cells. Provides the same 2x2 [byrnes] algorithm and a scattering matrix approach.
- Additional mentions: [refellips][EMpy][dtmm][py_matrix]
- Fast TMM -> AI stuff

# Application

Here the SiPh example?

# Example: Building a simple model

```python
import numpy as np
import elli
from elli.fitting import ParamsHist, fit
```

```python
params = ParamsHist()
params.add("n0", value=1.452)
params.add("n1", value=36.0)
params.add("thickness", value=20)
```

```python
SiO2 = elli.Cauchy(
  params["n0"],
  params["n1"],
).get_mat()
```

```python
rii_db = elli.db.RII()
Si = rii_db.get_mat("Si", "Aspnes")
```

```python
structure = elli.Structure(
    elli.AIR,
    [elli.Layer(SiO2, params["thickness"])],
    Si,
)
```

```python
wavelengths = np.linspace(210, 800, 100)
structure.evaluate(wavelengths, 70)
```

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:

- `@author:2001` -> "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
