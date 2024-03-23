#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ script that starts a Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """script that starts a Flask web application"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """script that starts a Flask web application"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """script that starts a Flask web application"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """script that starts a Flask web application"""
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
