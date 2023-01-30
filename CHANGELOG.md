# Changelog

## Version 0.15.1

### New

- Support for Python 3.11
- Pseudo dielectric dispersion

### Bug fixes

- Small fix in reading of rii dispersions
- Don't allow adding of refractive index based dispersions
- Don't allow adding of tabular dispersions

## Version 0.15.0

### New

- Include the Refractiveindex.info database and import and search scripts to access it
- Kramers-Kronig-Relationship conversions for dielectric functions
- Add Cody-Lorentz dispersion model

## Version 0.14.1

### Bug fixes:

- Installs the correct extra requirements in the docker container

## Version 0.14.0

### Breaking changes:

- Moved importers into the importers submodule
- Split the spectraray class into a class to load a dispersion table and an importer

### Bug fixes:

- Introduced proper dependency management
- Changed the dependency of extra install requirements for fitting and testing

## Version 0.13.0

### Breaking Changes:

- Moved math submodule into utils, to avoid name conflict with Python's math module

### Bug fixes:

- Fix error in eigenvalue sorting (PropergatorEig and non-isotropic backmaterials)
- Pin version of ipywidgets to keep plotly working

## Version 0.12.0

### Breaking Changes:

- Renamed the conversion functions and added more
- result.R and .T now return the reflectance/transmittance instead of the respective matrix, which can be accessed with .R_matrix/.T_matrix
- Renamed PropagatorExpmScipy to PropagatorExpm
- Removed Torch and Tensorflow Solvers

### New:

- Added a lot of documentation
- Added a Bruggeman EMA Material
- Support for transmissive Ellipsometry

### Bug fixes:

- Fix nan values in MaxwellGarnettEMA

## Version 0.11.0

- Adds reading functionality for [NeXus files](https://fairmat-experimental.github.io/nexus-fairmat-proposal/50433d9039b3f33299bab338998acb5335cd8951/classes/contributed_definitions/NXellipsometry.html#nxellipsometry).

## Version 0.10.1

- The fitting module is not imported at top-level anymore. It has now to be imported by `elli.fitting`.

## Version 0.10.0

- Dispersions are now addressed by their name only (instead of Dispersion...)
- Dispersions are initialized with two distinguished set of parameters for parameters which are set once and parameters which may be set multiple times (for oscillators etc). They can be added by invoking the `add` command on the respective class.
- There is a new factory class `DispersionFactory` to get a dispersion from it's string name, i.e. `DispersionFactory.get_dispersion(...)`

## Version 0.9.2

- Fitting decorator buttons (fit, undo, redo)
- Data export for decorators
- Changed file loading to -pi, pi delta convention
- Fixed Jones vector default
- Included more documentation

## Version 0.9.1

- Automated build of Docker images
- Benchmarking setup
- Added more documentation
- Renamed a lot of functions for PEP8 compliance
- More bugfixes

## Version 0.9.0

- Adapted examples to the new codebase
- Added a first batch of unit tests
- Reimplemented inhomogeneous and mixed materials
- Changed the sign convention of the E_rp vector
- Improve fitting decorators
- Added plotting and fitting for Mueller matrices
- Added type hints
- Various calculation bugfixes

## Version 0.1.0

- Initial Version after un-forking
- Complete rewrite of module structure
- Vectorization of calculations for massive speed-up
- Packaging as PyPi package
- Added additional dispersion models
- Added helper utilities for data-handling
