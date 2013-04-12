import SimpleMath

from SimpleMath import *

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

        i = 0
        while i < startLength:
            self.body.append(startPosArray[i])
            i = i + 1

    def move(self, newPos):
        #for i in range(self.length):
        #    self.body[self.length - (i + 1)] = self.body[self.length - i - 1]
        #self.body[0] = newPos

        i = self.length - 1
        while i > 0:
            self.body[i] = self.body[i - 1]
            i = i - 1
        self.body[0] = newPos

    def addBitsOfTrain(self):
        position = Vec2(self.body[self.length-1].X(), self.body[self.length-1].Y())
        self.body.append(position);
        self.length += 1

    def Direction(self):
        return self.direction

    def Body(self):
        return self.body