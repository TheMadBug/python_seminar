from dataclasses import dataclass
from math import sqrt

from lazy import lazy
from typing_extensions import Self


@dataclass(frozen=True)
class Point:
    """
    A point in 2dimensional Euclidian space
    """
    x: int
    y: int

    @lazy
    def distance_from_origin(self) -> float:
        return sqrt(self.x*self.x + self.y*self.y)

    # inbuilt class stuff overloading below
    def __add__(self, other) -> Self:
        # point_c = point_a + point_b
        return Point(x=self.x + other.x, y=self.y + other.y)

    def __neg__(self) -> Self:
        # counter point across diagonal axis
        return self.__class__(x=-self.x, y=-self.y)

    def __sub__(self, other) -> Self:
        # point_c = point_a - point_b
        return self + -other

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        # if point_a:
        return bool(self.x or self.y)

    def __lt__(self, other):
        # if point_a < point_b
        return self.distance_from_origin < other.distance_from_origin


# run script here
one_one = Point(x=1, y=1)
big_y = Point(x=2, y=6)
whats_this = big_y - one_one
print(big_y)
origin = Point(x=0, y=0)

if origin:
    print("!??? Origin should be false")
if one_one:
    print("One one should be true")


@dataclass(frozen=True)
class Rectangle:
    bottom_left: Point
    width: int
    height: int

    def __contains__(self, item):
        if isinstance(item, Point):
            return self.bottom_left.x <= item.x <= self.bottom_left.x + self.width and \
                self.bottom_left.y <= item.y <= self.bottom_left.y + self.width


ten_to_twenty = Rectangle(Point(10, 10), 10, 10)
fifteen = Point(15, 15)

if fifteen in ten_to_twenty:
    print("Maths works")

if one_one in ten_to_twenty:
    print("???? What? Maths doesn't work?")