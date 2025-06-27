# Changelog

## Version 0.22.4

### Bugfixes

- Fix for an error when copying of an IndexDispersion created from a Dispersion
- Fix for reading of woollam data if no dpolE is present

## Version 0.22.3

### Bugfixes

- Pin Plotly to a version smaller than 6, to avoid problems with the fitting widget (#203).

## Version 0.22.2

### Bugfixes

- Fix publishing workflow

## Version 0.22.1

### New

- convert_delta_range function

### Bugfixes

- Allow all valid Delta ranges in the Result class

## Version 0.22.0

### New

- Python 3.13 support
- Updated dependencies
- Updated refractive index database

### Bugfixes

- SciPy performance regression fixed with Version 1.15

## Version 0.21.2

### Bugfixes

- Include the RII database submodule in the Pypi package again

## Version 0.21.1

### Bugfixes

- Fix documentation generation

## Version 0.21.0

### New

- Reenable pytorch 4x4solver
- Use OIDC for publishing
- Add custom fitting example
- Add chardet encoding detection
- Add reader for accurion data

### Bugfixes

- Fix deprecation warnings

## Version 0.20.0

### New

- Vectorized KKR
- NumPy 2.0.0 support

### Bug fixes

- Fix root selection mistakes for Bruggeman EMA

### Known issues

- Performance regression for newer SciPy versions of expm solver (#178)

## Version 0.19.0

### New

- Python 3.12 Support
- Averaging of ResultLists
- Breaking change: Renamed RII.load_dispersion to RII.get_dispersion to be more consistent.

## Version 0.18.1

### Bug fixes

- Bump pygments from 2.13.0 to 2.15.0
- Bump tornado from 6.3.2 to 6.3.3
- Fixes wvase importer

## Version 0.18.0

### What's Changed

- Update spectraray importer
- Update RII database and use new file structure
- Bump scipy from 1.9.1 to 1.10.0
- Adds woollam importer

## Version 0.17.0

### New

- Support for NXopt based nexus definitions
- Interpolation order for refractiveindex.info database
- Speed up for formula dispersions

### Bug fixes

- Better error messages
- Raise error when solver2x2 gets a negative k

## Version 0.16.0

### New

- Support for nexus dispersion files
- Formula based dispersions
- Cauchy Urbach dispersion
- Filtering by range for the refractive index database

### Bug fixes

- Fixed a bug where incompatible dispersions were created in refractive index database
- Created separated index and dielectric dispersions
- Fixed checks for DispersionSums when dispersions are entered via \*args

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
- More Bug fixes

## Version 0.9.0

- Adapted examples to the new codebase
- Added a first batch of unit tests
- Reimplemented inhomogeneous and mixed materials
- Changed the sign convention of the E_rp vector
- Improve fitting decorators
- Added plotting and fitting for Mueller matrices
- Added type hints
- Various calculation Bug fixes

## Version 0.1.0

- Initial Version after un-forking
- Complete rewrite of module structure
- Vectorization of calculations for massive speed-up
- Packaging as PyPi package
- Added additional dispersion models
- Added helper utilities for data-handling
