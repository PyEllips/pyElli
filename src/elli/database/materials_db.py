# Encoding: utf-8
from ..dispersions import ConstantRefractiveIndex
from ..materials import IsotropicMaterial

AIR = IsotropicMaterial(ConstantRefractiveIndex(n=1))
