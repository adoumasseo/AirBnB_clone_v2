#!/usr/bin/python3
"""
    This module is a script that start a FLask Web app
    Route:
        /: return Hello HBNB!
        /hbnb: return HBNB
        Listening on 0.0.0.0 port 5000
"""


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
        This Function is Trigger with / route
        and Return Hello HBNB
        No Arguments
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """
        This Function is Trigger with / route
        and Return Hello HBNB
        No Arguments
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
