from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest, TestCase):
    def testClockwise(self):
        title_L = [2,3,1,0,5]
        self.assertTrue(puzzle(title_L))
    def testCounterClockwise(self):
        title_list = [1,2,3,4,0]
        self.assertTrue(puzzle(title_L))
    def testMixed(self):
        title_L =[2,3,2,1,4]
        self.assertTrue(puzzle(title_L))
    def testUnsolvable(self):
        title_L =[3,3,3,3,3]
        self.assertFalse(puzzle(title_L))
if __name__ == '__main__':
    unittest.main()