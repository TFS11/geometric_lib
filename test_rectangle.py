import unittest
from rectangle import area
from rectangle import perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, 6), 18)
        self.assertEqual(area(1.75, 1.75), 1.75*1.75)
        self.assertEqual(area(0, 4), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 7), 18)
        self.assertEqual(perimeter(1.75, 1.75), 7)
        self.assertEqual(perimeter(0, 6), 12)

    def test_values(self):
        self.assertRaises(ValueError, area, -2, -2)
        self.assertRaises(ValueError, perimeter, -2, -2)

    def test_Types(self):
        self.assertRaises(TypeError, area, [-2, 1], [-0, 6])
        self.assertRaises(TypeError, area, "3", "#")
        self.assertRaises(TypeError, area, 5+3j, 5+2j)
        self.assertRaises(TypeError, area, True, False)

        self.assertRaises(TypeError, perimeter, [-2, 1], [-0, 6])
        self.assertRaises(TypeError, perimeter, "3", "#")
        self.assertRaises(TypeError, perimeter, 5+3j, 5+2j)
        self.assertRaises(TypeError, perimeter, True, False)