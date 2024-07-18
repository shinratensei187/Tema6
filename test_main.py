# test_main.py
import unittest
from main import add, subtract, multiply, divide
from termcolor import colored

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(4, 2), 2)
        self.assertEqual(subtract(2, 4), -2)
        self.assertEqual(subtract(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-1, 2), -2)
    
    def test_divide(self):
        self.assertEqual(divide(8, 4), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ValueError) as cm:
            divide(10, 0)
        self.assertEqual(str(cm.exception), colored("Division by zero is not allowed.", "red"))

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print(colored("All tests passed!", "green"))
    else:
        print(colored("Some tests failed.", "red"))

if __name__ == "__main__":
    run_tests()
