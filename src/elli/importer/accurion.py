"""A helper class to load data from Accurion EP4 DAT files.
Typical files look like: Si3N4_on_4inBF33_W03_20240905-105631.ds.dat
"""

import pandas as pd
import chardet
import numpy as np

def detect_encoding(fname: str):
	r"""Detects the encoding of file fname. Used in read_accurion_psi_delta only.
  Args:
    fname (str): Filename
  """
	with open(fname, 'rb') as f:
		raw_data = f.read()
	result = chardet.detect(raw_data)
	return result['encoding']

def read_accurion_psi_delta(fname: str, wrap=True) -> pd.DataFrame:
	r"""Read a psi/delta Accurion dat file.
	
  Args:
    fname (str): Filename of the measured dat file
    wrap (bool): Whether delta values should be wrapped; should always be True

  Returns:
    pd.DataFrame: DataFrame containing the psi/delta data in the pyElli-compatible format.
  """
	encoding = detect_encoding(fname)
	psi_delta_df = pd.read_csv(fname, delimiter="\t", encoding=encoding, skiprows=0, header=0)[1:].astype(float)
	psi_delta_df = psi_delta_df.reindex(columns=list(["AOI", "Lambda", "Delta", "Psi"]))
	psi_delta_df = psi_delta_df.rename(columns={
		"AOI": "Angle of Incidence",
		"Lambda": "Wavelength",
		"Delta": "Δ",
		"Psi": "Ψ"
		})
	psi_delta_df = psi_delta_df.groupby(["Angle of Incidence", "Wavelength"]).sum()

	# wrap delta range
	if wrap:
		psi_delta_df.loc[:, "Δ"] = psi_delta_df.loc[:, "Δ"].where(
			psi_delta_df.loc[:, "Δ"] <= 180, psi_delta_df.loc[:, "Δ"] - 360
		)

	return psi_delta_df

def convert_psi_delta_to_isotropic_mueller_matrix(psi_delta_df) -> pd.DataFrame:
	r"""Extract aois and wavelengths values from psi_delta pandas.DataFrame and convert it to a Muellermatrix;
 	only works for isotropic media.

 	Args:
		psi_delta_df (pd.DataFrame): dataFrame returned from data import using 'read_accurion_psi_delta()'

 	Returns:
		pd.DataFrame: pyElli-compatible DataFrame of the Mueller matrix
  """
	aois = psi_delta_df.index.get_level_values("Angle of Incidence").unique().to_numpy()
	wavelengths = psi_delta_df.index.get_level_values("Wavelength").unique().to_numpy()

	# create empty Mueller matrix
	MM = pd.DataFrame(
		{},
		columns=["M11", "M12", "M13", "M14", "M21", "M22", "M23", "M24", "M31", "M32", "M33", "M34", "M41", "M42", "M43", "M44"],
		index=pd.MultiIndex.from_product([aois, wavelengths], names=["Angle of Incidence", "Wavelength"]),
		dtype=float,
		)

	# fill in the Mueller matrix coefficients for an isotropic material based equation in https://www.jawoollam.com/resources/ellipsometry-faq#toggle-id-15
	for aoi in aois:
		for λ in wavelengths:
			Δ = psi_delta_df.loc[aoi, λ]["Δ"]
			Ψ = psi_delta_df.loc[aoi, λ]["Ψ"]

			N = np.cos(2*Ψ)
			C = np.sin(2*Ψ) * np.cos(2*Δ)
			S = np.sin(2*Ψ) * np.cos(2*Δ)

			MM.loc[(aoi, λ), "M11"] = 1
			MM.loc[(aoi, λ), "M12"] = -N
			MM.loc[(aoi, λ), "M13"] = 0
			MM.loc[(aoi, λ), "M14"] = 0

			MM.loc[(aoi, λ), "M21"] = -N
			MM.loc[(aoi, λ), "M22"] = 1
			MM.loc[(aoi, λ), "M23"] = 0
			MM.loc[(aoi, λ), "M24"] = 0

			MM.loc[(aoi, λ), "M31"] = 0
			MM.loc[(aoi, λ), "M32"] = 0
			MM.loc[(aoi, λ), "M33"] = C
			MM.loc[(aoi, λ), "M34"] = S

			MM.loc[(aoi, λ), "M41"] = 0
			MM.loc[(aoi, λ), "M42"] = 0
			MM.loc[(aoi, λ), "M43"] = -S
			MM.loc[(aoi, λ), "M44"] = C

	return MM
