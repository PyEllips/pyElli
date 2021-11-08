"""Decorator functions for convenient fitting"""
from types import SimpleNamespace
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from lmfit import minimize
from ipywidgets import widgets
from IPython.display import display
from ..utils import calcPseudoDiel, calc_rho

def manual_parameters(exp_data, params, angle: float = 70):

    def decorator_func(model):
        fig = go.FigureWidget(pd.concat([exp_data,
                                        pd.DataFrame({'Ψ_tmm': model(exp_data.index, params).psi,
                                                      'Δ_tmm': model(exp_data.index, params).delta},
                                                     index=exp_data.index)]).plot(backend='plotly'))

        def update_params(v, fig, selected):
            params[v.owner.description].value = v.new

            with fig.batch_update():
                data = model(exp_data.index, params)

                if selected.value == 'Psi/Delta':
                    fig.data[2].y = data.psi
                    fig.data[3].y = data.delta
                elif selected.value == 'Rho':
                    fig.data[2].y = data.rho.real
                    fig.data[3].y = data.rho.imag
                elif selected.value == 'Pseudo Diel.':
                    peps = calcPseudoDiel(pd.DataFrame(data.rho, index=exp_data.index).iloc[:, 0],
                                          angle)
                    fig.data[2].y = peps.loc[:, 'ϵ1']
                    fig.data[3].y = peps.loc[:, 'ϵ2']

        def update_selection(v, fig):
            with fig.batch_update():
                data = model(exp_data.index, params)

                if v.new == 'Psi/Delta':
                    fig.data[0].y = exp_data.loc[:, 'Ψ']
                    fig.data[1].y = exp_data.loc[:, 'Δ']
                    fig.data[2].y = data.psi
                    fig.data[3].y = data.delta
                    fig.data[0].name = 'Ψ'
                    fig.data[1].name = 'Δ'
                    fig.data[2].name = 'Ψ_tmm'
                    fig.data[3].name = 'Δ_tmm'
                elif v.new == 'Rho':
                    exp_rho = calc_rho(exp_data)

                    fig.data[0].y = exp_rho.apply(lambda x: x.real).values
                    fig.data[1].y = exp_rho.apply(lambda x: x.imag).values
                    fig.data[2].y = data.rho.real
                    fig.data[3].y = data.rho.imag
                    fig.data[0].name = 'ρr'
                    fig.data[1].name = 'ρi'
                    fig.data[2].name = 'ρr_tmm'
                    fig.data[3].name = 'ρi_tmm'
                elif v.new == 'Pseudo Diel.':
                    exp_peps = calcPseudoDiel(calc_rho(exp_data), angle)
                    peps = calcPseudoDiel(pd.DataFrame(data.rho, index=exp_data.index).iloc[:, 0],
                                          angle)
                    fig.data[0].y = exp_peps.loc[:, 'ϵ1']
                    fig.data[1].y = exp_peps.loc[:, 'ϵ2']
                    fig.data[2].y = peps.loc[:, 'ϵ1']
                    fig.data[3].y = peps.loc[:, 'ϵ2']
                    fig.data[0].name = 'ϵ1'
                    fig.data[1].name = 'ϵ2'
                    fig.data[2].name = 'ϵ1_tmm'
                    fig.data[3].name = 'ϵ2_tmm'

        widget_list = []
        selector = widgets.Dropdown(
            options=['Psi/Delta', 'Rho', 'Pseudo Diel.'],
            value='Psi/Delta',
            description='Display: ',
            disabled=False
        )
        for param in params.valuesdict():
            curr_widget = widgets.BoundedFloatText(params[param],
                                                   min=params[param].min,
                                                   max=params[param].max,
                                                   description=param,
                                                   continuous_update=False)
            curr_widget.observe(lambda x: update_params(x, fig, selector), names=('value', 'owner'))
            widget_list.append(curr_widget)
        selector.observe(lambda x: update_selection(x, fig), names='value')
        widget_list.append(selector)

        display(widgets.VBox([widgets.HBox(widget_list,
                                           layout=widgets.Layout(width='100%',
                                                                 display='inline-flex',
                                                                 flex_flow='row wrap')),
                              fig]))

        def fit_function(params, lbda, rhor, rhoi):
            result = model(lbda, params)

            resid_rhor = rhor - result.rho.real
            resid_rhoi = rhoi - result.rho.imag

            return np.concatenate((resid_rhor, resid_rhoi))

        def execute_fit(method='leastsq'):
            rho = calc_rho(exp_data)
            return minimize(fit_function,
                            params,
                            args=(rho.index.to_numpy(), rho.values.real, rho.values.imag),
                            method=method)

        def fit_result(params):
            fit_result = model(exp_data.index.to_numpy(), params)

            return go.FigureWidget(pd.concat([exp_data,
                                              pd.DataFrame({'Ψ_fit': fit_result.psi,
                                                            'Δ_fit': fit_result.delta},
                                                           index=exp_data.index)]
                                             ).plot())

        def fit_result_rho(params):
            rho = calc_rho(exp_data)
            fit_result = model(rho.index.to_numpy(), params)

            return go.FigureWidget(pd.DataFrame({'ρr': rho.apply(lambda x: x.real),
                                                 'ρi': rho.apply(lambda x: x.imag),
                                                 'ρcr': fit_result.rho.real,
                                                 'ρci': fit_result.rho.imag},
                                                index=rho.index).plot())

        return SimpleNamespace(**{'value': model,
                                  'residual': fit_function,
                                  'fit': execute_fit,
                                  'plot': fit_result,
                                  'plot_rho': fit_result_rho})

    return decorator_func
