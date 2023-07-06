# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lumache'
copyright = '2023, YJN'
author = 'YJN'
release = '0.1'

# -- General configuration
# Including doctests in documentation
#
# import pathlib
# import sys
#
# sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
#
#
#
#
#  ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    # Enable doctest extension
    'sphinx.ext.doctest',
    # autosummary extension
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for EPUB output -------------------------------------------------

epub_show_urls = 'footnote'
