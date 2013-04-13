import SimpleMath
import Tile

from SimpleMath import *
from Tile import *

class Direction:
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

class Train:
    def __init__(self, startLength, startPosArray):
        self.length = startLength
        self.body = []
        self.direction = Direction.UP
        self.alive = True
        self.inputQueue = []
        self.brainstorming = 0
        self.curMultiplier = 0
        self.mindmaps = []

        i = 0
        while i < startLength:
            self.body.append(startPosArray[i])
            i = i + 1

    def move(self, newPos, lvl, othersnake):
        #for i in range(self.length):
        #    self.body[self.length - (i + 1)] = self.body[self.length - i - 1]
        #self.body[0] = newPos

        i = self.length - 1

        leavingPortal = False
        if lvl[self.body[i].X()][self.body[i].Y()].special == Special.SPECIAL:
            for mindmap in othersnake.mindmaps:
                if mindmap.X() == self.body[i].X():
                    if mindmap.Y() == self.body[i].Y():
                        leavingPortal = True
            if leavingPortal == True:
               self.brainstorming = self.brainstorming - 1
               if self.brainstorming <= 0:
                    derp = 'SCORE'
                    self.brainstorming = 0

        for mindmap in self.mindmaps:
            if mindmap.X() == self.body[i].X():
                if mindmap.Y() == self.body[i].Y():
                    self.mindmaps.pop(self.mindmaps.index(mindmap))

        lvl[self.body[i].X()][self.body[i].Y()].status = Status.EMPTY #last bit of snake is empty

        while i > 0:
            self.body[i] = self.body[i - 1]
            i = i - 1
        self.body[0] = newPos

        lvl[self.body[0].X()][self.body[0].Y()].status = Status.OCCUPIED #new bit of snake is occupied

    def addBitsOfTrain(self):
        position = Vec2(self.body[self.length-1].X(), self.body[self.length-1].Y())
        self.body.append(position);
        self.length += 1

    def Direction(self):
        return self.direction

    def Body(self):
        return self.body

    def Alive(self):
        return self.alive

    def kill(self):
        self.alive = False

    def addMindmap(self, mindmap):
        self.mindmaps.append(mindmap)