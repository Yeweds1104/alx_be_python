import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        result = SimpleCalculator.add(10, 5)
        self.assertEqual(result, 15)
    def test_subtract(self):
        result = SimpleCalculator.subtract(10, 5)
        self.assertEqual(result, 5)
    def test_multiply(self):
        result = SimpleCalculator.multiply(10, 5)
        self.assertEqual(result, 50)
    def test_divide(self):
        result = SimpleCalculator.divide(10, 5)
        self.assertEqual(result, 2.0)
        self.assertRaises(ValueError, SimpleCalculator.divide, 10, 0)
        
if __name__ == "__main__":
    unittest.main()