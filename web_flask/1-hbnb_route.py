#!/usr/bin/python3
"""start a flask web-app display hbnbn in /hbnb"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Greeting():
    """return a Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_HBNB():
    """Display HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
