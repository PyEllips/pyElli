"""Tests for the result class"""

import numpy as np
import elli
from pytest import raises


class TestStructures:
    disp = elli.ConstantRefractiveIndex(2)
    mat = elli.IsotropicMaterial(disp)
    layer = elli.Layer(mat, 20)

    def test_layer_typeguard(self):
        """Test layer input checks."""
        with raises(TypeError):
            elli.Layer(self.disp, 20)

        with raises(ValueError):
            elli.Layer(self.mat, -1)

        with raises(TypeError):
            elli.RepeatedLayers(self.layer, 2)

        with raises(TypeError):
            elli.RepeatedLayers([self.mat], 2)

        with raises(ValueError):
            elli.RepeatedLayers([self.layer], -2)

        with raises(ValueError):
            elli.RepeatedLayers([self.layer], 2, -2)

        with raises(ValueError):
            elli.RepeatedLayers([self.layer], 2, 0, -1)

        with raises(TypeError):
            elli.TwistedLayer(self.disp, 20, 5, 20)

        with raises(ValueError):
            elli.TwistedLayer(self.mat, -1, 5, 20)

        with raises(ValueError):
            elli.TwistedLayer(self.mat, 20, 0, 20)

        with raises(TypeError):
            elli.VaryingMixtureLayer(self.disp, 20, 5)

        with raises(TypeError):
            elli.VaryingMixtureLayer(self.mat, 20, 5)

    def test_structure_typeguard(self):
        """Test layer input checks."""
        with raises(TypeError):
            elli.Structure(self.disp, [], self.mat)

        with raises(TypeError):
            elli.Structure(self.mat, [], self.disp)

        with raises(TypeError):
            elli.Structure(elli.AIR, self.layer, self.mat)

        with raises(TypeError):
            elli.Structure(elli.AIR, [self.mat], self.mat)

    def test_varying_mixture_layer(self):
        """Tests the basic functionality of the VML."""
        vca_mat = elli.VCAMaterial(elli.AIR, self.mat, 0.5)
        vml = elli.VaryingMixtureLayer(vca_mat, 10, 3)

        np.testing.assert_array_equal(
            vml.get_permittivity_profile(500)[1][1],
            (elli.AIR.get_tensor(500) + self.mat.get_tensor(500)) / 2,
        )
