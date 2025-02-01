
# import libraries
import sys
import pyrootutils

root = pyrootutils.setup_root(sys.path[0], pythonpath=True, cwd=True)

def add_two_numbers(a, b):
	return a + b