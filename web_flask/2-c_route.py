#!/usr/bin/python3
"""start a flask web-app display c is fun"""
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


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """Display C is fun"""
    return "C " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
