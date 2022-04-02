# Changelog

## Version 0.10.0

- Dispersions are now addressed by their name only (instead of Dispersion...)
- Dispersions are initialized with two distinguished set of parameters for parameters which are set once and parameters which may be set multiple times (for oscillators etc). They can bey added by invocing the `add` command on the respective class.
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

- Initial Version after unforking
- Complete rewrite of module structure
- Vectorization of calculations for massive speed-up
- Packaging as PyPi package
- Added additional dispersion models
- Added helper utilities for data-handling
