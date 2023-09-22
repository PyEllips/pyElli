"""Tests for the result class"""
import numpy as np
from pytest import raises
import elli


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

    def test_mixture_materials(self):
        """Basic mixture material tests"""
        with raises(TypeError):
            elli.VCAMaterial(self.mat, self.disp, 0.5)

        with raises(TypeError):
            elli.VCAMaterial(self.disp, self.mat, 0.5)

        with raises(ValueError):
            elli.VCAMaterial(self.mat, self.mat, 10)

        vca = elli.VCAMaterial(self.mat2, self.mat, 0.1)
        looyenga = elli.LooyengaEMA(self.mat2, self.mat, 0.1)
        mg = elli.MaxwellGarnettEMA(self.mat2, self.mat, 0.1)
        brug = elli.BruggemanEMA(self.mat2, self.mat, 0.1)

        for mixture in [looyenga, mg, brug]:
            np.testing.assert_array_almost_equal(
                mixture.get_tensor(500), vca.get_tensor(500), decimal=-1
            )
