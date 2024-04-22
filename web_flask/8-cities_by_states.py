#!/usr/bin/python3
"""flask web-app that list states"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_SQL(exception):
    """remove sql session after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """list all the states by name"""
    states = list(storage.all("State").values())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
