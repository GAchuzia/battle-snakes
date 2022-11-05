# Simplifies response creation
__author__ = "Matteo Golin & Grant Achuzia"

# Imports


# Constants

# Functions
def move_response(direction: str, shout: str = None):

    if not shout:
        shout = "null"

    return {
        "move": direction,
        "shout": shout
    }
