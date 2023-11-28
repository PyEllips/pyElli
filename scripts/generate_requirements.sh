#!/bin/bash

pip-compile --resolver=backtracking --generate-hashes --output-file=requirements/requirements.txt pyproject.toml

pip-compile --resolver=backtracking --extra=fitting --generate-hashes --output-file=requirements/fitting-requirements.txt \
    requirements/requirements.txt pyproject.toml

pip-compile --resolver=backtracking --extra=fitting --extra=testing --generate-hashes \
    --output-file=requirements/dev-requirements.txt \
    requirements/fitting-requirements.txt \
    pyproject.toml