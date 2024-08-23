#!/usr/bin/python3
"""
    This module is a script that start a FLask Web app
    Route:
        /: return Hello HBNB!
        /hbnb: return HBNB
        Listening on 0.0.0.0 port 5000
"""

from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
        This Function is Trigger with / route
        and Return Hello HBNB
        No Arguments
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
        This Function is Trigger with /hbnb route
        and Return HBNB
        No Arguments
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_C(text):
    """
        This Function is Trigger with /c/<text> route
        and Return HBNB
        No Arguments
    """
    new_text = text.replace("_", " ")
    return "C {}".format(escape(new_text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
