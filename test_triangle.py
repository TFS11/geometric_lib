import unittest
from triangle import area
from triangle import perimeter



class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, 6), 9)
        self.assertEqual(area(1.75, 1.75), 1.75*1.75/2)
        self.assertEqual(area(0, 4), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 7, 3), 12)
        self.assertEqual(perimeter(1.75, 1.75, 1), 4.5)
        self.assertEqual(perimeter(0, 6, 1), 7)

    def test_values(self):
        self.assertRaises(ValueError, area, -2, -2)
        self.assertRaises(ValueError, perimeter, -2, -2, -1)

    def test_Types(self):
        self.assertRaises(TypeError, area, [-2, 1], [-0, 6])
        self.assertRaises(TypeError, area, "3", "#")
        self.assertRaises(TypeError, area, 5+3j, 5+2j)
        self.assertRaises(TypeError, area, True, False)

        self.assertRaises(TypeError, perimeter, [-2, 1], [-0, 6], 1)
        self.assertRaises(TypeError, perimeter, "3", "#", 1)
        self.assertRaises(TypeError, perimeter, 5+3j, 5+2j, 1)
        self.assertRaises(TypeError, perimeter, True, False, 1)