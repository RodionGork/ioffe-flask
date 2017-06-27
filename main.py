import flask
import os
app = flask.Flask(__name__)

@app.route('/')
def root():
    name = 'Vasyan'
    return flask.render_template('index.html')

@app.route('/task/<id>')
def task(id):
    path = './tasks/%s.txt' % id
    if not os.path.isfile(path):
        flask.abort(404)
    with open(path) as f:
        s = f.read()
    return flask.render_template('task.html', statement = s)

if __name__ == '__main__':
    app.run(debug = True)

