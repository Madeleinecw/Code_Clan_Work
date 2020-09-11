import unittest
from src.calculator import cd ..

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, add(2,3))

    def test_subtract(self):
        self.assertEqual(2, subtract(5,3))

    def test_multiply(self):
        self.assertEqual(4, multiply(2,2))

    def test_divide(self):
        self.assertEqual(3, divide(6,2))

    