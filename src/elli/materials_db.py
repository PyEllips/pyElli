# Encoding: utf-8
from .materials import IsotropicMaterial
from .dispersions.dispersions import Constant

AIR = IsotropicMaterial(Constant(n=1))
