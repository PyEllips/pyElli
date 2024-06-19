"""Tests for the materials classes"""

import elli
from pytest import raises


class TestMaterials:
    disp = elli.ConstantRefractiveIndex(2)
    disp2 = elli.ConstantRefractiveIndex(5)
    mat = elli.IsotropicMaterial(disp)
    mat2 = elli.IsotropicMaterial(disp2)

    def test_materials_typeguard(self):
        """Checks if materials check input types"""
        with raises(TypeError):
            elli.IsotropicMaterial(self.mat)

        with raises(TypeError):
            elli.IsotropicMaterial(23)

        with raises(TypeError):
            elli.UniaxialMaterial(self.disp, 23)

        with raises(TypeError):
            elli.BiaxialMaterial(self.disp, self.disp, 23)

        with raises(TypeError):
            elli.VCAMaterial(self.mat, self.disp, 0.5)

        with raises(TypeError):
            elli.VCAMaterial(self.disp, self.mat, 0.5)

        with raises(ValueError):
            elli.VCAMaterial(self.mat, self.mat, 10)
