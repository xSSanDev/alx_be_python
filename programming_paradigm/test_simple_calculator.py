import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        test_a = 10
        test_b = 5
        self.assertEqual(SimpleCalculator().add(test_a, test_b), 15, "Should be 15")

    def test_subtract(self):
        test_a = 10
        test_b = 5
        self.assertEqual(SimpleCalculator().subtract(test_a, test_b), 5, "Should be 5")

    def test_multiply(self):
        test_a = 10
        test_b = 5
        self.assertEqual(SimpleCalculator().multiply(test_a, test_b), 50, "Should be 50")

    def test_divide(self):
        test_a = 10
        test_b = 5
        self.assertEqual(SimpleCalculator().divide(test_a, test_b), 2, "Should be 2")

    def test_divide_by_zero(self):
        test_a = 10
        test_b = 0
        self.assertIsNone(SimpleCalculator().divide(test_a, test_b), "Should be None when dividing by zero")

if __name__ == "__main__":
    unittest.main()