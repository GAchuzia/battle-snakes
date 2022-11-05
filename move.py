# Moving logic for the snake
__author__ = "Matteo Golin & Grant Achuzia"

# Imports

# Constants
SURROUNDING_CELLS = {
    "up": [0, 1],
    "down": [0, -1],  # Down
    "right": [1, 0],  # Right
    "left": [-1, 0]  # Left
}

# Functions


def handle_backwards(state: dict, move_safe: dict) -> None:

    my_head = state["you"]["body"][0]
    my_neck = state["you"]["body"][1]

    if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
        move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
        move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
        move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
        move_safe["up"] = False


def handle_bounds(state: dict, move_safe: dict) -> None:

    width = state["board"]["width"]
    height = state["board"]["height"]

    head_loc = state["you"]["body"][0]

    for direction, vector in SURROUNDING_CELLS.items():
        possible_cell = head_loc["x"] + vector[0], head_loc["y"] + vector[1]

        if not (0 <= possible_cell[0] < width):
            move_safe[direction] = False

        if not (0 <= possible_cell[1] < height):
            move_safe[direction] = False

