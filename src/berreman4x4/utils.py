# Encoding: utf-8
import pandas as pd
import numpy as np
import scipy.constants as sc
from ipywidgets import widgets
from IPython.display import display
from lmfit import minimize
import plotly.graph_objects as go
from types import SimpleNamespace
from numpy.lib.scimath import sqrt

from .dispersions import DispersionTableEpsilon


def calcPseudoDiel(rho, angle: float, output: str = 'eps') -> pd.DataFrame:
    """Calculates the pseudo dielectric function of a measurement from rho.

    Args:
        rho (pandas.DataFrame): Measurement DataFrame containing rho as complex number as column and wavelength as index
        angle (float): Angle of measurement in degree
        output (str, optional): Output format for dielectric function.
            'n': refractive index,
            'eps': Dielectic function as two-column pandas.DataFrame,
            'epsi': Dielectric function as imaginary number.
            Defaults to 'eps'.

    Returns:
        pandas.DataFrame: Frame containing the pseudo dielectric function or refractive index.
    """
    theta = angle * np.pi / 180
    eps = np.sin(theta)**2 * (1 + np.tan(theta)**2 * ((1 - rho) / (1 + rho))**2)

    if output == 'n':
        n = sqrt(eps)
        return pd.DataFrame({'n': n.real,
                             'k': n.imag}, index=eps.index)

    if output == 'epsi':
        return eps

    return pd.concat({'ϵ1': eps.apply(lambda x: x.real),
                      'ϵ2': eps.apply(lambda x: x.imag)}, axis=1)


def calc_rho(psi_delta: pd.DataFrame) -> pd.DataFrame:
    """Calculate rho from a Psi-Delta DataFrame. The Psi-Delta DataFrame should be structured as follows:
        index: Wavelength
        column 'Ψ': Psi from measurement
        column 'Δ': Delta from measurement

        This format is as returned from SpectraRay.read_psi_delta_file(...).

    Args:
        psi_delta (pandas.DataFrame): DataFrame containing Psi+Delta Measurement data

    Returns:
        pandas.DataFrame: Frame containing rho as an imaginary number.
    """
    return psi_delta.apply(lambda x: np.tan(np.deg2rad(x['Ψ'])) *
                           np.exp(-1j * np.deg2rad(x['Δ'])),
                           axis=1)


def manual_parameters(exp_data, params, angle: float = 70):

    def decorator_func(model):
        fig = go.FigureWidget(pd.concat([exp_data,
                                        pd.DataFrame({'Ψ_tmm': model(exp_data.index, params).psi,
                                                      'Δ_tmm': model(exp_data.index, params).delta},
                                                     index=exp_data.index)]).plot())

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


class SpectraRay():

    def __init__(self, path: str) -> None:
        self.spectraray_path = path

    def loadDispersionTable(self, fname: str) -> DispersionTableEpsilon:
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
    def read_psi_delta_file(fname: str, decimal: str = '.') -> pd.DataFrame:
        return pd.read_csv(fname,
                           index_col=0,
                           sep=r'\s+',
                           decimal=decimal,
                           usecols=[0, 1, 2],
                           names=['Wavelength', 'Ψ', 'Δ'],
                           skiprows=1)

    @staticmethod
    def read_rho(fname: str, decimal: str = '.') -> pd.DataFrame:
        psi_delta = SpectraRay.read_psi_delta_file(fname, decimal)
        return calc_rho(psi_delta)

    @staticmethod
    def eV2nm(wlen):
        return sc.value('Planck constant in eV s') * sc.c * 1e9 / wlen


def get_QWP_thickness(material: "Material", lbda: float) -> float:
    """Return the thickness in nm of a Quater Wave Plate at wavelength 'lbda'."""
    nr = np.real(material.getRefractiveIndex(lbda)[0, 0, 0])
    return lbda / (4.*nr)
