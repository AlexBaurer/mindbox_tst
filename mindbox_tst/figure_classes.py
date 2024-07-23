from copy import copy
from math import prod, sqrt, pi


class Figure:
    pass


class FCircle(Figure):
    def __init__(self, radius: list | int):
        self.radius = radius
        if type(self.radius) == list:
            self.radius = self.radius[0]

        if self.radius <= 0:
            raise ValueError("Radius cannot be negative")

    def calc_sqr(self, measure: str) -> float:
        res = pi * (self.radius ** 2)
        print(f"Square of this circle if {res} {measure}")
        return float("%.2f" % res)


class FTriangle(Figure):
    def __init__(self, sides: list):
        self.sides = sides
        for i in sides:
            if i <= 0:
                raise ValueError("Side of triangle cannot be negative")

    def calc_sqr(self, measure: str) -> float:
        sides_no_max = copy(self.sides)
        sides_no_max.remove(max(self.sides))

        if max(self.sides) > sum(sides_no_max):
            raise ValueError("One side of triangle more than sum of two others, such triangle cannot exist.")

        if max(self.sides) ** 2 == sum(i**2 for i in sides_no_max):
            res = prod(sides_no_max) / 2
            print(f"This is right triangle and its square is {res} {measure}")
            return float("%.2f" % res)
        else:
            per = sum(self.sides) / 2
            res = sqrt(per * (per - self.sides[0]) * (per - self.sides[1]) * (per - self.sides[2]))
            print(f"Square of this triangle is {res} {measure}")
            return float("%.2f" % res)


