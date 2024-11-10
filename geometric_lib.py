import math

class CircleUtils:
    def area(r):
        return math.pi * r**2
    
    def perimeter(r):
        return 2 * math.pi * r

class TriangleUtils:
    def area(a, h):
        return a * h / 2
    
    def perimeter(a, b, c):
        return a + b + c
    
    def valid(a, b, c):
        if (a + b < c) or (a + c < b) or (b + c < a):
            return False
        return True
    
class RectangleUtils:
    def area(a, b):
        return a * b
    
    def perimter(a, b):
        return 2 * (a + b)
