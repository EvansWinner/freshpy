#!/usr/bin/env python3
"""Tests for freshpy.py."""

# Currently just uses code analysis tools to make sure
# there are not too many obvious issues. Will try to
# write some basic unit tests later, but that's about
# it.

# Also, this just calls out to the system to run the
# programs

import sys
import os
from typing import List

files: List[str] = ["freshpy.py", "freshpyconf.py", "tests.py"]

for file_name in files:
    os.system("radon cc " + file_name + " -nc")
    os.system("radon mi " + file_name + " -nc")
    os.system("pylint " + file_name)
    os.system("mypy " + file_name)
    os.system("pycodestyle " + file_name)
    os.system("pydocstyle " + file_name)
    os.system("pyflakes " + file_name)


def test_abort_fatal(msg: str) -> None:
    """Abort with an error message."""
    print(msg)
    print("Aborting.")
    sys.exit()
