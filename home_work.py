class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            return Rectangle(self.width, new_square // self.width)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            new_square = self.get_square() * n
            return Rectangle(self.width, new_square // self.width)
        return NotImplemented

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

