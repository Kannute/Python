
from math import sqrt
class Wektor:

    def __init__(self, x = 0, y = 0, z = 0):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, wektor):
        x = self._x + wektor._x
        y = self._y + wektor._y
        z = self._z + wektor._z
        return Wektor(x,y,z)

    __radd__=__add__

    def __sub__(self, wektor):
        x = self._x - wektor._x
        y = self._y - wektor._y
        z = self._z - wektor._z
        return Wektor(x,y,z)

        
    def __mul__(self, num):
        self._x *= num
        self._y *= num
        self._z *= num
        return self
    __rmul__ = __mul__

    def len(self):
        return int(sqrt(self._x**2 + self._y**2 + self._z**2 ))

    def __str__(self):
         return f'x:{self._x}, y={self._y}, z={self._z}'

    def skalarny(self, wektor):
        return self._x * wektor._x + self._y*wektor._y + self._z*wektor._z

    def wektorowy(self, wektor):
        return Wektor( (self._y * wektor._z - self._z*wektor._y) , (self._x * wektor._z - self._z*wektor._x) , (self._x * wektor._y - self._y*wektor._x) )

    def mieszany(self, wektor1, wektor2):
        return self.skalarny(wektor2.wektorowy(wektor1))
