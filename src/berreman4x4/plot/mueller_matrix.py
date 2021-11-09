"""Plotting functions for Mueller matrices"""
import plotly.graph_objects as go
import pandas as pd
COLORS = ['#636EFA', '#EF553B', '#00CC96',
          '#AB63FA', '#FFA15A', '#19D3F3',
          '#FF6692', '#B6E880', '#FF97FF',
          '#FECB52']

def plot_mmatrix(dataframes: pd.DataFrame,
                 colors:list=None,
                 dashes:list=None,
                 names:list=None) -> go.Figure:
    """Takes multiple Mueller matrix dataframes with columns Mxy for matrix postion x,y
    and plots them together."""
    if colors is None:
        colors = COLORS
    if dashes is None:
        dashes = ['solid', 'dash', 'dot']
    if names is None:
        names = ['', 'theory']

    fig = go.FigureWidget()
    for i, melem in enumerate(dataframes[0]):
        coli = colors[i % len(colors)]
        for j, mueller_df in enumerate(dataframes):
            dashi = dashes[j % len(dashes)]
            namesi = names[j % len(names)]
            fig.add_trace(go.Scatter(x=mueller_df.index,
                                     y=mueller_df[melem],
                                     name=f'{melem} {namesi}',
                                     line=dict(color=coli, dash=dashi)))

    fig.update_layout(yaxis_title='Müller Matrix Elements', xaxis_title='Wavelength (nm)')
    return fig
