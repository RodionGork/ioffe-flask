import flask
from core import pages

app = flask.Flask(__name__, static_folder = 's')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/q')
@app.route('/q/')
def show_task_root():
    return show_task('')

@app.route('/q/<path:page>')
def show_task(page):
    content = pages.load(page)
    if content is None:
        return page_not_found(None)
    return flask.render_template('task.html', body = content)

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('error404.html'), 404