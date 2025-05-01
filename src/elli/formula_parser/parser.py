"""This modules creates a formula parser"""

from functools import lru_cache
import os
from operator import add, mul, neg, sub, truediv
from typing import Dict

import numpy as np
import scipy.constants as sc
from lark import Lark, Transformer, v_args
from scipy.special import dawsn  # pylint: disable=no-name-in-module


@v_args(inline=True)
class FormulaTransformer(Transformer):
    """Transformer class for parsing formulas"""

    single_params: Dict[str, float]
    repeated_params: Dict[str, np.ndarray]
    no_repeated_params: int

    number = float
    add = add
    sub = sub
    mul = mul
    div = truediv
    neg = neg
    power = pow

    def _check_and_set(self, repeated_params):
        if not repeated_params:
            self.no_repeated_params = 0
            return

        if not isinstance(repeated_params, dict):
            raise ValueError(
                f"Repeated parameters must be a dict but found {type(repeated_params)}"
            )

        params = iter(repeated_params.items())
        length = len(next(params)[1])
        for name, param in params:
            if not isinstance(param, np.ndarray):
                raise TypeError(
                    f"Expected {name} to be of type numpy ndarray but found type {type(param)}"
                )
            if length != len(param):
                raise ValueError("Repeated parameters must have all the same length.")

        self.no_repeated_params = length

    def _check_and_set_single(self, single_params):
        for name, param in single_params.items():
            if not isinstance(param, (float, int)):
                raise TypeError(
                    f"Expected {name} to be of type float but found type {type(param)}."
                )
        self.single_params = single_params

    def __init__(
        self,
        x_axis_name: str,
        x_axis_values: np.ndarray,
        single_params: Dict[str, float],
        repeated_params: Dict[str, np.ndarray],
    ):
        super().__init__()
        if not isinstance(x_axis_name, str):
            raise TypeError("x_axis_name must be a string.")

        if not isinstance(x_axis_values, np.ndarray):
            raise TypeError("x_axis_values must be a numpy array.")

        self.x_axis_name = x_axis_name
        self.x_axis_values = x_axis_values

        self._check_and_set(repeated_params)
        self._check_and_set_single(single_params)

        self.repeated_params = repeated_params
        self.single_params = single_params

    def eps(self, inp):
        """Return an epsilon type formula"""
        return "eps", inp

    # pylint: disable=invalid-name
    def n(self, inp):
        """Return an index type formula"""
        return "n", inp

    def kkr_term(self, term):
        """Calculate the kramers kronig transformation on the function"""
        raise NotImplementedError("kkr transformation not yet implemented")

    def func(self, name, val):
        """Evaluates a function"""
        names = {
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "sqrt": np.emath.sqrt,
            "dawsn": dawsn,
            "ln": np.log,
            "log": np.log10,
            "heaviside": np.heaviside,
        }

        if name in names:
            return names[name](val)

        raise ValueError(f"Unknown function: {name}")

    def builtin(self, name):
        """Returns the values for builtin tokens"""
        names = {
            "1j": 1j,
            "pi": sc.pi,
            "eps_0": sc.epsilon_0,
            "hbar": sc.hbar,
            "h": sc.h,
            "c": sc.c,
        }

        if name in names:
            return names[name]

        raise ValueError(f"Unknown constant: {name}")

    def sum_expr(self, expr):
        """Sum an expression"""
        return expr.sum(axis=1)

    def single_param_name(self, name):
        """Return a parameter inside a non-repeated section"""
        if name == self.x_axis_name:
            return self.x_axis_values

        if name in self.single_params:
            return self.single_params[name]

        raise ValueError(f"No such parameter {name}")

    def param_name(self, name):
        """Return a parameter inside a repeated section"""
        if name == self.x_axis_name:
            return np.einsum(
                "i,j->ij", self.x_axis_values, np.ones(self.no_repeated_params)
            )

        if name in self.single_params:
            return self.single_params[name]

        if name in self.repeated_params:
            return self.repeated_params[name]

        raise ValueError(f"No such parameter {name}")


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(
    f"{__location__}/dispersion_function_grammar.lark", encoding="utf-8"
) as formula_grammar:
    grammar = Lark(
        formula_grammar,
        start="assignment",
        parser="lalr",
    )


@lru_cache(maxsize=128)
def parse_formula(formula: str):
    """
    Parses a dispersion formula string into an abstract syntax tree.
    Uses caching to avoid re-parsing of the formula.

    Args:
        formula (str): The formula string to parse.

    Returns:
        Lark.Tree: The parsed formula Tree.
    """
    return grammar.parse(formula)
