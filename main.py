# BattleSnakes competition November 5th 2022
__author__ = "Matteo Golin & Grant Achuzia"

# Imports
from flask import Flask, request
import json

# Constants
app = Flask(__name__)
NAME = "SSSSSYSC2006"
COLOUR = "#55FF00"


# Main API
@app.route("/", methods=["GET"])
def get():
    return {
        "apiversion": "1",
        "author": NAME,
        "color": COLOUR,
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


@app.route("/start", methods=["POST"])
def start():
    return "Start"


@app.route("/move", methods=["POST"])
def move():
    return "Move"


@app.route("/end", methods=["POST"])
def end():
    return "End"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
