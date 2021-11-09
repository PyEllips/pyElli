"""Decorator functions for convenient fitting"""
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from lmfit import minimize
from ipywidgets import widgets
from IPython.display import display
from ..utils import calcPseudoDiel, calc_rho

class FitRho():
    """A class to fit psi/delta or rho based ellipsometry data with two degress of freedom"""

    def set_psi_delta(self, update_exp:bool=False, update_names:bool=False) -> None:
        """Sets Plot to Psi/Delta values
            :update_exp: Flag to change the experimental data as well
            :update_names: Flag to change the label names"""
        data = self.model(self.exp_data.index, self.params)
        self.fig.update_layout(yaxis_title="Ψ/Δ (°)")
        self.fig.data[2].y = data.psi
        self.fig.data[3].y = data.delta

        if update_exp:
            self.fig.data[0].y = self.exp_data.loc[:, 'Ψ']
            self.fig.data[1].y = self.exp_data.loc[:, 'Δ']

        if update_names:
            self.fig.data[0].name = 'Ψ'
            self.fig.data[1].name = 'Δ'
            self.fig.data[2].name = 'Ψ_tmm'
            self.fig.data[3].name = 'Δ_tmm'

    def set_rho(self, update_exp:bool=False, update_names:bool=False) -> None:
        """Sets Plot to Rho values
            :update_exp: Flag to change the experimental data as well
            :update_names: Flag to change the label names"""
        data = self.model(self.exp_data.index, self.params)
        self.fig.update_layout(yaxis_title="ρ")
        self.fig.data[2].y = data.rho.real
        self.fig.data[3].y = data.rho.imag

        if update_exp:
            exp_rho = calc_rho(self.exp_data)
            self.fig.data[0].y = exp_rho.apply(lambda x: x.real).values
            self.fig.data[1].y = exp_rho.apply(lambda x: x.imag).values

        if update_names:
            self.fig.data[0].name = 'ρr'
            self.fig.data[1].name = 'ρi'
            self.fig.data[2].name = 'ρr_tmm'
            self.fig.data[3].name = 'ρi_tmm'

    def set_pseudo_diel(self, update_exp:bool=False, update_names:bool=False) -> None:
        """Sets Plot to Pseudo Dielectric function values
            :update_exp: Flag to change the experimental data as well
            :update_names: Flag to change the label names"""
        data = self.model(self.exp_data.index, self.params)
        peps = calcPseudoDiel(pd.DataFrame(data.rho, index=self.exp_data.index).iloc[:, 0],
                                          self.angle)
        self.fig.update_layout(yaxis_title="ϵ")
        self.fig.data[2].y = peps.loc[:, 'ϵ1']
        self.fig.data[3].y = peps.loc[:, 'ϵ2']

        if update_exp:
            exp_peps = calcPseudoDiel(calc_rho(self.exp_data), self.angle)
            self.fig.data[0].y = exp_peps.loc[:, 'ϵ1']
            self.fig.data[1].y = exp_peps.loc[:, 'ϵ2']

        if update_names:
            self.fig.data[0].name = 'ϵ1'
            self.fig.data[1].name = 'ϵ2'
            self.fig.data[2].name = 'ϵ1_tmm'
            self.fig.data[3].name = 'ϵ2_tmm'

    def update_params(self, change, selected):
        """Update plot after a change of fitting parameters"""
        self.params[change.owner.description].value = change.new

        with self.fig.batch_update():
            update = self.update_dict.get(selected.value)
            if update is not None:
                update()

    def update_selection(self, change):
        """Update plot after selection of displayed data"""

        with self.fig.batch_update():
            update = self.update_dict.get(change.new)
            if update is not None:
                update(update_exp=True, update_names=True)

    def create_widgets(self):
        """Create ipywidgets for parameter estimation"""
        widget_list = []
        for param in self.params.valuesdict():
            curr_widget = widgets.BoundedFloatText(self.params[param],
                                                   min=self.params[param].min,
                                                   max=self.params[param].max,
                                                   description=param,
                                                   continuous_update=False)
            curr_widget.observe(lambda x: self.update_params(x, selector), names=('value', 'owner'))
            widget_list.append(curr_widget)

        selector = widgets.Dropdown(
            options=['Psi/Delta', 'Rho', 'Pseudo Diel.'],
            value='Psi/Delta',
            description='Display: ',
            disabled=False
        )
        selector.observe(self.update_selection, names='value')
        widget_list.append(selector)

        display(widgets.VBox([widgets.HBox(widget_list,
                                           layout=widgets.Layout(width='100%',
                                                                 display='inline-flex',
                                                                 flex_flow='row wrap')),
                              self.fig]))

    def fit_function(self, params, lbda, rhor, rhoi):
        """The fit function to minimize the fitting problem"""
        result = self.model(lbda, params)

        resid_rhor = rhor - result.rho.real
        resid_rhoi = rhoi - result.rho.imag

        return np.concatenate((resid_rhor, resid_rhoi))

    def fit(self, method='leastsq'):
        """Execute the lmfit with the current fitting parameters"""
        rho = calc_rho(self.exp_data)
        res = minimize(self.fit_function,
                       self.params,
                       args=(rho.index.to_numpy(), rho.values.real, rho.values.imag),
                       method=method)

        self.fitted_params = res.params
        return res

    def plot(self):
        """Plot the fit results as Psi/Delta"""
        fit_result = self.model(self.exp_data.index.to_numpy(), self.fitted_params)

        return go.FigureWidget(pd.concat([self.exp_data,
                                            pd.DataFrame({'Ψ_fit': fit_result.psi,
                                                        'Δ_fit': fit_result.delta},
                                                        index=self.exp_data.index)]
                                            ).plot())

    def plot_rho(self):
        """Plot the fit results as Rho"""
        rho = calc_rho(self.exp_data)
        fit_result = self.model(rho.index.to_numpy(), self.fitted_params)

        return go.FigureWidget(pd.DataFrame({'ρr': rho.apply(lambda x: x.real),
                                             'ρi': rho.apply(lambda x: x.imag),
                                             'ρcr': fit_result.rho.real,
                                             'ρci': fit_result.rho.imag},
                                             index=rho.index).plot())

    def __init__(self, exp_data, params, model, angle:float = 70):
        self.model = model
        self.exp_data = exp_data
        self.params = params
        self.fitted_params = params.copy()
        self.angle = angle
        self.fig = go.FigureWidget(pd.concat([exp_data,
                    pd.DataFrame({'Ψ_tmm': model(exp_data.index, params).psi,
                                 'Δ_tmm': model(exp_data.index, params).delta},
                                 index=exp_data.index)]).plot(backend='plotly'))
        self.fig.update_layout(yaxis_title="Ψ/Δ (°)", xaxis_title="Wavelength (nm)")

        self.update_dict = {'Psi/Delta': self.set_psi_delta,
                            'Rho': self.set_rho,
                            'Pseudo Diel.': self.set_pseudo_diel}

        self.create_widgets()

def fit(exp_data, params, angle: float = 70):
    """A manual parameters decorator for providing convenient fitting functions"""
    return lambda model: FitRho(exp_data, params, model, angle)
