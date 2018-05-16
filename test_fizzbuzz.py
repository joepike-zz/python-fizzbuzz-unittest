
import unittest

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return ""

class TestFizzBuzz(unittest.TestCase):
    def test_return_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
    def test_return_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
    def test_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")
    def test_return_default(self):
        self.assertEqual(fizzbuzz(1), "")

if __name__ == "__main__":
    unittest.main()
