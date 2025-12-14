"""
Unit tests untuk Calculator class
Demonstrasi testing dalam CI/CD pipeline
"""

import unittest
import sys
import os

# Menambahkan src directory ke path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases untuk Calculator class"""
    
    def setUp(self):
        """Setup yang dijalankan sebelum setiap test"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test fungsi penambahan"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test fungsi pengurangan"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
    
    def test_multiply(self):
        """Test fungsi perkalian"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
    
    def test_divide(self):
        """Test fungsi pembagian"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test fungsi pangkat"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(3, 2), 9)

if __name__ == '__main__':
    unittest.main()