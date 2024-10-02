import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize a SimpleCalculator instance before each test
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Test the addition method
        test_a = 10
        test_b = 5
        # Assert that the addition of test_a and test_b equals 15
        self.assertEqual(self.calc.add(test_a, test_b), 15, "Should be 15")

    def test_subtraction(self):
        # Test the subtraction method
        test_a = 10
        test_b = 5
        # Assert that the subtraction of test_b from test_a equals 5
        self.assertEqual(self.calc.subtract(test_a, test_b), 5, "Should be 5")

    def test_multiplication(self):
        # Test the multiplication method
        test_a = 10
        test_b = 5
        # Assert that the multiplication of test_a and test_b equals 50
        self.assertEqual(self.calc.multiply(test_a, test_b), 50, "Should be 50")

    def test_division(self):
        # Test the division method
        test_a = 10
        test_b = 5
        # Assert that the division of test_a by test_b equals 2
        self.assertEqual(self.calc.divide(test_a, test_b), 2, "Should be 2")

    def test_divide_by_zero(self):
        # Test the division method when dividing by zero
        test_a = 10
        test_b = 0
        # Assert that dividing by zero returns None
        self.assertIsNone(self.calc.divide(test_a, test_b), "Should be None when dividing by zero")

if __name__ == "__main__":
    # Run the tests
    unittest.main()