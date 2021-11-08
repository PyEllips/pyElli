"""Decorator functions for convenient fitting
of Mueller matrices"""
from ipywidgets import widgets
from IPython.display import display
from ..plot.mueller_matrix import plot_mmatrix

class FitMuellerMatrix():
    """A class to fit mueller matrices to experimental data"""

    def update_params(self, change):
        """Update plot after a change of fitting parameters"""
        self.params[change.owner.description].value = change.new

        with self.fig.batch_update():
            self.fig = plot_mmatrix([self.exp_mm,
                                     self.model(self.exp_mm.index.values,
                                                self.exp_mm,
                                                self.params).mueller_matrix])

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

    def plot(self):
        """Plot the fit results"""
        fit_result = self.model(self.exp_mm.index.values,
                                self.exp_mm,
                                self.fitted_params)

        return plot_mmatrix([self.exp_mm, fit_result])

    def __init__(self, exp_mm, params, model):
        self.exp_mm = exp_mm
        self.params = params
        self.fitted_params = params.copy()
        self.model = model

        self.fig = plot_mmatrix([exp_mm,
                                 model(exp_mm.index.values,
                                       exp_mm,
                                       params).mueller_matrix])

        self.create_widgets()

def fit_mueller_matrix(exp_mm, params):
    """A parameters decorator for fitting mueller matrices"""
    return lambda model: FitMuellerMatrix(exp_mm, params, model)
