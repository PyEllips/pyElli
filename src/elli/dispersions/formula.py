"""A formula dispersion to parse dispersion values from a formula string."""
from typing import Dict, List, Optional
import numpy.typing as npt

from .base_dispersion import Dispersion, IndexDispersion


class FormulaDispersion(Dispersion):
    r"""A formula dispersion"""

    @property
    def single_params_template(self) -> dict:
        return self.f_single_params

    @property
    def rep_params_template(self) -> dict:
        return self.f_rep_params

    def __init__(
        self,
        formula: str,
        single_params: Dict[str, float],
        rep_params: Dict[str, List[float]],
    ):
        self.f_single_params: Dict[str, float] = single_params
        rep_params_len: Optional[int] = None
        rep_params_sets: List[Dict[str, float]] = []

        for key, values in rep_params.items():
            if not isinstance(values, list):
                raise ValueError("Repeated parameters must be given as dict of lists")
            for i, value in enumerate(values):
                if i >= len(rep_params_sets):
                    rep_params_sets.append({})
                rep_params_sets[i][key] = value

            if rep_params_len is None:
                rep_params_len = len(values)
                continue
            if len(values) != rep_params_len:
                raise ValueError(
                    f"All repeated parameters must have the same length."
                    f"Found {values} with length {len(values)}, "
                    f"but previous length was {rep_params_len}."
                )

        self.f_rep_params = rep_params_sets[0]
        super().__init__()

        for rep_params_set in rep_params_sets:
            self.add(**rep_params_set)

        self.formula = formula

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        pass


class FormulaIndexDispersion(IndexDispersion):
    r"""A formula dispersion in refractive index formulation"""
