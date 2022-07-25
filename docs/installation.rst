.. _installation:

========
Install
========
The installers for all releases are available at the
`Python package Index (PyPI) <https://pypi.org/project/pyElli>`_.

To install the package in your current virtual environment execute

    .. code-block:: shell

        pip install pyElli

A complete environment for pyElli is also available as a
`Docker Container <https://hub.docker.com/r/domna/pyelli>`_.
To pull and run it directly just execute

    .. code-block:: shell

        docker run -p 8888:8888 domna/pyelli

from your local docker install. After startup a link should
appear in your console. Click it and you will be directed
to a jupyter server with the latest release of pyElli available.

To install the latest development version use:

    .. code-block:: shell

            pip install git+https://github.com/pyEllips/pyElli.git

The source code is hosted on `GitHub <https://github.com/PyEllips/pyElli>`_,
to manually install from source, clone the repository and run `pip install -e .` in
the folder to install it in development mode:

    .. code-block:: shell

        git clone https://github.com/PyEllips/pyElli
        cd pyElli
        pip install -e .
