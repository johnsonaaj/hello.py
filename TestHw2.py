class TestCard(unittest.TestCase):

def test_init():
c1 = Card(2, "green", "striped", "diamond")
>>> c1.number
2
"""Tests that we can initialize cards w/ number/color/shading/shape"""

def test_str():
"""test that we can get a good string representation of Card instances"""

def test_eq(self):
"""Tests that two cards are equal iff all attributes are equal"""