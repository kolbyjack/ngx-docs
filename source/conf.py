# -*- coding: utf-8 -*-
'''
Sphinx Documentation for Nginx
'''

import os
import sys
import sphinx_rtd_theme

sys.path.append(os.path.abspath('../_modules'))

# -- General configuration -----------------------------------------------------

extensions = ['ngxblock', 'text']
templates_path = ['../_templates']
source_suffix = '.txt'
master_doc = 'index'
project = u'Nginx'
copyright = u'2013, Ngx Community Center'
version = 'latest'
release = 'latest'
#language = None
today_fmt = '%B %d, %Y'
exclude_patterns = ['../_build']
show_authors = False
pygments_style = 'sphinx'
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

html_theme = 'sphinx_rtd_theme'
#html_theme_options = {}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = None
html_short_title = 'Ngx CC'
#html_logo = None
#html_favicon = None
html_static_path = ['../_static']
html_last_updated_fmt = '%b %d, %Y'
html_use_smartypants = False
html_use_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
htmlhelp_basename = 'NgxDoc'


# -- Options for LaTeX output --------------------------------------------------

#latex_paper_size = 'letter'
#latex_font_size = '10pt'
latex_documents = [
  ('index', 'NgxDocs.tex', u'Ngx Community Documentation',
   u'Ngx Community Center', 'manual'),
]
#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_preamble = ''
#latex_appendices = []
#latex_domain_indices = True
