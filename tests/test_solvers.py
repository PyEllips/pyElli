#!/usr/bin/python
# encoding: utf-8
import warnings

import elli
import numpy as np
from pytest import raises


def test_solver2x2_active_medium():
    s = elli.Structure(elli.AIR, [], elli.ConstantRefractiveIndex(2 - 1j).get_mat())
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        s.evaluate([200, 300, 400, 500], 70, solver=elli.Solver2x2)
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)


def test_solver2x2_inverse_active_medium():
    s = elli.Structure(elli.AIR, [], elli.ConstantRefractiveIndex(-2 + 1j).get_mat())
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        s.evaluate([200, 300, 400, 500], 70, solver=elli.Solver2x2)
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)
