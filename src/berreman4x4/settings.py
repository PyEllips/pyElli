# Encoding: utf-8
"""
Settings used during runtime.
Change in script by accessing the settings dict.

dtype:
    Datatype used by numpy

    np.complex128 (default)
    np.complex64


ExpmBackend:
    Library used to calculate the matrix exponential

    scipy (default) - not vectorized, thus slow
    tensorflow      - faster, but experimental and maybe loss of accuracy
    pytorch         - experimental

"""
import numpy as np

from .solverExpm import SolverExpm
from .solver2x2 import Solver2x2

# Default settings
settings = {
    'dtype': np.complex128,
    'ExpmBackend': 'tensorflow',
    'solver': SolverExpm
}
