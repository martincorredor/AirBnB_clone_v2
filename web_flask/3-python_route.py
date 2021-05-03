#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!
/hbnb: display “HBNB”
/c/<text>: display “C/text”
/python/(<text>): display python/text - The default value of text is “is cool”
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB!" (text) """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "Hello HBNB!" (text) """
    return "Hello HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Display text """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
