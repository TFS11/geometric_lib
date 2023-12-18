import unittest
from circle import area
from circle import perimeter
from math import pi


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3), pi*9)
        self.assertEqual(area(5), pi*25)
        self.assertEqual(area(1.75), pi*1.75*1.75)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(3), pi*6)
        self.assertEqual(perimeter(5), pi*10)
        self.assertEqual(perimeter(1.75), pi*3.5)
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
        self.assertRaises(TypeError, perimeter, "3")
        self.assertRaises(TypeError, perimeter, 5+3j)
        self.assertRaises(TypeError, perimeter, True)