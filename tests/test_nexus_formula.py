"""Test loading optical models from nexus dispersive material files"""
from fixtures import datadir

from elli.importer.nexus import read_nexus_materials


def test_loading_without_errors(datadir):
    """All dispersive materials are loaded without errors"""
    for file in datadir.iterdir():
        read_nexus_materials(file)
