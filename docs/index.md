# Getting Started with pyElli

PyElli is an open-source numerical solver for spectral ellipsometry employing well-known 2x2 and 4x4 solver algorithms.
It is intended for a broad range of problems such as simple fitting of layered structures,
anisotropic layers and any other polarized light interaction with layered 1D structures.
It serves as a system for the day to day ellipsometry task at hand and aims to make optical model generation standardized and reproducible.

PyElli can be installed directly from [PyPI](https://pypi.org/project/pyElli/).
Installation is as simple as

```sh
pip install pyelli
```

## Fitting dependencies

PyElli has the optional dependency `fitting` to install dependencies to use additional
fitting capabilities and interactive widgets with jupyter notebooks.
If you want to use those you can directly install the dependencies along with pyElli:

```sh
pip install 'pyelli[fitting]'
```