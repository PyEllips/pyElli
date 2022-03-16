# Encoding: utf-8
from .materials import IsotropicMaterial
from .dispersions.dispersions import ConstantRefractiveIndex, EpsilonInf

AIR = IsotropicMaterial(ConstantRefractiveIndex(n=1))
