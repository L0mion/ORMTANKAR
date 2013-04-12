import SimpleMath

from SimpleMath import *

class Status:
    EMPTY = 0
    OCCUPIED = 1
    TRAINFOOD = 2

class Special:
    NA = 0
    SPECIAL = 1

class Tile:
    def __init__(self, status, special):
        self.status = status
        self.special = special