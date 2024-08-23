#!/usr/bin/python3
"""
    This module is a script that start a FLask Web app
    Route:
        /: return Hello HBNB!
        Listening on 0.0.0.0 port 5000
"""


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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
