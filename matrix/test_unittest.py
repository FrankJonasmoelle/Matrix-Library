import unittest

from matrix import *

class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.m1 = Matrix([[1,2,3],[4,5,6]])
        self.m2 =  Matrix([[1,1,1],[1,1,1]])
        self.m3 = Matrix([[1,2],[3,4],[5,6]])

    def test_add(self):
        out = self.m1 + self.m2
        expected = Matrix([[2,3,4], [5,6,7]])
        self.assertEqual(out, expected)

if __name__ == "__main__":
    unittest.main()
