#!/usr/bin/env python3
"""Tests for freshpy.py."""

# Currently just uses code analysis tools to make sure
# there are not too many obvious issues. Will try to
# write some basic unit tests later, but that's about
# it.

# Also, this just calls out to the system to run the
# programs

import sys
from typing import List
import subprocess

files: List[str] = ["freshpy.py", "freshpyconf.py", "tests.py"]

for file_name in files:
    subprocess.call("radon cc " + file_name + " -nc")
    subprocess.call("radon mi " + file_name + " -nc")
    subprocess.call("pylint " + file_name)
    subprocess.call("mypy " + file_name)
    subprocess.call("pycodestyle " + file_name)
    subprocess.call("pydocstyle " + file_name)
    subprocess.call("pyflakes " + file_name)


def test_abort_fatal(msg: str) -> None:
    """Abort with an error message."""
    print(msg)
    print("Aborting.")
    sys.exit()
