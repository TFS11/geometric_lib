import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):

    def test_int(self):
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(area(2000000000, 1000000000), 2000000000000000000)
        self.assertEqual(perimeter(2000000000, 1000000000), 6000000000)


    def test_float(self):
        self.assertEqual(area(1.01, 1.03), 1.01*1.03)
        self.assertEqual(perimeter(1.30, 1.20), 5)

    def test_zero(self):
        self.assertEqual(area(0, 4), 0)
        self.assertEqual(perimeter(0, 0), 0)

    def test_sqare(self):
        self.assertEqual(area(5, 5), 25)
        self.assertEqual(perimeter(5, 5), 20)

    def test_negative_values(self):
        self.assertEqual(area(-5,-2),-5*-2)
        self.assertEqual(perimeter(-5,-2),-14)

    def test_string(self):
    #     self.assertRaises(TypeError, area, [-2, 1], [-0, 6])
        self.assertRaises(TypeError, area, "3", "#")
        self.assertEqual(perimeter("a", "z"), "azaz")