#!/usr/bin/python3

# add_integer.py
import importlib.util
import os

# locate the real file
here = os.path.dirname(__file__)
file_path = os.path.join(here, '0-add_integer.py')

# load it as a module
spec = importlib.util.spec_from_file_location("add_integer_real", file_path)
_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_mod)

# expose the function
add_integer = _mod.add_integer
