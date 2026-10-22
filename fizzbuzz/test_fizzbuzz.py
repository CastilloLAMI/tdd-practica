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


if __name__ == '__main__':
    unittest.main()
