import unittest
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_numero_normal(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(4), "4")

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
