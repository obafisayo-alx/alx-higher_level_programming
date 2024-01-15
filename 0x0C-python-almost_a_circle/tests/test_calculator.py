#!/usr/bin/python3
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = self.calculator.multiply(2, 6)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calculator.divide(8, 2)
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)


if __name__ == '__main__':
    unittest.main()
