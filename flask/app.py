from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/users/<int:id>/<string:name>')
def users_with_name(id, name):
    return f'Hello World!{id}/{name}'


@app.route('/users/<int:id>')
def users(id):
    return f'Hello World!{id}'


app.run(debug=True)
