from enum import Enum

class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

class Globals:
    master = None
    display = None