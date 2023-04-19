#!/usr/bin/python
# encoding: utf-8

import elli
import numpy as np
from pytest import raises


def test_solver2x2_active_medium():
    s = elli.Structure(elli.AIR, [], elli.ConstantRefractiveIndex(2 - 1j).get_mat())
    with raises(ValueError):
        s.evaluate(500, 70, solver=elli.Solver2x2)
