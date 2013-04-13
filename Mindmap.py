import SimpleMath

from SimpleMath import *

class Mindmap:
    def __init__(self, pos, lifetime):
        self.pos = pos
        self.timeLeft = lifetime

    def Pos(self):
        return self.pos
    def TimeLeft(self):
        return self.timeLeft