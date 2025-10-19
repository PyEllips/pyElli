# Contributing

We're happy that you are interested in contributing to pyElli!

There are several ways of contributing to pyElli.
The easiest is reporting issues or starting discussions.
If you want to dive deeper feel free to open a pull request or contact us
if you need some help.
We're eager to help you if you want to contribute code to pyElli even if you feel
you don't bring a lot of knowledge (yet). We are happy to assist.

## Reporting an Issue

If you are encountering problems with pyElli or have a feature request
please open an issue at our [Github Issues Page](https://github.com/PyEllips/pyElli/issues).

Please try to provide a minimal example for reproducing the issue.
This makes it a lot easier for the developers to work on the problem.

If you are not entirely sure whether the problem you're encountering is actually a bug
or if you want to discuss some feature ideas feel free to post on our [Github Discussion Page](https://github.com/orgs/PyEllips/discussions)

## Making a Pull Request

```sh
git clone --recurse-submodules https://github.com/PyEllips/pyElli
cd pyElli
```

=== "pip"

    ```sh
    pip install -e '.[dev,docs,fitting]
    ```

=== "uv"

    ```sh
    uv sync --extra dev --extra docs --extra fitting
    ```