from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/users/<int:id>/<string:name>')
def users_with_name(id: int, name: str):
    return f'Hello World!{id}/{name}'


@app.route('/users/<int:id>')
def users(id: int):
    return f'Hello World!{id}'


if __name__ == '__main__':
    app.run(debug=True)
