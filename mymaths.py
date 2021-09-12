
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tuple(self):
        return (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x + other, self.y + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x - other, self.y - other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x / other, self.y / other)
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x // other.x, self.y // other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x // other, self.y // other)
        else:
            return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x % other.x, self.y % other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x % other, self.y % other)
        else:
            return NotImplemented

    def tile_shift(self):
        return Vector2(self.x, self.y + (self.x % 2) * 0.5)

    def __eq__(self, other):
        return self.tuple() == other.tuple()

    def round(self):
        return Vector2(round(self.x), round(self.y))

    def int(self):
        return Vector2(int(self.x), int(self.y))

    def __iter__(self):
        return self.tuple().__iter__()

    def map(self, f):
        return Vector2(f(self.x), f(self.y))

    def __hash__(self):
        return hash(self.tuple())

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __imul__(self, other):
        self = self * other
        return self

    def __itruediv__(self, other):
        self = self / other
        return self

    def __ifloordiv__(self, other):
        self = self // other
        return self

    def __str__(self):
        sx, sy = str(self.x), str(self.y)
        sx = sx[:sx.find('.') + 3]
        sy = sy[:sy.find('.') + 3]
        return f'({sx};{sy})'

    def __repr__(self):
        return f'Vector2({self.x}, {self.y})'

    def __getitem__(self, key):
        return self.tuple()[key]

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def length(self):
        from math import sqrt
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def unit(self):
        return self / self.length()
