# BattleSnakes competition November 5th 2022
__author__ = "Matteo Golin & Grant Achuzia"

# Imports
import flask
from flask import Flask, request
import json

from response import move_response
from move import *

# Constants
app = Flask(__name__)
NAME = "SSSSSYSC2006"
COLOUR = "#55FF00"


# Unpack helper function

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
    print("Game has started.")
    return "Start"


@app.route("/move", methods=["POST"])
def move():

    # Assume all moves are safe
    move_safe = {
        "left": True,
        "right": True,
        "up": True,
        "down": True
    }

    # Check valid moves
    handle_backwards(request.json, move_safe)


    # Take the safest move
    if any(move_safe.values()):  # There are some moves

        valid_moves = []
        for direction, valid in move_safe.items():
            if valid:
                valid_moves.append(direction)

        if len(valid_moves) == 1:
            return move_response(valid_moves[0])
        else:  # More than 1 move
            pass

    # No moves
    else:
        print("Noooo we died!")
        return move_response("up", "I died with honour.")

    return "Move"


@app.route("/end", methods=["POST"])
def end():
    print("Game has ended.")
    return "End"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
