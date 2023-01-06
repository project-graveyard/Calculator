__doc__ = "Implementation of vector calculations"


class Add2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Add2D(self.x + other.x, self.y + other.y)


class Sub2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Sub2D(self.x - other.x, self.y - other.y)