## import libraries
import sys
import pyrootutils
root = pyrootutils.setup_root(sys.path[0], pythonpath=True, cwd=True)

from src.main import add_two_numbers
import pytest

def test_add_two_numbers():
	assert add_two_numbers(1, 2) == 3
	assert add_two_numbers(0, 0) == 0
	assert add_two_numbers(-1, 1) == 0
	assert add_two_numbers(-1, -1) == -2
	assert add_two_numbers(1, -1) == 0

	