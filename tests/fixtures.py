import os
from shutil import copytree, rmtree

from pytest import fixture


@fixture
def datadir(tmp_path, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        rmtree(tmp_path)
        copytree(test_dir, str(tmp_path))

    return tmp_path
