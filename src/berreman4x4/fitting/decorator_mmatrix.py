"""Decorator functions for convenient fitting
of Mueller matrices"""
from ipywidgets import widgets
from IPython.display import display
import pandas as pd
from lmfit import minimize
from ..plot.mueller_matrix import plot_mmatrix

def mmatrix_to_dataframe(exp_df, mueller_matrix):
    """Reshape a numpy 4x4 array containing mueller matrix elements
    to a dataframe with columns Mxy. The index labels for each column
    are taken from the provided exp_df."""
    mueller_df = pd.DataFrame(index=exp_df.index, columns=exp_df.columns, dtype='float64')
    mueller_df.values[:] = mueller_matrix.reshape(-1, 16)

    return mueller_df

class FitMuellerMatrix():
    """A class to fit mueller matrices to experimental data"""

    def update_params(self, change):
        """Update plot after a change of fitting parameters"""
        self.params[change.owner.description].value = change.new

        with self.fig.batch_update():
            model_df = mmatrix_to_dataframe(self.exp_mm,
                                            self.model(self.exp_mm.index.values,
                                                       self.params).mueller_matrix)

            for i, melem in enumerate(model_df):
                self.fig.data[2*i+1].y = model_df[melem]

    def create_widgets(self):
        """Create ipywidgets for parameter estimation"""
        widget_list = []
        for param in self.params.valuesdict():
            curr_widget = widgets.BoundedFloatText(self.params[param],
                                                   min=self.params[param].min,
                                                   max=self.params[param].max,
                                                   description=param,
                                                   continuous_update=False)
            curr_widget.observe(self.update_params, names=('value', 'owner'))
            widget_list.append(curr_widget)

        display(widgets.VBox([widgets.HBox(widget_list,
                                           layout=widgets.Layout(width='100%',
                                                                 display='inline-flex',
                                                                 flex_flow='row wrap')),
                              self.fig]))

    def fit_function(self, params, lbda, mueller_matrix):
        """The fit function to minimize the fitting problem"""
        return mueller_matrix.values.reshape(-1, 4, 4) - self.model(lbda, params).mueller_matrix

    def fit(self, method='leastsq'):
        """Execute the lmfit with the current fitting parameters"""
        res = minimize(self.fit_function,
                       self.params,
                       args=(self.exp_mm.index.values, self.exp_mm),
                       method=method)

        self.fitted_params = res.params
        return res

    def get_fit_data(self):
        """Get the fit results as dataframe"""
        return mmatrix_to_dataframe(self.exp_mm,
                                    self.model(self.exp_mm.index.values,
                                                self.fitted_params).mueller_matrix)

    def plot(self, display_single:bool=None):
        """Plot the fit results"""
        if display_single is None:
            display_single = self.display_single
        fit_result = mmatrix_to_dataframe(self.exp_mm,
                                          self.model(self.exp_mm.index.values,
                                                     self.fitted_params).mueller_matrix)

        return plot_mmatrix([self.exp_mm, fit_result], single=display_single)

    def __init__(self, exp_mm, params, model, display_single):
        self.exp_mm = exp_mm
        self.params = params
        self.fitted_params = params.copy()
        self.model = model
        self.display_single = display_single

        model_df = mmatrix_to_dataframe(exp_mm, model(exp_mm.index.values, params).mueller_matrix)
        self.fig = plot_mmatrix([exp_mm,
                                 model_df], single=display_single)

        self.create_widgets()

def fit_mueller_matrix(exp_mm, params, display_single=True):
    """A parameters decorator for fitting mueller matrices"""
    return lambda model: FitMuellerMatrix(exp_mm, params, model, display_single)
