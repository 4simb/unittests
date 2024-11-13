import math

class CircleUtils:
    def area(r):
        if(r < 0):
            return -1
        return math.pi * r**2
    
    def perimeter(r):
        if(r < 0):
            return -1
        return 2 * math.pi * r

class TriangleUtils:
    def area(a, h):
        if(a < 0 or h < 0):
            return -1
        return a * h / 2
    
    def perimeter(a, b, c):
        if(a < 0 or b < 0 or c < 0):
            return -1
        return a + b + c
    
    def valid(a, b, c):
        if(a < 0 or b < 0 or c < 0):
            return False
        if (a + b < c) or (a + c < b) or (b + c < a):
            return False
        return True
    
class RectangleUtils:
    def area(a, b):
        if(a < 0 or b < 0):
            return -1
        return a * b
    
    def perimter(a, b):
        if(a < 0 or b < 0):
            return -1
        return 2 * (a + b)
