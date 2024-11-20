import os
import sys

from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    match request.method:
        case 'POST':
            return render_template('login.html', name='POST', title='Webpage')
        case 'GET':
            return render_template(os.path.join(sys.path[0], 'templates', 'login.html'), name='GET', title='Webpage')


@app.route('/register', methods=['POST', 'GET'])
def register():
    match request.method:
        case 'POST':
            return render_template(os.path.join(sys.path[0], 'templates', 'register.html'), name='POST',
                                   title='Webpage')
        case 'GET':
            return render_template(os.path.join(sys.path[0], 'templates', 'register.html'), name='GET', title='Webpage')


def render(template_path: str, **kwargs):
    with open(template_path) as file_:
        return render_template(Template(file_.read()), **kwargs)

if __name__ == '__main__':
    app.run(debug=True)
