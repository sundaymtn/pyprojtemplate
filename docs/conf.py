"""Sphinx configuration."""
project = "Python Project Template"
author = "Seth Carter"
copyright = "2022, Seth Carter"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
