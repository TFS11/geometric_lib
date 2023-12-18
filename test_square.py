import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3), 9)
        self.assertEqual(area(1.75), 1.75*1.75)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(1.75), 7)
        self.assertEqual(perimeter(0), 0)

    def test_values(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, perimeter, -2)

    def test_Types(self):
        self.assertRaises(TypeError, area, [-2, 1])
        self.assertRaises(TypeError, area, "3")
        self.assertRaises(TypeError, area, 5+3j)
        self.assertRaises(TypeError, area, True)

        self.assertRaises(TypeError, perimeter, [-2, 1])
        self.assertRaises(TypeError, perimeter, "3",)
        self.assertRaises(TypeError, perimeter, 5+3j)
        self.assertRaises(TypeError, perimeter, True)