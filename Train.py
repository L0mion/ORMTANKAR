import SimpleMath

from SimpleMath import *

class Train:
    def __init__(self, startLength, startPosArray):
        self.length = startLength
        self.body = []

        i = 0
        while i < startLength:
            self.body.append(startPosArray[i])
            i = i + 1