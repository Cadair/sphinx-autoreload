# Default Config
import os

if os.path.isdir('./docs'):
    DOCS_BASE = './docs'
elif os.path.isdir('./doc'):
    DOCS_BASE = './doc'
else:
    raise ValueError("Can't autodetect Doc directory")

SOURCE_DIR = os.path.realpath(DOCS_BASE)
CONF_DIR = os.path.realpath(DOCS_BASE)
OUT_DIR = os.path.realpath(os.path.join(DOCS_BASE, '_build'))
DOCTREE_DIR = os.path.realpath(os.path.join(DOCS_BASE, '.doctrees'))
PORT = 2105
