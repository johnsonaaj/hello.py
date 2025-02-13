class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
""" Sees if two points are equal to eachother"""
    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()
"""Sees which point has a lesser distance from orgin"""
    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()
"""See which point has a greater distance from orgin"""
    def __str__(self):
        return f"({self.x}, {self.y})"
"""Formats point into a string"""
    def dist_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5
"""Finds distance from orgin"""
