#!/bin/bash

uv pip compile --generate-hashes --output-file=requirements/requirements.txt pyproject.toml

uv pip compile --extra=fitting --generate-hashes --output-file=requirements/fitting-requirements.txt \
    requirements/requirements.txt pyproject.toml

uv pip compile --extra=fitting --extra=dev --generate-hashes \
    --output-file=requirements/dev-requirements.txt \
    requirements/fitting-requirements.txt \
    pyproject.toml