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

- Offers two different algorithms 2x2, 4x4
- Power comes from extensibility
- We want to enable collaborative work for an ellipsometry platform
- So far: Different solutions from different companies with their own set of models
  - Can lead to non-reproducibility
- Inclusion of open available data (refractiveindex.info)

<!-- Refactor according to nature summary http://www.cbs.umn.edu/sites/default/files/public/downloads/Annotated_Nature_abstract.pdf -->

Spectroscopic ellipsometry is an easy applicable and useful tool for todays materials research. It is important in alot of different fields since optical constants are often deduced by ellipsometry analysis.
However, the software to analyise data is shipped together with the instruments and hence each vendor implements their own dispersion models and fitting models. The open source ellipsometry software pyElli, written in python tries to solve this issue by supplying an open platform for ellipsometry. A major goal in designing the software was to keep it open to extensions from a broader community.
This applies to the optical models used, which try to stay as close as possible to formulas documented in literature [fujiwara]. It also applies to the solving algorithms. It already comes with a 2x2 algorithm which is often used for simple problems and a 4x4 algorithm based on the berreman transfer matrix formulation [berreman], which is able to solve anisotropic materials as well.

# Example

- Show a walkthrough of the SiO2 on Si example.
- Show a Mueller matrix example?
- Show an anisotropy example?

# Statement of need

- Analysis tools should be as open as the research data
- Often hard to translate optical models between different programs, we aim to make it easier
- Keep interoperability with other formats
- Extend basic functionality of vendor fitting programs

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$
\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.
$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int\_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

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
