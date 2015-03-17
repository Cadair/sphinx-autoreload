# Default Config
import os

DOCS_BASE = '.'
SOURCE_DIR = os.path.realpath(DOCS_BASE)
CONF_DIR = os.path.realpath(DOCS_BASE)
OUT_DIR = os.path.realpath(os.path.join(DOCS_BASE, '_build'))
DOCTREE_DIR = os.path.realpath(os.path.join(DOCS_BASE, '.doctrees'))
PORT = 2105
