class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.a * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"