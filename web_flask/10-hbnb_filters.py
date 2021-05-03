#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
remove the current SQLAlchemy Session
Routes:
/hbnb_filters: display a HTML page like 6-index.html
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a HTML page: (inside the tag BODY) """
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Display a HTML page: (inside the tag BODY) """
    all_states = None
    for state in storage.all(State).values():
        if state.id == id:
            all_states = state
    return render_template('9-states.html', all_states=all_states)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ display a HTML page like 6-index.html """
    all_states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', all_states=all_states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
