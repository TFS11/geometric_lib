import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5),25)
        self.assertEqual(perimeter(5),20)
        self.assertEqual(area(5000000000), 25000000000000000000)
        self.assertEqual(perimeter(5000000000), 20000000000)

    def test_float(self):
        self.assertEqual(area(2.5),2.5*2.5)
        self.assertEqual(perimeter(2.5), 10)

    def test_zero(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative_values(self):
        self.assertEqual(area(-5), 25)
        self.assertEqual(perimeter(-5), -20)

    def test_string(self):
        self.assertRaises(TypeError,area,"a")
        self.assertEqual(perimeter("a"), "aaaa")