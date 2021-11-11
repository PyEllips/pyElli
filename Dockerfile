FROM domna/jupyter-tf-base

ENV APP_HOME=/home/jovyan/berreman4x4
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY --chown=${NB_UID}:${NB_GID} . $APP_HOME
RUN pip install --quiet --no-cache-dir 'flake8==3.9.2' -r requirements.txt
RUN python setup.py develop

WORKDIR /home/jovyan