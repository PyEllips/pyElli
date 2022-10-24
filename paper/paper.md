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

Spectroscopic ellipsometry is an easy applicable and useful tool for todays materials research. It is used throughout various scientific fields to determine the optical constants of materials.
However, ellipsometry always needs numerical analysis to deduce material properties from a measurement.
The algorithm of choice for such analysis is the so-called transfer-matrix approach, using matrices for each layer to construct a full matrix for the complete system.
Typically, software for such calculations is shipped together with ellipsometers, where each hardware vendor supplies their own version.
Therefore, through different implementation details and different optical models the dispersion models for materials in literature cannot readily be adapted in the lab.
Further, if the supplied software does not support a specific kind of analysis (e.g. anisotropy) scientists need to use third party software, anyways.
In this paper we present the open source python software pyElli, which tackles these problems by offering an open source platform, which is by design easily extendable and adaptable with new optical models or analysis algorithms. It supports querying the popular database for optical constants [refractiveindex.info], too.
The optical models used, try to stay as close as possible to formulas documented in literature [fujiwara]. It is possible to include vendor-specific models or self-designed models, too. PyElli currently supports two solving algorithms, one based on a 2x2 matrix algorithm [byrnes] which is often used for simple problems and a 4x4 matrix algorithm based on the berreman transfer matrix formulation [berreman]. While the 2x2 algorithm splits the two perpendicular polarized beams and solves them separately, the 4x4 matrix approach solves the complete electromagnetic field. Accordingly, it allows to solve more complex problems like anisotropy (... more examples??).
An [example] in the NORTH analysis toolkit within the research data management software NOMAD by the german FAIRmat consortium shows that the software can easily be integrated in emerging cloud-based analysis tools for science and supports a standardization of ellipsometry data formats within this project [NXellispometry].
We hope that the software contributes to easier analysis and reproducibility, as well as FAIR data management within the ellipsometry community.

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
