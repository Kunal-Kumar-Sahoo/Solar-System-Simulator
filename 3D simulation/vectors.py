import math

class Vector:
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0
    ) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y}, {self.z})'
    
    def __str__(self) -> str:
        return f'{self.x}i + {self.y}j + {self.z}k'

    def __getitem__(self, item) -> float:
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError('There are only 3 elements in the vector')

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            '''
            Dot product
            '''
            return Vector(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z
            )

        elif isinstance(other, (int, float)):
            '''
            Scalar product
            '''
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other
            )

        else:
            raise TypeError("Operand must be Vector, int of float")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            try:
                return Vector(
                    self.x / other,
                    self.y / other,
                    self.z / other
                )
            except ZeroDivisionError as e:
                print(e)
            
        else:
            raise TypeError("Operand must be int or float")

    def get_magnitude(self) -> float:
        return math.sqrt(
            self.x ** 2 + self.y ** 2 + self.z ** 2
        )

    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude
        )

