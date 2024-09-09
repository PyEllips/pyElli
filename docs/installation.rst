.. _installation:

========
Install
========
The installers for all releases are available at the
`Python package Index (PyPI) <https://pypi.org/project/pyElli>`_.

To install the package in your current virtual environment execute

    .. code-block:: shell

        pip install pyElli[fitting]

This installs pyElli with the additional fitting capabilities and interactive widgets.
If you don't want to have this functionality just drop the `[fitting]` in the end.

To increase performance of the 4x4 Solver, it is recommended to
install PyTorch manually, as it is too big to include in the standard installation.
Installation information can be found at the `PyTorch Website <https://pytorch.org/get-started/locally/>`_.
The CPU variant is sufficient, if you want to save some space.

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
