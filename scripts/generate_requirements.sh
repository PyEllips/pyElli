#!/bin/bash

uv pip compile --generate-hashes --upgrade --output-file=requirements/requirements.txt pyproject.toml

uv pip compile --extra=fitting --generate-hashes --upgrade --output-file=requirements/fitting-requirements.txt \
    requirements/requirements.txt pyproject.toml

uv pip compile --extra=fitting --extra=dev --generate-hashes --upgrade\
    --output-file=requirements/dev-requirements.txt \
    requirements/fitting-requirements.txt \
    pyproject.toml

uv pip compile --extra=fitting --extra=dev --extra=docs --generate-hashes --upgrade\
    --output-file=docs/requirements.txt \
    requirements/dev-requirements.txt \
    pyproject.toml
