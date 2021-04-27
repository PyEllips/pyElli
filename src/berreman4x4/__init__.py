# Encoding: utf-8
import sys
from .dispersions import *
from .experiment import Experiment
from .materials import *
from .math import lambda2E
from .result import Result
from .rotations import *
from .settings import *
from .solver import *
from .structure import *
from .utils import *
from .materials_db import *

from importlib_metadata import PackageNotFoundError, version

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
