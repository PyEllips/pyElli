"""Abstract base class for Decorator functions for convenient fitting"""
# Encoding: utf-8
from abc import ABC, abstractmethod

import pandas as pd

try:
    from lmfit import Parameters
    from ipywidgets import widgets
except ImportError as e:
    raise ImportError(
        "This module requires lmfit and ipywidgets to work properly.\n"
        "Try installing this package with the additional fitting requirement, "
        "i.e. pip install pyElli[fitting]"
    ) from e

from .params_hist import ParamsHist


def is_in_notebook() -> bool:
    """Checks whether the current shell is in a jupyter notebook.

    Returns:
        bool: True if the shell is in jupyter, False otherwise.
    """
    try:
        # pylint: disable=import-outside-toplevel
        from IPython import get_ipython

        if "IPKernelApp" not in get_ipython().config:
            return False
    except ImportError:
        return False
    except AttributeError:
        return False
    return True


class FitDecorator(ABC):
    """The abstract base class for fitting decorators.
    Providing features for fit, undo and redo buttons."""

    def __init__(self) -> None:
        self.params = ParamsHist()
        self.fitted_params = ParamsHist()
        self.last_params = ParamsHist()
        self.initial_params = ParamsHist()
        self.param_widgets = {}

    @abstractmethod
    def get_model_data(
        self, params: Parameters = None, append_exp_data=False
    ) -> pd.DataFrame:
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

    def to_csv(
        self,
        *args,
        fname: str,
        params: Parameters = None,
        append_exp_data: bool = False,
        **kwargs
    ) -> None:
        """Saves the current model to csv. This is just a wrapper to
        pandas Dataframe and any argument to pandas to_csv may be passed
        as function arguments.

        Args:
            fname (str): The file name to save the data to.
            params (Parameters, optional):
                The parameters to calculate the model with.
                If not provided, the fitted parameters are used.
                Defaults to None.
            append_exp_data (bool, optional):
                Appends the experimental data if set to True.
                Defaults to False.
        """
        self.get_model_data(params, append_exp_data).to_csv(fname, *args, **kwargs)

    @abstractmethod
    def fit(self, method: str = "") -> None:
        """Execute lmfit with the current fitting parameters

        Args:
            method (str, optional): The fitting method to use.
                                    Any method supported by scipys curve_fit is allowed.
                                    Defaults to 'leastsq'.

        Returns:
            Result: The fitting result
        """

    @abstractmethod
    def update_selection(self, change: dict = None) -> None:
        """Update plot after selection of displayed data

        Args:
            change (dict, optional): A dictionary containing the ipywidgets change event
        """

    def set_vary_param(self, change: dict) -> None:
        self.initial_params[change.owner.description_tooltip].vary = change.new
        self.params[change.owner.description_tooltip].vary = change.new

    def fit_button_clicked(self) -> None:
        """Fit and update plot after the fit button has been clicked

        Args:
            selected (dict): Dict containing the current widget information
                of the selection dropdown.
        """
        self.fit()
        if isinstance(self.params, ParamsHist):
            self.params.commit()
        self.params.update_params(self.fitted_params)
        self.update_widgets()

        self.update_selection()

    def re_undo_button_clicked(self, button: widgets.Button) -> None:
        """Redo or undo an operation on the parameters history object

        Args:
            button (widgets.Button):
                The button instance, which triggered the event.
        """
        if not isinstance(self.params, ParamsHist):
            return

        if button.description == "Undo":
            self.last_params = self.params.pop()
            self.update_widgets()
        elif self.last_params is not None:
            self.params.update_params(self.last_params)
            self.update_widgets()
            self.last_params = None

        self.update_selection()

    def reset_to_init_params(self) -> None:
        """Resets the parameters to the initial values"""

        if not isinstance(self.params, ParamsHist):
            return

        self.last_params = self.params.pop()
        self.params = self.initial_params.copy()
        self.update_widgets()
        self.update_selection()

    def update_params(self, change: dict) -> None:
        """Update plot after a change of fitting parameters

        Args:
            change (dict): A dictionary containing the ipywidgets change event
            selected (dict): The selected value of the data display dropdown widget
        """
        if isinstance(self.params, ParamsHist):
            self.params.commit()
        self.params[change.owner.description].value = change.new

        self.update_selection()

    def update_widgets(self) -> None:
        """Updates the widget values according to the current parameters."""
        for param in self.params:
            widget = self.param_widgets.get(param)
            if widget is not None:
                # Unobserve and re-observe, otherwise the update_params
                # would be called on every change
                # and a history event would be triggered for each of these changes.
                widget.unobserve(self.update_params, names="value")
                widget.value = self.params[param].value
                widget.observe(self.update_params, names="value")
