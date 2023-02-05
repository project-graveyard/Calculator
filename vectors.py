__doc__ = "Implementation of vector calculations"


class Make2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Make2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Make2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Make2D(self.x * other.x, self.y * other.y)


def dot_product(vect1, vect2):
    first_vector = Make2D(vect1[0], vect1[1])
    second_vector = Make2D(vect2[0], vect2[1])
    result_vector = first_vector * second_vector
    return round(result_vector.x + result_vector.y, 4)


def magnitude(vector):
    return round(((vector[0] ** 2) + (vector[1] ** 2)) ** 0.5, 4)
