"""Tests for the different mixture models"""

import pytest
import elli
import numpy as np


material_list = [
    ("Si", "Aspnes"),
    ("GaAs", "Aspnes"),
    ("SiO2", "Malitson"),
    ("CaF2", "Li"),
    ("Rh", "Weaver"),
    ("MoS2", "Song-1L"),
]


@pytest.fixture
def RII():
    RII = elli.db.RII()
    return RII


@pytest.mark.parametrize(
    "host_book, host_page",
    material_list,
)
@pytest.mark.parametrize(
    "guest_book, guest_page",
    material_list,
)
@pytest.mark.parametrize(
    "EMA",
    [
        elli.LooyengaEMA,
        elli.MaxwellGarnettEMA,
    ],
)
def test_mixture_models(host_book, host_page, guest_book, guest_page, EMA, RII):
    host_mat = RII.get_mat(host_book, host_page)
    guest_mat = RII.get_mat(guest_book, guest_page)

    lbda = np.arange(250, 800, 25)

    np.testing.assert_allclose(
        elli.BruggemanEMA(host_mat, guest_mat, 0.1).get_tensor(lbda),
        EMA(host_mat, guest_mat, 0.1).get_tensor(lbda),
        rtol=0.5,
        atol=0.5 + 0.5j,
    )
