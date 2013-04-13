class Vec2:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def X(self):
        return self.x
    def Y(self):
        return self.y

    def asPython(self):
        return (self.x, self.y)