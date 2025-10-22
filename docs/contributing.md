# Contributing

We're happy that you are interested in contributing to pyElli!

You can contribute by reporting issues, starting discussions or open pull requests yourself
to contribute code directly.
In case you need help don't hesitate to ask for it.

## Reporting an Issue

If you are encountering problems with pyElli or have a feature request
open an issue at pyElli's [Github Issues Page](https://github.com/PyEllips/pyElli/issues).

Ideally, you'll provide a minimal example to reproduce the issue.
This will make it a lot easier to work on the problem.

If you are not entirely sure whether the problem you're encountering is actually a bug
or if you want to discuss some feature ideas feel free to post on pyElli's [Github Discussion Page](https://github.com/orgs/PyEllips/discussions)

## Making a Pull Request

In case you want to contribute your own code to pyElli you can open a pull request.
To do this you need to fork pyElli first and create the pull request from your fork.
[Github's excellent documentation on the topic](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) will be helpful if you need help to create a fork.

### Setting up the repository and development environment

First, clone the repo to start working on the code.
Replace `https://github.com/PyEllips/pyElli` with the url of your fork.

```sh
git clone --recurse-submodules https://github.com/PyEllips/pyElli
cd pyElli
```

In the next step we install the package in development mode.
We recommend using [uv](https://docs.astral.sh/uv/), which will manage a dedicated python
virtual environment for the project.
However, any virtual environment should work.

=== "uv"

    ```sh
    uv sync --extra dev --extra docs --extra fitting
    ```

=== "pip"

    ```sh
    pip install -e '.[dev,docs,fitting]
    ```

Now you're ready to make your changes to the code.

### Testing

Before opening a pull request please ensure that the tests pass and the code passes
the linting checks and is formatted properly.
We use the tool [ruff](https://docs.astral.sh/ruff/) to check linting and formatting
and [pytest](https://docs.pytest.org/en/stable/) for testing.

=== "uv"

    ```sh
    uv run pytest
    uv run ruff check .
    uv run ruff format .
    ```

=== "pip"

    ```sh
    pytest
    ruff check .
    ruff format .
    ```