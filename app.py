import flask

app = flask.Flask(__name__, static_folder = 's', template_folder = 't')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/q')
def show_task():
    return flask.render_template('task.html')
