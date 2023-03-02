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

Spectroscopic ellipsometry is an easy applicable and useful tool for todays materials research. 
It is used throughout various scientific fields to determine the optical constants of materials.
However, ellipsometry always needs numerical analysis to deduce material properties from a measurement.
The algorithm of choice for such analysis is the so-called transfer-matrix approach, using matrices for each layer to construct a full matrix for the complete system. 
The matrix describes the whole light matter interaction - reflection, transmission and absorption - of the sample.

Typically, software for such calculations is shipped together with ellipsometers, where each hardware vendor supplies their own version.
Therefore, through different implementation details and different optical models the dispersion models for materials in literature cannot readily be adapted in the lab.

Further, if the supplied software does not support a specific kind of analysis (e.g. anisotropic materials or simultaneous fitting of multiple measurements) scientists need to use third party software, anyways.

In this paper we present the open source python software pyElli, which tackles these problems by offering an open source platform, which is by design easily extendable and adaptable with new optical models or analysis algorithms.

The optical models used, try to stay as close as possible to formulas documented in literature [fujiwara]. 
But it is possible to include vendor-specific models or self-designed models, too.

It leverages the popular public domain database for optical constants [refractiveindex.info] to use citeable reference materials.

PyElli currently supports two solving algorithms, one based on a 2x2 matrix algorithm [byrnes] which is faster, but only applicable for simple problems and a 4x4 matrix algorithm based on the Berreman's transfer matrix formulation [berreman]. 
While the 2x2 algorithm splits the two perpendicular polarized beams and solves them separately, the 4x4 matrix approach solves the complete electromagnetic field. 
Accordingly, it allows to solve more complex problems like anisotropic samples.

# Statement of need

As it is more and more common to publish research data for reuse and review after the FAIR data guidelines [FAIR]. 
The same benefits apply to research software and were summarized in the FAIR4RS principles [FAIR4RS]. 
This is especially important for ellisometric data as the results are tightly related and dependant on the algorithms and models used for evaluation.

Opposite to the vendor provided software, an open source toolkit has many inherent benefits. 
The optical models used can vary between vendors and the translation may be difficult, if the information is not clearly documented. 
PyElli's open source nature makes the models extendable, auditable and occurring changes comprehensible. 
It allows the handling of files from many different measurement devices as importer scripts can be developed as plugins.

To provide fast processing of measurement data, PyElli's algorithms are fully vectorized for multiple wavelengths and leverage the numerical algebra libraries [NumPy] and [SciPy].
This allows the use advanced fitting algorithms like global optimizers in reasonable evaluation times. 
On the other hand this makes realtime, in-situ monitoring of layered material growth possible. 

An [example] in the NORTH analysis toolkit within the research data management software NOMAD by the german FAIRmat consortium shows that the software can easily be integrated in emerging cloud-based analysis tools for science and supports a standardization of ellipsometry data formats within this project [NXellispometry].
We hope that the software contributes to easier analysis and reproducibility, as well as FAIR data management within the ellipsometry community.

Other notable python open source software for solving transfer-matrices are available, but tend to focus on different aspects:

* [PyGTM]: Slower, but more extensive general transfer matrix approach, calculates additional parameters, like the electric field strengths in the multilayer stack.
* [PyLlama]: Provides transfer and scattering matrix algorithms (RCWA), better suited to simulate liquid crystals. Non vectorized.
* [RayFlare]: Complete toolkit to simulate solar cells. Provides the same 2x2 [byrnes] algorithm and a scattering matrix approach.
* Additional mentions: [refellips][EMpy][dtmm][py_matrix]

# Example

* Show a walkthrough of the SiO2 on Si example.
* Show a Mueller matrix example?
* Show an anisotropy example? (Maybe quote my paper about SiPh4 and show the code in a separate git repo)

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:

* `@author:2001` -> "Author et al. (2001)"
* `[@author:2001]` -> "(Author et al., 2001)"
* `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

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