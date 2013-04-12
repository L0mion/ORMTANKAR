import SimpleMath

from SimpleMath import *

class Status:
    EMPTY = 0
    TRAIN1 = 1
    TRAIN2 = 2
    TRAINFOOD = 3

class Special:
    NA = 0
    THOUGHT = 1

class Tile:
    def __init__(self, status, special):
        self.status = status
        self.special = special