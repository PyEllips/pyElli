# Encoding: utf-8
import pandas as pd
import numpy as np
import scipy.constants as sc
from ipywidgets import widgets
from IPython.display import display
import plotly.graph_objects as go

from .dispersions import DispersionTableEpsilon


def calcPseudoDiel(rho, angle):
    theta = angle * np.pi / 180
    eps = np.sin(theta)**2 * (1 + np.tan(theta)**2 * ((1 - rho) / (1 + rho))**2)

    return pd.concat({'ϵ1': eps.apply(lambda x: x.real),
                      'ϵ2': eps.apply(lambda x: x.imag)}, axis=1)


def manual_parameters(exp_data, params):

    def decorator_func(model):
        fig = go.FigureWidget(pd.concat([exp_data, 
                                        pd.DataFrame({'Ψ_tmm': model(exp_data.index, params).psi,
                                                      'Δ_tmm': model(exp_data.index, params).delta}, 
                                                      index=exp_data.index)]).plot())

        def update_params(v, fig):
            params[v.owner.description].value = v.new

            with fig.batch_update():
                data = model(exp_data.index, params)
                fig.data[2].y = data.psi
                fig.data[3].y = data.delta

        widget_list = []
        for param in params.valuesdict():
            curr_widget = widgets.BoundedFloatText(params[param], 
                                                   min=params[param].min, 
                                                   max=params[param].max, 
                                                   description=param, 
                                                   continuous_update=False)
            curr_widget.observe(lambda x: update_params(x, fig), names=('value', 'owner'))
            widget_list.append(curr_widget)

        display(widgets.VBox([widgets.HBox(widget_list, 
                                           layout=widgets.Layout(width='100%', 
                                                                 display='inline-flex',
                                                                 flex_flow='row wrap')), 
                            fig]))
        
    return decorator_func


class SpectraRay():

    def __init__(self, path):
        self.spectraray_path = path

    def loadDispersionTable(self, fname):
        start = 0
        stop = 0
        with open(self.spectraray_path + fname, 'r') as f:
            line = f.readline()
            cnt = 0
            while line:
                if line.strip() == 'Begin of array':
                    start = cnt + 1
                if line.strip() == 'End of array':
                    stop = cnt
                line = f.readline()
                cnt += 1

                if line.startswith('Units='):
                    x_unit = line.split('=')[1].split(',')[0]

        df = pd.read_csv(self.spectraray_path + fname,
                         delim_whitespace=True,
                         skiprows=start, nrows=stop-start,
                         index_col=0, usecols=[0, 1, 2],
                         names=[x_unit, 'ϵ1', 'ϵ2'])

        if x_unit == 'Wavelength':
            return DispersionTableEpsilon(df.index, df.loc[:, 'ϵ1'] + 1j * df.iloc[:, 'ϵ2'])
        elif x_unit == 'eV':
            return DispersionTableEpsilon(SpectraRay.eV2nm(df.index), df.loc[:, 'ϵ1'] + 1j * df.loc[:, 'ϵ2'])

    @staticmethod
    def read_psi_delta_file(fname):
        return pd.read_csv(fname,
                           index_col=0,
                           sep=' ',
                           usecols=[0, 1, 2],
                           names=['Wavelength', 'Ψ', 'Δ'],
                           skiprows=1)

    @staticmethod
    def read_rho(fname):
        psi_delta = SpectraRay.read_psi_delta_file(fname)
        return psi_delta.apply(lambda x: np.tan(np.deg2rad(x['Ψ'])) *
                               np.exp(-1j * np.deg2rad(x['Δ'])),
                               axis=1)

    @staticmethod
    def eV2nm(wlen):
        return sc.value('Planck constant in eV s') * sc.c * 1e9 / wlen
