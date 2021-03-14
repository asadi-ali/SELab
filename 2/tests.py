import unittest

from .rectangle import Rectangle


class RectangleUnitTest(unittest.TestCase):
    def test_rectangle_area(self):
        rectangle: Rectangle = Rectangle(height=3, width=2)
        self.assertEqual(rectangle.compute_area(), 6)

    def test_rectangle_set_height(self):
        rectangle: Rectangle = Rectangle(height=3, width=2)
        rectangle.set_height(5)
        self.assertEqual(rectangle.get_height(), 5)
