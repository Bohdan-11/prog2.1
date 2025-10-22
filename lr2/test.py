from lr2 import find_indices
import unittest

class TestMath(unittest.TestCase):
    def test_1(self):
        result = find_indices([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_2(self):
        result = find_indices([3, 2, 4], 6)
        self.assertEqual(result, [1, 2])

    def test_3(self):
        result = find_indices([3, 3], 6)
        self.assertEqual(result,[0, 1])
    def test_4(self):
        result = find_indices([3, 3], 9)
        self.assertEqual(result,[])
    def test_5(self):
        result = find_indices([3,6,4,5], 9)
        self.assertEqual(result,[0, 1],[2,3])

unittest.main()
    
