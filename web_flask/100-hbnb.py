#!/usr/bin/python3
"""flask web-app that list states"""
from flask import Flask, render_template, Markup
from models import storage
import sys
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states_list():
    """pass the states & cities by name(display html page 6-index.html)"""
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    amenities = list(storage.all("Amenity").values())
    amenities.sort(key=lambda x: x.name)
    places = list(storage.all("Place").values())
    places.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def shutdown_SQL(exception):
    """remove sql session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
