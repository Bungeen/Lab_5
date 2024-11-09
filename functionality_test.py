import unittest

import math

import hexagon
import rectangle
import square
import triangle
import circle

class SquareTestCase(unittest.TestCase):
    def test_square_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    
    def test_square_normal_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)
    
    def test_square_negative_area(self):
        res = square.area(-2)
        self.assertEqual(res, 0)
    


    def test_square_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_square_normal_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)
    
    def test_square_negative_perimeter(self):
        res = square.perimeter(-2)
        self.assertEqual(res, 0)
    

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_zero_area(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)
    
    def test_rectangle_normal_area(self):
        res = rectangle.area(10, 20)
        self.assertEqual(res, 200)
    
    def test_rectangle_negative_area(self):
        res = rectangle.area(-2, 8)
        self.assertEqual(res, 0)
    


    def test_rectangle_zero_perimeter_first(self):
        res = rectangle.perimeter(0, 10)
        self.assertEqual(res, 0)

    def test_rectangle_zero_perimeter_second(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_normal_perimeter(self):
        res = rectangle.perimeter(10, 20)
        self.assertEqual(res, 60)
    
    def test_rectangle_negative_perimeter(self):
        res = rectangle.perimeter(-2, 8)
        self.assertEqual(res, 0)


class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)
    
    def test_triangle_normal_area(self):
        res = triangle.area(10, 20)
        self.assertEqual(res, 100)
    
    def test_triangle_negative_area(self):
        res = triangle.area(-2, 8)
        self.assertEqual(res, 0)
    


    def test_triangle_zero_perimeter_first(self):
        res = triangle.perimeter(0, 10, 20)
        self.assertEqual(res, 0)

    def test_triangle_zero_perimeter_second(self):
        res = triangle.perimeter(10, 0, 20)
        self.assertEqual(res, 0)

    def test_triangle_normal_perimeter(self):
        res = triangle.perimeter(10, 20, 30)
        self.assertEqual(res, 60)
    
    def test_triangle_negative_perimeter(self):
        res = triangle.perimeter(-2, 8, 7)
        self.assertEqual(res, 0)


class CircleTestCase(unittest.TestCase):
    def test_circle_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_circle_normal_area(self):
        res = circle.area(10)
        self.assertEqual(res, 100 * math.pi)
    
    def test_circle_negative_area(self):
        res = circle.area(-2)
        self.assertEqual(res, 0)
    


    def test_circle_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_circle_normal_perimeter(self):
        res = circle.perimeter(10)
        self.assertEqual(res, 20 * math.pi)
    
    def test_circle_negative_perimeter(self):
        res = circle.perimeter(-2)
        self.assertEqual(res, 0)



class HexagonTestCase(unittest.TestCase):
    def test_hexagon_zero_area(self):
        res = hexagon.area(0)
        self.assertEqual(res, 0)
    
    def test_hexagon_normal_area(self):
        res = hexagon.area(10)
        self.assertEqual(res, ((3 ** 0.5 * 3) / 2) * 100)
    
    def test_hexagon_negative_area(self):
        res = hexagon.area(-2)
        self.assertEqual(res, 0)
    


    def test_hexagon_zero_perimeter(self):
        res = hexagon.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_hexagon_normal_perimeter(self):
        res = hexagon.perimeter(10)
        self.assertEqual(res, 60)
    
    def test_hexagon_negative_perimeter(self):
        res = hexagon.perimeter(-2)
        self.assertEqual(res, 0)
    


    def test_hexagon_zero_mainDiagonal(self):
        res = hexagon.mainDiagonal(0)
        self.assertEqual(res, 0)
    
    def test_hexagon_normal_mainDiagonal(self):
        res = hexagon.mainDiagonal(10)
        self.assertEqual(res, 20)
    
    def test_hexagon_negative_mainDiagonal(self):
        res = hexagon.mainDiagonal(-2)
        self.assertEqual(res, 0)
    


    def test_hexagon_zero_subDiagonal(self):
        res = hexagon.subDiagonal(0)
        self.assertEqual(res, 0)
    
    def test_hexagon_normal_subDiagonal(self):
        res = hexagon.subDiagonal(10)
        self.assertEqual(res, 10 * 3 ** 0.5)
    
    def test_hexagon_negative_subDiagonal(self):
        res = hexagon.subDiagonal(-2)
        self.assertEqual(res, 0)