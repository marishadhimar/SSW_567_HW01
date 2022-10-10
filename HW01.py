import unittest

def classify_triangle(a, b, c):
    if check_if_valid_triangle(a, b, c):
        triangle_type = ""
        if a == b and b == c:
            triangle_type = "Equilateral"
            return triangle_type
        elif a == b or b == c or a == c:
            triangle_type = "Isosceles"
            return triangle_type
        elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            triangle_type = "Right angle"
            return triangle_type
        else:
            triangle_type = "Scalene"
            return triangle_type
    else:
        return "The triangle is not possible with given sides"


def check_if_valid_triangle(a, b, c):
    if a + b > c and b + c > a and a + c> b:
        return True
    else:
        return False


class TestTriangle(unittest.TestCase):

    def setUp(self):
        pass

    def test_triangle(self):
        self.assertEqual(classify_triangle(3,4,5), "Right angle")
        self.assertEqual(classify_triangle(10,10,10), "Equilateral")
        self.assertEqual(classify_triangle(8,8,4), "Isosceles")
        self.assertEqual(classify_triangle(8,5,4), "Scalene")
        self.assertEqual(classify_triangle(2,7,4), "The traingle is not possible with given sides")
        self.assertNotEqual(classify_triangle(1,1,1), "The traingle is not possible with given sides")
        self.assertNotEqual(classify_triangle(2,3,5), "Right Angle")
        self.assertEqual(classify_triangle("2","3","5"), "The traingle is not possible with given sides")
        self.assertEqual(classify_triangle(10.5, 10.5, 10.5), "Equilateral")
        self.assertNotEqual(classify_triangle(-10.5, -10.5, 10.5), "Equilateral")

if __name__ == '__main__':
    unittest.main()

