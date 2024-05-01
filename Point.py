class Point:
       def __init__(self, x, y):
             self.x = x
             self.y = y
       def __eq__(self, other):
              if self.x == other.x and self.y== other.y:
                    return True
              else:
                    return False
       def equidistant(self, other):
              if ((self.x**2 + self.y**2)**1/2) == ((other.x**2+ other.y**2)**1/2):
                    return True
              else:
                     return False
       def within(self, distance, other):
              if ((((other.x - self.x)**2) + ((other.y - self.y)**2))**(1/2)) <= distance:
                    return True
              else:
                    return False 
 