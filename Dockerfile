FROM jupyter/scipy-notebook

ENV HOME=/home/jovyan
WORKDIR $HOME

RUN pip install pyElli[fitting]

WORKDIR $HOME/work
ADD examples ./