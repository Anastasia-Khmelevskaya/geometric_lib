import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_basic(self):
        self.assertEqual(area(3, 4), 12.0)

    def test_area_zero_height(self):
        self.assertEqual(area(10, 0), 0.0)

    def test_area_zero_width(self):
        self.assertEqual(area(0, 10), 0.0)

    def test_area_float(self):
        self.assertEqual(area(2.5, 7), 17.5)

    def test_perimeter_basic(self):
        self.assertEqual(perimeter(3, 4), 14.0)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(2.5, 7), 19.0)


if __name__ == "__main__":
    unittest.main()
