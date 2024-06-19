"""Read and write NeXus files in the ellipsometry
`standard <https://manual.nexusformat.org/classes/contributed_definitions/NXellipsometry.html#nxellipsometry>`_.
NeXus is a format originating from large beam line facitilies and is adapted for
other smaller labratory experiments to supply an agreed standard for data sharing.
For now only reading is supported but in the future there will also be a writer
to store the whole optical model and fit inside the NeXus file."""

from dataclasses import dataclass
from typing import Callable, Optional

import h5py
import numpy as np
import pandas as pd

if np.lib.NumpyVersion(np.__version__) < "2.0.0":
    from numpy.lib.index_tricks import IndexExpression
else:
    from numpy.lib._index_tricks_impl import IndexExpression

from elli.dispersions.formula import Formula, FormulaIndex
from elli.dispersions.table_epsilon import TableEpsilon
from elli.dispersions.table_index import Table
from elli.materials import BiaxialMaterial, IsotropicMaterial, UniaxialMaterial

from ..utils import calc_rho, conversion_wavelength_energy


@dataclass
class NexusGroupNames:
    """Contains nexus group names to read from the nexus file"""

    entry: str = "entry"
    sample: str = "sample"
    instrument: str = "instrument"

    @property
    def full_instrument_path(self):
        """Get the full instrument path with prepended entry name, e.g. entry/instrument"""
        return f"{self.entry}/{self.instrument}"

    @property
    def full_sample_path(self):
        """Get the full sample path with prepended entry name, e.g. entry/sample"""
        return f"{self.entry}/{self.sample}"


def read_nexus_psi_delta(
    nxs_filename: str, group_names: Optional[NexusGroupNames] = None
) -> pd.DataFrame:
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

    def read_data(
        wavelength_path: str,
        aois_path: str,
        data_path: str,
        indexing: Callable[[int, int], IndexExpression],
    ):
        aois = np.array(h5file[aois_path])
        wavelength = np.array(h5file[wavelength_path]) / 10
        psi_delta_df = pd.DataFrame(
            {},
            columns=["Ψ", "Δ"],
            index=pd.MultiIndex.from_product(
                [aois, wavelength], names=["Angle of Incidence", "Wavelength"]
            ),
            dtype=float,
        )

        data = np.array(h5file[data_path])

        for i, aoi in enumerate(aois):
            psi_delta_df.loc[aoi, "Ψ"] = data[indexing(i, 0)]
            psi_delta_df.loc[aoi, "Δ"] = data[indexing(i, 1)]

        return psi_delta_df

    def read_legacy() -> pd.DataFrame:
        return read_data(
            wavelength_path=f"{group_names.full_instrument_path}/spectrometer/wavelength",
            aois_path=f"{group_names.full_instrument_path}/angle_of_incidence",
            data_path=f"{group_names.full_sample_path}/measured_data",
            indexing=lambda aoi_idx, observable_idx: np.s_[
                0, 0, aoi_idx, observable_idx, :
            ],
        )

    def read_nx_opt_def() -> pd.DataFrame:
        return read_data(
            wavelength_path=f"{group_names.entry}/data_collection/wavelength_spectrum",
            aois_path=f"{group_names.full_instrument_path}/angle_of_incidence",
            data_path=f"{group_names.entry}/data_collection/measured_data",
            indexing=lambda aoi_idx, observable_idx: np.s_[aoi_idx, observable_idx, :],
        )

    if group_names is not None and not isinstance(group_names, NexusGroupNames):
        raise ValueError(
            f"Invalid type for for group_names: {type(group_names)}. "
            "Should be an instance of NexusGroupNames."
        )

    if group_names is None:
        group_names = NexusGroupNames()

    h5file = h5py.File(nxs_filename, "r")
    if f"{group_names.entry}/sample/data_type" in h5file:
        data_type = h5file[f"{group_names.entry}/sample/data_type"][()].decode("utf-8")
    elif f"{group_names.entry}/data_collection/data_type" in h5file:
        data_type = h5file[f"{group_names.entry}/data_collection/data_type"][()].decode(
            "utf-8"
        )
    else:
        raise ValueError(
            "Could not resolve a proper definition "
            f"from the provided nexus file: {nxs_filename}"
        )

    # Currently, the appdef version can only be determined
    # reliably by the case in the data_type field.
    def_mapping = {
        "psi/delta": read_legacy,
        "Psi/Delta": read_nx_opt_def,
    }

    if data_type not in def_mapping:
        raise NotImplementedError(
            f"Unsupported data type: {data_type}. "
            "Only 'psi/delta' values are supported yet."
        )

    return def_mapping.get(data_type)()


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
