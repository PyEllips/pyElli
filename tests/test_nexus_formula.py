"""Test loading optical models from nexus dispersive material files"""

import numpy as np
from numpy.testing import assert_array_almost_equal
import h5py

from fixtures import datadir  # pylint: disable=unused-import
from elli.dispersions.table_index import Table
from elli.importer.nexus import read_nexus_materials
from elli.dispersions.base_dispersion import IndexDispersionSum
from elli.dispersions.polynomial import Polynomial
from elli.dispersions.sellmeier import Sellmeier
from elli.dispersions.sellmeier_custom import SellmeierCustomExponent
from elli.materials import BiaxialMaterial, IsotropicMaterial, UniaxialMaterial


def test_read_nexus_without_errors(datadir):
    """All dispersive materials are loaded without errors"""
    for file in datadir.iterdir():
        read_nexus_materials(file)


def test_read_nexus_nk_table(datadir):
    """An isotropic nk table is loaded properly"""
    nk_file = datadir / "MoTe2-Beal.nxs"

    with h5py.File(nk_file, "r") as h5file:
        dispersion_path = "/entry/dispersion_x/dispersion_table_nk"
        lbda = h5file[f"{dispersion_path}/wavelength"][()]

        table_manual = Table(
            lbda=lbda,
            n=h5file[f"{dispersion_path}/refractive_index"][()],
        )

    nexus_material = read_nexus_materials(nk_file)["entry"]

    assert isinstance(nexus_material, IsotropicMaterial)

    assert_array_almost_equal(
        table_manual.get_dielectric(lbda),
        nexus_material.dispersion_x.get_dielectric(lbda),
    )


def test_read_nexus_uniaxial_material_with_table(datadir):
    """An uniaxial material with tabulated data is loaded correctly."""
    uniaxial_file = datadir / "MoSe2-Munkhbat-o.nxs"

    with h5py.File(uniaxial_file, "r") as h5file:
        dispersion_x_path = "/entry/dispersion_x/dispersion_table_nk"
        lbda = h5file[f"{dispersion_x_path}/wavelength"][()]

        table_x_manual = Table(
            lbda=lbda,
            n=h5file[f"{dispersion_x_path}/refractive_index"][()],
        )

        dispersion_z_path = "/entry/dispersion_z/dispersion_table_n"
        lbda = h5file[f"{dispersion_z_path}/wavelength"][()]

        table_z_manual = Table(
            lbda=lbda, n=h5file[f"{dispersion_z_path}/refractive_index"][()]
        )

    nexus_material = read_nexus_materials(uniaxial_file)["entry"]

    assert isinstance(nexus_material, UniaxialMaterial)

    assert_array_almost_equal(
        table_x_manual.get_dielectric(lbda),
        nexus_material.dispersion_x.get_dielectric(lbda),
    )

    assert_array_almost_equal(
        table_z_manual.get_dielectric(lbda),
        nexus_material.dispersion_z.get_dielectric(lbda),
    )


def test_read_nexus_for_sellmeier_table_sum(datadir):
    """A sum of sellmeier and a table is read correctly"""
    nexus = datadir / "Si-Chandler-Horowitz.nxs"

    def read_sellmeier(h5file: h5py.File):
        sellmeier_path = "/entry/dispersion_x/sellmeier"
        params_A = h5file[f"{sellmeier_path}/A/values"][()]
        params_B = h5file[f"{sellmeier_path}/B/values"][()]
        params_e1 = h5file[f"{sellmeier_path}/e1/values"][()]
        params_e2 = h5file[f"{sellmeier_path}/e2/values"][()]
        eps_inf = h5file["/entry/dispersion_x/sellmeier/eps_inf/value"][()]

        sellmeier = SellmeierCustomExponent()
        for A, B, e1, e2 in zip(params_A, params_B, params_e1, params_e2):
            sellmeier.add(A, e1, B, e2)

        return (sellmeier + eps_inf).as_index()

    with h5py.File(nexus, "r") as h5file:
        table_path = "/entry/dispersion_x/dispersion_table_k"
        lbda = h5file[f"{table_path}/wavelength"][()]

        table = Table(lbda=lbda, n=h5file[f"{table_path}/refractive_index"][()])

        dispersion = table + read_sellmeier(h5file)

    nexus_material = read_nexus_materials(nexus)["entry"]

    assert isinstance(nexus_material, IsotropicMaterial)
    assert isinstance(nexus_material.dispersion_x, IndexDispersionSum)

    assert_array_almost_equal(
        dispersion.get_dielectric(lbda),
        nexus_material.dispersion_x.get_dielectric(lbda),
    )


def test_read_nexus_sellmeier(datadir):
    """A sellmeier dispersion is read correctly"""
    nexus = datadir / "Si-Salzberg.nxs"
    lbda = np.linspace(1357, 11040, 100)

    with h5py.File(nexus, "r") as h5file:
        sellmeier_path = "/entry/dispersion_x/sellmeier"
        params_A = h5file[f"{sellmeier_path}/A/values"][()]
        params_B = h5file[f"{sellmeier_path}/B/values"][()]

        sellmeier = Sellmeier()
        for A, B in zip(params_A, params_B):
            sellmeier.add(A, B**2)

    nexus_material = read_nexus_materials(nexus)["entry"]

    assert isinstance(nexus_material, IsotropicMaterial)

    assert_array_almost_equal(
        sellmeier.get_dielectric(lbda), nexus_material.dispersion_x.get_dielectric(lbda)
    )


def test_read_nexus_biaxial_material(datadir):
    """A biaxial material is read correctly"""
    nexus = datadir / "WTe2-Munkhbat-alpha.nxs"

    with h5py.File(nexus, "r") as h5file:
        table_x_path = "/entry/dispersion_x/dispersion_table_nk"
        table_y_path = "/entry/dispersion_y/dispersion_table_nk"
        table_z_path = "/entry/dispersion_z/dispersion_table_n"
        lbda = h5file[f"{table_x_path}/wavelength"][()]

        table_x = Table(lbda=lbda, n=h5file[f"{table_x_path}/refractive_index"][()])
        table_y = Table(
            lbda=h5file[f"{table_y_path}/wavelength"][()],
            n=h5file[f"{table_y_path}/refractive_index"][()],
        )
        table_z = Table(
            lbda=h5file[f"{table_z_path}/wavelength"][()],
            n=h5file[f"{table_z_path}/refractive_index"][()],
        )

    nexus_material = read_nexus_materials(nexus)["entry"]

    assert isinstance(nexus_material, BiaxialMaterial)

    assert_array_almost_equal(
        table_x.get_dielectric(lbda), nexus_material.dispersion_x.get_dielectric(lbda)
    )

    assert_array_almost_equal(
        table_y.get_dielectric(lbda), nexus_material.dispersion_y.get_dielectric(lbda)
    )

    assert_array_almost_equal(
        table_z.get_dielectric(lbda), nexus_material.dispersion_z.get_dielectric(lbda)
    )


def test_read_nexus_dispersion_sum(datadir):
    """A dispersion sum is read correctly"""
    nexus = datadir / "YVO4-Shi-e-20C.nxs"
    lbda = np.linspace(480, 1340, 100)

    def read_sellmeier(h5file: h5py.File):
        sellmeier_path = "/entry/dispersion_x/sellmeier"
        params_A = h5file[f"{sellmeier_path}/A/values"][()]
        params_B = h5file[f"{sellmeier_path}/B/values"][()]
        params_e1 = h5file[f"{sellmeier_path}/e1/values"][()]
        params_e2 = h5file[f"{sellmeier_path}/e2/values"][()]
        eps_inf = h5file["/entry/dispersion_x/sellmeier/eps_inf/value"][()]

        sellmeier = SellmeierCustomExponent()
        for A, B, e1, e2 in zip(params_A, params_B, params_e1, params_e2):
            sellmeier.add(A, e1, B, e2)

        return sellmeier + eps_inf

    def read_poly(h5file: h5py.File):
        polynomial_path = "/entry/dispersion_x/polynomial"
        params_e = h5file[f"{polynomial_path}/e/values"][()]
        params_f = h5file[f"{polynomial_path}/f/values"][()]

        poly = Polynomial(0)
        for e, f in zip(params_e, params_f):
            poly.add(f / 1e3**e, e)

        return poly

    with h5py.File(nexus, "r") as h5file:
        disp = read_sellmeier(h5file) + read_poly(h5file)

    nexus_material = read_nexus_materials(nexus)["entry"]

    assert isinstance(nexus_material, IsotropicMaterial)

    assert_array_almost_equal(
        disp.get_dielectric(lbda), nexus_material.dispersion_x.get_dielectric(lbda)
    )
