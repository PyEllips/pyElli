# Encoding: utf-8
from .materials import IsotropicMaterial
from .dispersions import DispersionLess, DispersionMgO

AIR = IsotropicMaterial(DispersionLess(1))
MgO = IsotropicMaterial(DispersionMgO(2.956362, -0.01062387, -0.0000204968, 0.02195770, 0.01428322))
