import unittest
import math
from geometric_lib import CircleUtils, TriangleUtils, RectangleUtils

class GeometricTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(RectangleUtils.area(0, 0), 0)
        self.assertEqual(RectangleUtils.area(999, 0), 0)
        self.assertEqual(RectangleUtils.area(1, 1), 1)
        self.assertEqual(RectangleUtils.area(12, 4), 48)
        
    def test_rectangle_perimeter(self):
        self.assertEqual(RectangleUtils.perimter(0, 0), 0)
        self.assertEqual(RectangleUtils.perimter(10, 1), 22)
        self.assertEqual(RectangleUtils.perimter(1, 10), 22)
        self.assertEqual(RectangleUtils.perimter(1001, 1001), 4004)
        
    def test_circle_area(self):
        self.assertAlmostEqual(CircleUtils.area(0), 0)
        self.assertAlmostEqual(CircleUtils.area(10 / math.pi), 31.830988618379074)
        self.assertAlmostEqual(CircleUtils.area(4 / math.pi**0.5), 16)
        
    def test_circle_perimeter(self):
        self.assertAlmostEqual(CircleUtils.perimeter(0), 0)
        self.assertAlmostEqual(CircleUtils.perimeter(13 / math.pi), 26)
        self.assertAlmostEqual(CircleUtils.perimeter(3), 18.84955592153876)
        
    def test_triangle_area(self):
        self.assertEqual(TriangleUtils.area(10, 5), 25)
        self.assertEqual(TriangleUtils.area(0, 10), 0)
        self.assertEqual(TriangleUtils.area(13, 0), 0)
        self.assertEqual(TriangleUtils.area(100, 100), 5000)
    
    def test_triangle_perimeter(self):
        self.assertEqual(TriangleUtils.perimeter(0, 0, 0), 0)
        self.assertEqual(TriangleUtils.perimeter(4, 5, 6), 15)
        self.assertEqual(TriangleUtils.perimeter(1000, 2000, 3000), 6000)
        
    def test_triangle_valid(self):
        self.assertTrue(TriangleUtils.valid(4, 4, 4))
        self.assertTrue(TriangleUtils.valid(20, 20, 10))
        self.assertFalse(TriangleUtils.valid(1, 1, 3))
        self.assertFalse(TriangleUtils.valid(43, 27, 71))