#!/usr/bin/python3
"""flask web-app that list states"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_list():
    """list all the states by name(display html page 6-index.html)"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def shutdown_SQL(exception):
    """remove sql session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
