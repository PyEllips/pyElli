"""Read and write NeXus files in the ellipsometry
`standard <https://manual.nexusformat.org/classes/contributed_definitions/NXellipsometry.html#nxellipsometry>`_.
NeXus is a format originating from large beam line facitilies and is adapted for
other smaller labratory experiments to supply an agreed standard for data sharing.
For now only reading is supported but in the future there will also be a writer
to store the whole optical model and fit inside the NeXus file."""
import h5py
import numpy as np
import pandas as pd

from elli.dispersions.formula import Formula, FormulaIndex
from elli.dispersions.table_epsilon import TableEpsilon
from elli.dispersions.table_index import Table
from elli.materials import BiaxialMaterial, IsotropicMaterial, UniaxialMaterial

from ..utils import calc_rho, conversion_wavelength_energy


def read_nexus_psi_delta(nxs_filename: str) -> pd.DataFrame:
    """Read a NeXus file containing Psi and Delta data.

    Args:
        nxs_filename (str): The filename of the NeXus file.

    Raises:
        ValueError: Is raised when the data is not stored as psi / delta value.

    Returns:
        pd.DataFrame: Psi/Delta DataFrame.
        The index is a multiindex consisting of the angle of incidents as first column
        and the wavelength as second column.
    """
    h5file = h5py.File(nxs_filename, "r")
    if h5file["entry/sample/data_type"].asstr()[()] != "psi/delta":
        raise ValueError("Data type is not psi / delta")

    aois = np.array(h5file["entry/instrument/angle_of_incidence"])
    wavelength = np.array(h5file["entry/instrument/spectrometer/wavelength"]) / 10
    column_names = np.array(h5file["/entry/sample/column_names"].asstr())
    psi_delta_df = pd.DataFrame(
        {},
        columns=column_names,
        index=pd.MultiIndex.from_product(
            [aois, wavelength], names=["Angle of Incidence", "Wavelength"]
        ),
        dtype=float,
    )

    data = np.array(h5file["/entry/sample/measured_data"])

    for i, aoi in enumerate(aois):
        psi_delta_df.loc[aoi, column_names[1]] = data[0, 0, i, 1, :]
        psi_delta_df.loc[aoi, column_names[0]] = data[0, 0, i, 0, :]

    return psi_delta_df.rename(columns={"psi": "Ψ", "delta": "Δ"})


def read_nexus_rho(nxs_filename: str) -> pd.DataFrame:
    """Reads rho value from NeXus datafile.
    Currently, this works only with psi / delta representation in the NeXus file.

    Raises:
        ValueError: Is raised when the data is not stored as psi / delta value.

    Returns:
        pd.DataFrame: DataFrame containing the measured data as imaginary rho value.
        The index is a multiindex consisting of the angle of incidents as first column
        and the wavelength as second column.
    """
    return calc_rho(read_nexus_psi_delta(nxs_filename))


def read_nexus_materials(filename: str):
    """Read the optical materials from a nexus file.

    Args:
        filename (str): The nexus filename.
    """

    def get_dispersion_function(dataset: h5py.Dataset):
        single_params = {}
        rep_params = {}

        def get_params(_: str, dataset: h5py.Dataset):
            if dataset.attrs.get("NX_class", "") in ["NXdispersion_single_parameter"]:
                param_name = dataset["name"][()].decode("utf-8")
                single_params[param_name] = dataset["value"][()]

            if dataset.attrs.get("NX_class", "") in ["NXdispersion_repeated_parameter"]:
                param_name = dataset["name"][()].decode("utf-8")
                rep_params[param_name] = dataset["values"][()]

        identifier = None
        if "wavelength_identifier" in dataset:
            identifier = dataset["wavelength_identifier"][()].decode("utf-8")
            unit = (
                f"{dataset['wavelength_unit'][()]} "
                f"{dataset['wavelength_unit'].attrs.get('units', '')}"
            )

        if "energy_identifier" in dataset:
            raise NotImplementedError(
                "Using dispersions with an energy axis is not yet supported."
            )

        representation = dataset["representation"][()].decode("utf-8")
        formula = dataset["formula"][()].decode("utf-8")
        dataset.visititems(get_params)

        if representation == "eps":
            return Formula(formula, identifier, single_params, rep_params, unit)

        if representation == "n":
            return FormulaIndex(formula, identifier, single_params, rep_params, unit)

        raise ValueError(f"Unsupported representation {representation}")

    def get_dispersion_table(dataset: h5py.Dataset):
        wavelength = None
        if "wavelength" in dataset:
            wavelength = dataset["wavelength"]

        if "energy" in dataset:
            wavelength = conversion_wavelength_energy(dataset["energy"])

        if wavelength is None:
            raise ValueError("No wavelength array found in dataset.")

        if "refractive_index" in dataset:
            return Table(lbda=wavelength, n=dataset["refractive_index"][()])

        if "dielectric_function" in dataset:
            return TableEpsilon(
                lbda=wavelength, epsilon=dataset["dielectric_function"][()]
            )

        raise ValueError(
            "Invalid dispersion table, neither `refractive_index` "
            "nor `dielectric_function` found."
        )

    def get_dispersion(dataset: h5py.Dataset):
        dispersion = None
        for data in dataset.values():
            if data.attrs.get("NX_class") in ["NXdispersion_function"]:
                dispersion = (
                    get_dispersion_function(data)
                    if dispersion is None
                    else dispersion + get_dispersion_function(data)
                )

            if data.attrs.get("NX_class") in ["NXdispersion_table"]:
                dispersion = (
                    get_dispersion_table(data)
                    if dispersion is None
                    else dispersion + get_dispersion_table(data)
                )

        return dispersion

    def get_material(dataset: h5py.Dataset):
        dispersions = {}
        for dispersion in [f"dispersion_{axis}" for axis in ["x", "y", "z"]]:
            if dispersion not in dataset:
                if dispersion == "dispersion_x":
                    raise ValueError("Invalid dispersion file. `dispersion_x` missing")
                continue
            dispersions[dispersion] = get_dispersion(dataset[dispersion])

        if len(dispersions) == 1:
            return IsotropicMaterial(dispersions["dispersion_x"])
        if len(dispersions) == 2:
            return UniaxialMaterial(
                dispersions["dispersion_x"], dispersions["dispersion_z"]
            )
        if len(dispersions) == 3:
            return BiaxialMaterial(**dispersions)

        raise ValueError("Could not create material from nexus file.")

    entries = {}
    with h5py.File(filename) as h5file:
        for entry, data in h5file.items():
            entries[entry] = get_material(data)

    return entries
