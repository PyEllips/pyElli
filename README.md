<div align="center">
 <img alt="The pyElli logo" src="https://raw.githubusercontent.com/PyEllips/pyElli/master/logo/logo_light.svg">
</div>

--------

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyElli) [![PyPI](https://img.shields.io/pypi/v/pyElli)](https://pypi.org/project/pyElli/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5702469.svg)](https://doi.org/10.5281/zenodo.5702469) [![status](https://joss.theoj.org/papers/515ecaee405aa0be1cb9b887fc5e21bb/status.svg)](https://joss.theoj.org/papers/515ecaee405aa0be1cb9b887fc5e21bb) [![Pytest](https://github.com/PyEllips/pyElli/actions/workflows/pytest.yml/badge.svg)](https://github.com/PyEllips/pyElli/actions/workflows/pytest.yml) [![Documentation Status](https://readthedocs.org/projects/pyelli/badge/?version=latest)](https://pyelli.readthedocs.io/en/latest/?badge=latest) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![](https://dcbadge.vercel.app/api/server/zCBNMtBFAQ?style=flat&compact=true)](https://discord.gg/zCBNMtBFAQ)

# pyElli

PyElli is an open source numerical solver for spectral ellipsometry employing well-known 2x2 and 4x4 algorithms.
It is intended for a broad case of problems including simple fitting of layered structures, anisotropic layers and any other light interaction with layered 1D structures.
It serves as a system for the day to day ellipsometry task at hand and is easily extendable with your own dispersion models, EMAs or solvers.
Our goal is to provide a reproducible and flexible tool for the needs
of scientists working with spectral ellipsometry.

## Features

- A multitude of models to approximate the dielectric function of your material.
- Use the vast library of materials from refractiveindex.info as reference materials.
- Build up your structure easily from materials and layers.
- Simulate reflection and transmission spectra, ellipsometric parameters and Mueller matrices.
- Utilities to quickly convert, plot and fit your measurement data.
- Powerful when necessary, editable and expandable.

## Got a question?

If you have questions using pyElli please feel free to open a discussion in the [Q&A](https://github.com/PyEllips/pyElli/discussions/categories/q-a) or join our [discord channel](https://discord.gg/zCBNMtBFAQ).

## How to get it

The installers for all releases are available at the [Python Package Index (PyPI)](https://pypi.org/project/pyElli/).

To install run:

```sh
pip install pyElli[fitting]
```

This installs pyElli with the additional fitting capabilities and interactive widgets.
If you don't want to have this functionality just drop the `[fitting]` in the end.

To increase performance of the 4x4 Solver, it is recommended to
install PyTorch manually, as it is too big to include in the standard installation.
Installation information can be found at the [PyTorch Website](https://pytorch.org/get-started/locally/).
The CPU variant is sufficient, if you want to save some space.

A complete environment for pyElli is also available as a [Docker Container](https://hub.docker.com/r/domna/pyelli).
To pull and run it directly just execute

```sh
docker run -p 8888:8888 domna/pyelli
```

from your local docker install. After startup a link should
appear in your console. Click it and you will be directed
to a jupyter server with the latest release of pyElli available.

To install the latest development version use:

```sh
pip install "pyElli[fitting] @ git+https://github.com/PyEllips/pyElli.git"
```

The source code is hosted on [GitHub](https://github.com/PyEllips/pyElli), to manually install from source, clone the repository and run `pip install -e .` in
the folder to install it in development mode:

```sh
git clone https://github.com/PyEllips/pyElli
cd pyElli
pip install -e ".[fitting]"
```

## How to cite

Until we have published a Paper on pyElli, we have prepared a Zenodo entry with DOIs for every pyElli Version. The can be found [here](https://zenodo.org/records/13903325).


## Acknowledgements

- Based on Olivier Castany's [Berreman4x4](https://github.com/Berreman4x4/Berreman4x4)
- Solver2x2 based on Steve Byrnes' [tmm](https://github.com/sbyrnes321/tmm)
- Mikhail Polyanskiy's [refractiveindex.info database](https://github.com/polyanskiy/refractiveindex.info-database) and Pavel Dmitriev's [pyTMM](https://github.com/kitchenknif/PyTMM) for his importer script for the database

[@MarJMue](https://github.com/MarJMue) received financial support from 2021 until 2025 by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation), grant No. 398143140 (FOR 2824).
