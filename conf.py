# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add custom paths here if needed
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate Your UHC Card'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare'

# The full version of the project
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# List of patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Page and browser title
html_title = "Activate Your UHC Card at activate.uhc.com – Step-by-Step Guide"

# Optional shorter title (like for navbar)
html_short_title = "UHC Card Activation"

# Theme (default: 'alabaster', or use 'sphinx_rtd_theme', etc.)
# html_theme = 'sphinx_rtd_theme'  # Uncomment if you're using Read the Docs theme

# Disable source link from appearing in HTML
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

# Hide “Powered by Sphinx” footer
html_theme_options = {
    'show_powered_by': False,
}

# Use custom templates directory (if available)
templates_path = ['_templates']

# Enable static files (like CSS, JS, favicon)
# html_static_path = ['_static']  # Uncomment if you have custom static files

# Favicon setup (put favicon.ico in root or _static folder)
html_favicon = 'favicon.ico'
