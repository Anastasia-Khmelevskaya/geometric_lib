import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_basic(self):
        self.assertEqual(area(5), 25)

    def test_area_float(self):
        self.assertEqual(area(2.5), 6.25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_basic(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(2.5), 10.0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)


if __name__ == "__main__":
    unittest.main()
