import flask
import os

app = flask.Flask(__name__, static_folder = 's', template_folder = 't')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/q')
@app.route('/q/')
def show_task_root():
    return show_task('')

@app.route('/q/<path:page>')
def show_task(page):
    page = os.path.abspath('./pages') + '/' + page
    if os.path.isdir(page):
        page += '/_idx'
    page += '.txt'
    if not os.path.isfile(page):
        content = "<h3>Not found: %s</h3>" % page
    else:
        with open(page) as f:
            content = f.read()
    return flask.render_template('task.html', body = content)
