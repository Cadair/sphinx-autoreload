Sphinx Autoreload
-----------------

This is a little experiment to make a webserver that will
autorebuild a sphinx page when it is loaded in the browser. This should
enable live preview when editing documentation for anything that
uses sphinx to build its documentation.

## Installation

    pip install git+git://github.com/Cadair/sphinx-autoreload.git

##Usage

The command line script `autoreload-sphinx` will build the sphinx
documentation and start a webserver. When the command is run it will
do a full sphinx build (using any vaild current environment). When a
page is loaded, it will rerun sphinx just for the file requested.

Get Help:
    
    autoreload-sphinx -help

Run with defaults:

    autoreload-sphinx ./doc
