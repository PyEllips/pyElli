"""Plotting functions for Mueller matrices"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
COLORS = ['#636EFA', '#EF553B', '#00CC96',
          '#AB63FA', '#FFA15A', '#19D3F3',
          '#FF6692', '#B6E880', '#FF97FF',
          '#FECB52']

def plot_mmatrix(dataframes: pd.DataFrame,
                 colors:list=None,
                 dashes:list=None,
                 names:list=None,
                 single:bool=True,
                 full_scale:bool=False,
                 sharex:bool=False) -> go.Figure:
    """Takes multiple Mueller matrix dataframes with columns Mxy for matrix postion x,y
    and plots them together."""
    if colors is None:
        colors = COLORS
    if dashes is None:
        dashes = ['solid', 'dash', 'dot']
    if names is None:
        names = ['', 'theory']

    if single:
        fig = go.Figure()
        fig.update_layout(yaxis_title='Müller Matrix Elements', xaxis_title='Wavelength (nm)')
    else:
        fig = make_subplots(rows=4, cols=4)
        if full_scale:
            fig.update_yaxes(range=[-1, 1])

    for i, melem in enumerate(dataframes[0]):
        coli = colors[i % len(colors)]
        for j, mueller_df in enumerate(dataframes):
            dashi = dashes[j % len(dashes)]
            namesi = names[j % len(names)]
            if single:
                fig.add_trace(go.Scatter(x=mueller_df.index,
                                        y=mueller_df[melem],
                                        name=f'{melem} {namesi}',
                                        line=dict(color=coli, dash=dashi)))
            else:
                fig.add_trace(go.Scatter(x=mueller_df.index,
                                        y=mueller_df[melem],
                                        name=f'{melem} {namesi}',
                                        line=dict(color=coli, dash=dashi)),
                                        row=1 if single else i//4 + 1, col=1 if single else i%4 + 1)
    if sharex:
        fig.update_xaxes(matches='x')
    return go.FigureWidget(fig)
