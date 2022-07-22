# Encoding: utf-8
import sys
from .dispersions.dispersions import *
from .dispersions.base_dispersion import *
from .experiment import Experiment
from .materials import *
from .math import *
from .result import Result, ResultList
from .solver2x2 import Solver2x2
from .solver4x4 import *
from .structure import *
from .utils import *
from .spectraray import *
from .materials_db import *

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
