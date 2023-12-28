import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5,10), 25)
        self.assertEqual(perimeter(10,15,5), 30)
        self.assertEqual(area(2000000000, 1000000000), 1000000000000000000)
        self.assertEqual(perimeter(2000000000, 3000000000, 1000000000), 6000000000)

    def test_float(self):
        self.assertEqual(area(2.5, 0.5), 0.625)
        self.assertEqual(perimeter(2.2, 3.4, 4.1), 9.7)

    def test_zero(self):
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_negative_values(self):
        self.assertEqual(area(-5,-2), 5)
        self.assertEqual(perimeter(-5,-5,-2), -12)

    def test_string(self):
        self.assertRaises(TypeError,area,"a","h")
        self.assertEqual(perimeter("a","b","c"), "abc")