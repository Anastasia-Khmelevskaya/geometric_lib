import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_345(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=6)

    def test_perimeter_345(self):
        self.assertEqual(perimeter(3, 4, 5), 12.0)


if __name__ == "__main__":
    unittest.main()
