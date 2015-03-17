import os

from flask import Flask, send_from_directory, redirect, abort

from sphinx.application import Sphinx

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Serve static files:


@app.route('/_static/<path:path>')
@app.route('/sphinx/_static/<path:path>')
def send_static(path):
        return send_from_directory(os.path.join(app.config['OUT_DIR'], '_static'), path)


@app.route('/_sources/<path:path>')
@app.route('/sphinx/_sources/<path:path>')
def send_sources(path):
        return send_from_directory(os.path.join(app.config['OUT_DIR'], '_sources'), path)


@app.route('/')
def index():
    return redirect('/sphinx/index.html')


@app.route('/sphinx/<path:path>')
def sphinx(path):
    if path.endswith('.html'):
        path = path[:-5]
    source = os.path.join(app.config['SOURCE_DIR'], path)+'.rst'
    if not os.path.isfile(source):
        abort(404)
    app.sphinx_app.build(False, [source])
    output = os.path.join(app.config['OUT_DIR'], path + '.html')
    with open(output, 'r') as fb:
        return fb.read()

# Error Pages:


@app.errorhandler(404)
def notfound(e):
    return "File Not Found {}".format(e)

# Server Starting:


def run(arguments={}):
    app.config.update(arguments)
    print(app.config)
    app.sphinx_app = Sphinx(app.config['SOURCE_DIR'], app.config['CONF_DIR'],
                            app.config['OUT_DIR'], app.config['DOCTREE_DIR'],
                            'html')
    app.sphinx_app.build(force_all=True)
    app.run(port=app.config['PORT'], host='0.0.0.0')


if __name__ == "__main__":
    run()
