# Encoding: utf-8
import sys
from .evaluation import Evaluation
from .dispersions import *
from .half_spaces import *
from .layers import *
from .materials import *
from .math import lambda2E
from .rotations import *
from .settings import *
from .structure import *
from .utils import *

from importlib_metadata import PackageNotFoundError, version

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
