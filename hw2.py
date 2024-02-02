class TestCard(unittest.TestCase):

  def test_init():
   c1 = Card(1, "green", "empty", "diamond")
   >>> c1.number
   1

   c2= Card(3, "oval", "purple", "solid")
   >>> c2.number 
   3

   c3= Card(2, "squiggle", "blue", "striped")
    >>> c3.number 
    2

"""Tests that we can initialize cards w/ number/color/shading/shape"""


   def test_str():

    >>> str(c1)
    Card(1, green, empty, diamond)

    >>> str(c2)
    Card(3, oval, purple, solid)

    >>> str(c3)
    Card(2, squiggle, blue, striped)

"""test that we can get a good string representation of Card instances"""

  def test_eq(self):
"""Tests that two cards are equal iff all attributes are equal"""