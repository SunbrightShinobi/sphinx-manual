#!/usr/bin/env python3

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('./source/common'))
sys.path.append(os.path.abspath('./source/configs'))
sys.path.append(os.path.abspath('./source/scripts'))
sys.path.append(os.path.abspath('./source/common_docs'))

# -- Project information -----------------------------------------------------

project = 'Sphinx Manual'
copyright = '2020, Josh Johnson @binarylandscapes'
author = 'Josh Johnson @binarylandscapes'

# Load the rest of the default configuration
exec(open(r'./common/sphinx_defaults.py').read())

