"""Decorator functions for convenient fitting of Mueller matrices"""
# Encoding: utf-8
from typing import Callable
from ipywidgets import widgets
from IPython.display import display
import pandas as pd
import numpy.typing as npt
from lmfit import minimize, Parameters
from lmfit.minimizer import MinimizerResult
import plotly.graph_objects as go
from ..result import Result
from ..plot.mueller_matrix import plot_mmatrix
from .params_hist import ParamsHist
from .decorator import FitDecorator


def mmatrix_to_dataframe(exp_df: pd.DataFrame,
                         mueller_matrix: npt.NDArray,
                         identifier:str=None) -> pd.DataFrame:
    """Reshape a numpy 4x4 array containing mueller matrix elements
    to a dataframe with columns Mxy. The index labels for each column
    are taken from the provided exp_df.

    Args:
        exp_df (pd.DataFrame): The experimental dataframe providing the index and columns for
                               the newly generated dataframe.
        mueller_matrix (npt.NDArray): Data to be reshaped into a dataframe
        identifier (str, optional):
            An identifier to append to each column name, in the form
            Mxy_<identifier>, where Mxy is the old column name.
            Defaults to None.

    Returns:
        pd.DataFrame: Contains the data from mueller_matrix in the shape of exp_df
    """
    if identifier is not None:
        columns = [f'{c}_{identifier}' for c in exp_df.columns]
    else:
        columns = exp_df.columns
    mueller_df = pd.DataFrame(
        index=exp_df.index, columns=columns, dtype='float64')
    mueller_df.values[:] = mueller_matrix.reshape(-1, 16)

    return mueller_df


class FitMuellerMatrix(FitDecorator):
    """A class to fit mueller matrices to experimental data"""

    def update_selection(self, _: dict = None) -> None:
        """Update plot after selection of displayed data

        Args:
            _ (dict, optional): No function. Just for compliance with ABC.
        """
        with self.fig.batch_update():
            model_df = mmatrix_to_dataframe(self.exp_mm,
                                            self.model(self.exp_mm.index.values,
                                                       self.params).mueller_matrix)

            for i, melem in enumerate(model_df):
                self.fig.data[2*i+1].y = model_df[melem]

    def create_widgets(self) -> None:
        """Create ipywidgets for parameter estimation"""
        self.param_widgets = {}
        for param in self.params.valuesdict():
            curr_widget = widgets.BoundedFloatText(self.params[param],
                                                   min=self.params[param].min,
                                                   max=self.params[param].max,
                                                   description=param,
                                                   continuous_update=False)
            curr_widget.observe(self.update_params, names=('value', 'owner'))
            self.param_widgets[param] = curr_widget

        fit_button = widgets.Button(description='Fit')
        fit_button.on_click(lambda _: self.fit_button_clicked())
        button_list = [fit_button]

        if isinstance(self.params, ParamsHist):
            undo_button = widgets.Button(description='Undo')
            undo_button.on_click(self.re_undo_button_clicked)
            redo_button = widgets.Button(description='Redo')
            redo_button.on_click(self.re_undo_button_clicked)

            button_list.append(undo_button)
            button_list.append(redo_button)

        display(widgets.VBox([widgets.HBox(list(self.param_widgets.values()) +
                                           button_list,
                                           layout=widgets.Layout(width='100%',
                                                                 display='inline-flex',
                                                                 flex_flow='row wrap')),
                              self.fig]))

    def fit_function(self,
                     params: Parameters,
                     lbda: npt.NDArray,
                     mueller_matrix: pd.DataFrame) -> npt.NDArray:
        """The fit function to minimize the fitting problem

        Args:
            params (Parameters): The lmfit fitting Parameters to construct the simulation
            lbda (npt.NDArray): Wavelengths in nm
            mueller_matrix (pd.DataFrame): The experimental data to compare to the fitted model

        Returns:
            npt.NDArray: Residual between the calculation
                with current parameters and experimental data
        """
        return mueller_matrix.values.reshape(-1, 4, 4) - self.model(lbda, params).mueller_matrix

    def fit(self, method: str = 'leastsq') -> MinimizerResult:
        """Execute lmfit with the current fitting parameters

        Args:
            method (str, optional): The fitting method to use.
                Any method supported by scipys curve_fit is allowed.
                Defaults to 'leastsq'.

        Returns:
            Result: The fitting result
        """
        res = minimize(self.fit_function,
                       self.params,
                       args=(self.exp_mm.index.values, self.exp_mm),
                       method=method)

        self.fitted_params = res.params
        return res

    def get_model_data(self,
                       params:Parameters=None,
                       append_exp_data=False) -> pd.DataFrame:
        """Gets the data from the provided model with the provided parameters.
        If no parameters are provided, the fitted parameters are used
        (which default to the initial parameters if no fit has been triggered).

        Args:
            params (Parameters, optional): 
                The parameters to calculate the model with. 
                If not provided, the fitted parameters are used.
                Defaults to None.
            append_exp_data (bool, optional):
                Appends the experimental data if set to True.
                Defaults to False.

        Returns:
            pd.DataFrame: The model results
        """
        if params is None:
            fit_result = self.model(self.exp_mm.index.values, self.fitted_params)
            desc = 'fit'
        else:
            fit_result = self.model(self.exp_mm.index.values, params)
            desc = 'model'

        if append_exp_data:
            return pd.concat([self.exp_mm,
                              mmatrix_to_dataframe(self.exp_mm,
                                                   fit_result.mueller_matrix,
                                                   identifier=desc)], axis=1)

        return mmatrix_to_dataframe(self.exp_mm,
                                    fit_result.mueller_matrix,
                                    identifier=desc)

    def plot(self, **kwargs) -> go.Figure:
        """Plot the fit results

        Args:
            **display_single (bool):
                Returns a figure containing a single graph, if set to true.
                Returns a grid of figures otherwise.
            **sharex (bool): Ties the zoom of the x-axes together for grid view.
            **full_scale (bool): Sets the y-axis scale to [-1, 1] if set to True.

        Returns:
            go.Figure: The figure containing the data
        """
        fit_result = mmatrix_to_dataframe(self.exp_mm,
                                          self.model(self.exp_mm.index.values,
                                                     self.fitted_params).mueller_matrix)

        return plot_mmatrix([self.exp_mm, fit_result],
                            single=self.display_single
                            if kwargs.get('display_single') is None else kwargs.get('display_single'),
                            sharex=self.sharex
                            if kwargs.get('sharex') is None else kwargs.get('sharex'),
                            full_scale=self.full_scale
                            if kwargs.get('full_scale') is None else kwargs.get('full_scale'))

    def __init__(self,
                 exp_mm: pd.DataFrame,
                 params: Parameters,
                 model: Callable[[npt.NDArray, Parameters], Result],
                 **kwargs) -> None:
        """Intialize the mueller matrix fitting class

        Args:
            exp_mm (pd.DataFrame): The dataframe containing an experimental mueller matrix.
                                   It should contain 16 columns with labels Mxy,
                                   where xy are the matrix positions.
            params (Parameters): Fitting start parameters
            model (Callable[[npt.NDArray, Parameters], Result]):
                A function taking wavelengths as first parameter
                and fitting parameters as second,
                which returns a pyEllis Result object.
                This function contains the actual model which should be fitted

            **display_single (bool):
                Returns a figure containing a single graph, if set to true.
                Returns a grid of figures otherwise.
            **sharex (bool): Ties the zoom of the x-axes together for grid view.
            **full_scale (bool): Sets the y-axis scale to [-1, 1] if set to True.
        """
        super().__init__()
        self.exp_mm = exp_mm
        self.params = params
        self.fitted_params = params.copy()
        self.model = model
        self.display_single = kwargs.get('display_single')
        self.sharex = kwargs.get('sharex')
        self.full_scale = kwargs.get('full_scale')
        self.param_widgets = {}

        model_df = mmatrix_to_dataframe(exp_mm, model(
            exp_mm.index.values, params).mueller_matrix)
        self.fig = plot_mmatrix([exp_mm,
                                 model_df],
                                single=self.display_single,
                                sharex=self.sharex,
                                full_scale=self.full_scale)

        self.create_widgets()


def fit_mueller_matrix(exp_mm: pd.DataFrame,
                       params: Parameters,
                       **kwargs) -> Callable[[npt.NDArray, Parameters], Result]:
    """A parameters decorator for fitting mueller matrices. Displays an ipywidget float box for
    each fitting parameter and an interactive plot to estimate parameters.

    Args:
        exp_mm (pd.DataFrame): The dataframe containing an experimental mueller matrix.
                               It should contain 16 columns with labels Mxy,
                               where xy are the matrix positions.
        params (Parameters): Fitting start parameters
        **display_single (bool):
            Returns a figure containing a single graph, if set to true.
            Returns a grid of figures otherwise.
        **sharex (bool): Ties the zoom of the x-axes together for grid view.
        **full_scale (bool): Sets the y-axis scale to [-1, 1] if set to True.

    Returns:
        Callable[[npt.NDArray, Parameters], Result]:
            A function taking wavelengths as first parameter and fitting parameters as second,
            which returns a pyEllis Result object.
            This function contains the actual model which should be fitted and is automatically
            provided when used as a decorator.
    """
    return lambda model: FitMuellerMatrix(exp_mm, params, model, **kwargs)
