FROM jupyter/scipy-notebook

ENV HOME=/home/jovyan
WORKDIR $HOME

RUN pip install plotly ipython ipywidgets torch
RUN pip install pyElli

WORKDIR $HOME/work