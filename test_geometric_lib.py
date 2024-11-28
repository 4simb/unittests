import unittest
import math
from geometric_lib import CircleUtils, TriangleUtils, RectangleUtils

class GeometricTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(RectangleUtils.area(0, 0), 0)
        self.assertEqual(RectangleUtils.area(999, 0), 0)
        self.assertEqual(RectangleUtils.area(14, 3), 42)
        self.assertEqual(RectangleUtils.area(-123, 23), -1)
        self.assertAlmostEqual(RectangleUtils.area(12.5, 4.99), 62.375)
        self.assertAlmostEqual(RectangleUtils.area(324.33, 0.324), 105.08292)
        
    def test_rectangle_perimeter(self):
        self.assertEqual(RectangleUtils.perimter(0, 0), 0)
        self.assertEqual(RectangleUtils.perimter(10, 1), 22)
        self.assertEqual(RectangleUtils.perimter(-10, 1), -1)
        self.assertEqual(RectangleUtils.perimter(1.0, 10), 22)
        self.assertEqual(RectangleUtils.perimter(1001, 1001), 4004)
        self.assertAlmostEqual(RectangleUtils.perimter(12.4, 53.12), 131.04)
        
    def test_circle_area(self):
        self.assertEqual(CircleUtils.area(0), 0)
        self.assertEqual(CircleUtils.area(-13), -1)
        self.assertAlmostEqual(CircleUtils.area(1), math.pi)
        self.assertAlmostEqual(CircleUtils.area(10 / math.pi), 31.8309886)
        self.assertAlmostEqual(CircleUtils.area(4 / math.pi**0.5), 16)
        
    def test_circle_perimeter(self):
        self.assertEqual(CircleUtils.perimeter(0), 0)
        self.assertEqual(CircleUtils.perimeter(-543), -1)
        self.assertAlmostEqual(CircleUtils.perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(CircleUtils.perimeter(13 / math.pi), 26)
        self.assertAlmostEqual(CircleUtils.perimeter(3), 18.8495559)
        
    def test_triangle_area(self):
        self.assertEqual(TriangleUtils.area(44, -123), -1)
        self.assertEqual(TriangleUtils.area(10, 5), 25)
        self.assertEqual(TriangleUtils.area(0, 10), 0)
        self.assertEqual(TriangleUtils.area(13, 0), 0)
        self.assertEqual(TriangleUtils.area(100, 100), 5000)
    
    def test_triangle_perimeter(self):
        self.assertEqual(TriangleUtils.perimeter(0, 0, 0), 0)
        self.assertEqual(TriangleUtils.perimeter(4, 5, 6), 15)
        self.assertEqual(TriangleUtils.perimeter(1.2, 2.3, 3.4), 6.9)
        self.assertEqual(TriangleUtils.perimeter(1, 4, -2), -1)
        self.assertEqual(TriangleUtils.perimeter(1000, 2000, 3000), 6000)
        
    def test_triangle_valid(self):
        self.assertTrue(TriangleUtils.valid(4, 4, 4))
        self.assertTrue(TriangleUtils.valid(20, 20, 10))
        self.assertFalse(TriangleUtils.valid(1, 1, 3))
        self.assertFalse(TriangleUtils.valid(43, 27, 71))
        self.assertFalse(TriangleUtils.valid(-12, 42, 1))
        
        