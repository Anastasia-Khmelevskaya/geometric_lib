import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_r1(self):
        self.assertAlmostEqual(area(1), math.pi, places=6)

    def test_area_r3(self):
        self.assertAlmostEqual(area(3), math.pi * 9, places=6)

    def test_area_zero(self):
        self.assertEqual(area(0), 0.0)

    def test_perimeter_r1(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=6)

    def test_perimeter_r3(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3, places=6)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0.0)


if __name__ == "__main__":
    unittest.main()
