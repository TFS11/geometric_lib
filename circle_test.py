import unittest
import math
from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5),78.53981633974483)
        self.assertEqual(perimeter(5),31.41592653589793)
        self.assertEqual(area(5000000000), 7.853981633974483e+19)
        self.assertEqual(perimeter(5000000000), 31415926535.89793)

    def test_float(self):
        self.assertEqual(area(2.5),19.634954084936208)
        self.assertEqual(perimeter(2.5), 15.707963267948966)

    def test_zero(self):
        self.assertEqual(area(0), 0.0)
        self.assertEqual(perimeter(0), 0.0)

    def test_negative_values(self):
        self.assertEqual(area(-5), 78.53981633974483)
        self.assertEqual(perimeter(-5), -31.41592653589793)

    def test_string(self):
        self.assertRaises(TypeError,area,"a")
        self.assertRaises(TypeError,perimeter,"a")
