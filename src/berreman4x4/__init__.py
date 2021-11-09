# Encoding: utf-8
import sys
from .dispersions import *
from .experiment import Experiment
from .materials import *
from .math import *
from .result import Result
from .solver2x2 import Solver2x2
from .solver4x4 import *
from .structure import *
from .utils import *
from .spectraray import *
from .materials_db import *
from .fitting.params_hist import ParamsHist
from .fitting.decorator_psi_delta import fit
from .fitting.decorator_mmatrix import fit_mueller_matrix
from .plot.mueller_matrix import plot_mmatrix

if sys.version_info.major >= 3 and sys.version_info.minor > 7:
    from importlib.metadata import PackageNotFoundError, version
else:
    from importlib_metadata import PackageNotFoundError, version

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
