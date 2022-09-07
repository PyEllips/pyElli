# Contributing

Welcome to `pyElli` contributor's guide.

This document focuses on getting any potential contributor familiarized
with the development processes, but `other kinds of contributions` are also
appreciated.

If you are new to using git or have never collaborated in a project previously,
please have a look at [contribution-guide.org](contribution-guide.org).

Please notice, all users and contributors are expected to be **open,
considerate, reasonable, and respectful**. When in doubt, `Python Software Foundation's Code of Conduct` is a good reference in terms of behavior guidelines.

## Issue Reports

If you experience bugs or general issues with `pyElli`, please have a look
on the [issue tracker](https://github.com/PyEllips/pyElli/issues). If you don't see anything useful there, please feel
free to fire an issue report.

    Please don't forget to include the closed issues in your search.
    Sometimes a solution was already reported, and the problem is considered
    solved.

New issue reports should include information about your programming environment
(e.g., operating system, Python version) and steps to reproduce the problem.
Please try also to simplify the reproduction steps to a very minimal example
that still illustrates the problem you are facing. By removing other factors,
you help us to identify the root cause of the issue.

## Documentation Improvements

You can help improve `pyElli` docs by making them more readable and coherent, or
by adding missing information and correcting mistakes.

`pyElli` documentation uses Sphinx as its main documentation compiler.
This means that the docs are kept in the same repository as the project code, and
that any documentation update is done in the same way was a code contribution.

## Code Contributions

PyElli consists of different classes representing different parts of an ellipsometric
experiment. You can see an overview graph in the [documentation](https://pyelli.readthedocs.io/en/latest/index.html).
If you want to add a dispersion, solver or material class to extend the
present functionality you can do so by creating a new class under the respective abstract base classes.

#### Submit an issue

Before you work on any non-trivial code contribution it's best to first create
a report in the [issue tracker](https://github.com/PyEllips/pyElli/issues) to start a discussion on the subject.
This often provides additional considerations and avoids unnecessary work.

#### Create an environment

Before you start coding, we recommend creating an isolated `virtual environment` to avoid any problems with your installed Python packages.
This can easily be done via either **virtualenv**

    virtualenv <PATH TO VENV>
    source <PATH TO VENV>/bin/activate

or **Miniconda**

    conda create -n pyElli python=3 six virtualenv pytest pytest-cov
    conda activate pyElli

#### Clone the repository

1.  Create an user account on [github](https://github.com/) if you do not already have one.
2.  Fork the [project repository](https://github.com/PyEllips/pyElli/) click on the _Fork_ button near the top of the
    page. This creates a copy of the code under your account on github.
3.  Clone this copy to your local disk

         git clone https://github.com:YourLogin/pyElli.git
         cd pyElli

4.  You should run

          pip install -U pip setuptools -e .[fitting,testing]

    which installs the package in development mode and all extra requirements in your current virtualenv.

### Implement your changes

1.  Create a branch to hold your changes

        git checkout -b my-feature

    and start making changes. Never work on the master branch!

2.  Start your work on this branch. Don't forget to add docstrings to new
    functions, modules and classes, especially if they are part of public APIs.

3.  Add yourself to the list of contributors in `AUTHORS.md`.

4.  When you’re done editing, do

        git add <MODIFIED FILES>
        git commit

    to record your changes in git.

    **Important:** Don't forget to add unit tests and documentation in case your
    contribution adds an additional feature and is not just a bugfix.

    Moreover, writing a `descriptive commit message` is highly recommended.
    In case of doubt, you can check the commit history with:

        git log --graph --decorate --pretty=oneline --abbrev-commit --all

    to look for recurring communication patterns.

5.  Please check that your changes don't break any unit tests with:

        pytest

6.  If you added features, please add them to the documentation and check the documentation status locally by running

        python setup.py build_sphinx

    This should create html pages in `build/sphinx/html` for you.

7.  We are using the python [black formatter](https://black.readthedocs.io/en/stable/) throughout the code and sphinx-lint for the docstrings.
    We supply a pre-commit hook which you can install accordingly to
    pre-commits [documentation](https://pre-commit.com/#install),
    which checks black formatting before the code is committed.
    For sphinx you have to invoke it manually by installing with

        pip install sphinx-lint

    and running

        sphinx-lint

    in the project directory.

### Submit your contribution

1.  If everything works fine, push your local branch to github with:

         git push -u origin my-feature

2.  Go to the web page of your fork and create a pull request to send your changes for review.
