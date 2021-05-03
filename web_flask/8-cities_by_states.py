#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
remove the current SQLAlchemy Session
Routes:
/: display “Hello HBNB!
/hbnb: display “HBNB”
/c/<text>: display “C/text”
/python/(<text>): display python/text - The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
/states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: list of all State objects in DBStorage sorted by name
     LI tag: description of one State: <state.id>: <B><state.name></B>+ UL tag
      LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask, render_template
from models import storage
from models import *
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


@app.route('/number/<int:n>', strict_slashes=False)
def if_number(n):
    """ Display a HTML page only if n is an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display - n is a number - only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display - n is a number - only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.teardown_appcontext
def teardown(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a HTML page: (inside the tag BODY) """
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a HTML page: (inside the tag BODY) """
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
