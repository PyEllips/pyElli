"""A formula dispersion to parse dispersion values from a formula string."""
from typing import Dict, List, Optional

import numpy as np
import numpy.typing as npt

from elli.dispersions.base_dispersion import Dispersion, IndexDispersion
from elli.formula_parser.parser import formula_parser, transformation_formula_parser


class FormulaParser(Dispersion):
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
        wavelength_axis_name: str,
        single_params: Dict[str, float],
        rep_params: Dict[str, List[float]],
    ):
        self.f_single_params: Dict[str, float] = single_params
        self.f_axis_name: str = wavelength_axis_name
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

        self.f_rep_params = {}
        if rep_params_sets:
            self.f_rep_params = rep_params_sets[0]
        super().__init__()

        for rep_params_set in rep_params_sets:
            self.add(**rep_params_set)

        self.rep_params_dl = {}
        if self.rep_params:
            self.rep_params_dl = {
                k: np.array([dic[k] for dic in self.rep_params])
                for k in self.rep_params[0]
            }

        self.formula = formula

        self._check_repr()

    def _check_repr(self):
        representation = formula_parser().parse(self.formula).data

        if isinstance(self, FormulaIndex) and not representation == "n":
            raise ValueError(
                f"Representation `{representation}` not supported by FormulaIndex"
            )

        if isinstance(self, Formula) and not representation == "eps":
            raise ValueError(
                f"Representation `{representation}` not supported by Formula"
            )

    def _dispersion_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return transformation_formula_parser(
            self.f_axis_name, lbda, self.single_params, self.rep_params_dl
        ).parse(self.formula)[1]


class Formula(FormulaParser):
    r"A formula dispersion"

    def dielectric_function(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self._dispersion_function(lbda)


class FormulaIndex(IndexDispersion, FormulaParser):
    r"""A formula dispersion in refractive index formulation"""

    def refractive_index(self, lbda: npt.ArrayLike) -> npt.NDArray:
        return self._dispersion_function(lbda)
