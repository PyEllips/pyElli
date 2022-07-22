# Encoding: utf-8
from .materials import IsotropicMaterial
from .dispersions.dispersions import ConstantRefractiveIndex

AIR = IsotropicMaterial(ConstantRefractiveIndex(n=1))
