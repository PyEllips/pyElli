# Encoding: utf-8
from .materials import IsotropicMaterial
from .dispersions import DispersionLess

AIR = IsotropicMaterial(DispersionLess(1))
