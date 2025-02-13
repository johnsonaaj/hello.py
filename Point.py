class Point:
    def __init__(self, x, y):
        """Initializes a point with x and y coordinates."""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Sees if two points are equal to each other."""
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Sees which point has a lesser distance from the origin."""
        return self.dist_from_origin() < other.dist_from_origin()

    def __gt__(self, other):
        """Sees which point has a greater distance from the origin."""
        return self.dist_from_origin() > other.dist_from_origin()

    def __str__(self):
        """Formats point into a string."""
        return f"Point({self.x}, {self.y})"

    def dist_from_origin(self):
        """Finds distance from the origin."""
        return (self.x**2 + self.y**2) ** 0.5
