"""Plotting functions for Mueller matrices"""
# Encoding: utf-8
from typing import List, Union, Optional

import pandas as pd

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
except ImportError as e:
    raise ImportError(
        "Optional dependency plotly is not installed. This module will not work properly.\n"
        "Try installing this package with the additional fitting requirement, "
        "i.e. pip install pyElli[fitting]"
    ) from e

COLORS = [
    "#636EFA",
    "#EF553B",
    "#00CC96",
    "#AB63FA",
    "#FFA15A",
    "#19D3F3",
    "#FF6692",
    "#B6E880",
    "#FF97FF",
    "#FECB52",
]


def plot_mmatrix(
    dataframes: Union[pd.DataFrame, List[pd.DataFrame]],
    colors: Optional[List[str]] = None,
    dashes: Optional[List[str]] = None,
    names: Optional[List[str]] = None,
    single: bool = True,
    full_scale: bool = False,
    sharex: bool = False,
) -> go.Figure:
    """Takes multiple Mueller matrix dataframes with columns Mxy for matrix postion x,y
    and plots them together. Needs plotly as additional requirement to work.

    Args:
        dataframes (Union[pd.Dataframe, List[pd.DataFrame]]):
            A dataframe or a list of dataframes containing data of the same index.
        colors (Optional[List[str]], optional):
            A list of colors which are cycled for each dataframes index. Defaults to None.
        dashes (Optional[List[str]], optional):
            A list of dash line styles which are cycled for each dataframes index. Defaults to None.
        names (Optional[List[str]], optional): A name for each dataframe index. Defaults to None.
        single (bool, optional): Uses a single plot if set and a grid if not set. Defaults to True.
        full_scale (bool, optional): Sets the y-axis limits to [-1, 1] if set. Defaults to False.
        sharex (bool, optional):
            Ties the zooming of the x-axis together for each plot in grid view. Defaults to False.

    Returns:
        go.Figure: A plotly figure containing the data from dataframes as a grid or single view.
    """
    if isinstance(dataframes, pd.DataFrame):
        dataframes = [dataframes]

    if colors is None:
        colors = COLORS
    if dashes is None:
        dashes = ["solid", "dash", "dot"]
    if names is None:
        names = ["", "theory"]

    if single:
        fig = go.Figure()
        fig.update_layout(
            yaxis_title="Müller Matrix Elements", xaxis_title="Wavelength (nm)"
        )
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
                fig.add_trace(
                    go.Scatter(
                        x=mueller_df.index,
                        y=mueller_df[melem],
                        name=f"{melem} {namesi}",
                        line=dict(color=coli, dash=dashi),
                    )
                )
            else:
                fig.add_trace(
                    go.Scatter(
                        x=mueller_df.index,
                        y=mueller_df[melem],
                        name=f"{melem} {namesi}",
                        line=dict(color=coli, dash=dashi),
                    ),
                    row=1 if single else i // 4 + 1,
                    col=1 if single else i % 4 + 1,
                )
    if sharex:
        fig.update_xaxes(matches="x")
    return go.FigureWidget(fig)
