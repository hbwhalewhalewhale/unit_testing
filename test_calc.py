import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):         
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(7, 99), 106)
        self.assertEqual(calc.add(0, 0), 0)
    
    def test_subtract(self):         
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertEqual(calc.subtract(7, 99), -92)
        self.assertEqual(calc.subtract(0, 0), 0)

    def test_multiply(self):         
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(7, 99), 693)
        self.assertEqual(calc.multiply(0, 0), 0)

    def test_divide(self):         
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(7, 99), 0.0707070707070707)
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()