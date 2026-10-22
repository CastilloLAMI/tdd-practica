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

    def test_rango_completo(self):
        esperados = {
            1: "1", 2: "2", 3: "Fizz", 4: "4", 5: "Buzz",
            6: "Fizz", 10: "Buzz", 14: "14", 15: "FizzBuzz",
            30: "FizzBuzz", 45: "FizzBuzz",
        }
        for n, esperado in esperados.items():
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), esperado)


if __name__ == '__main__':
    unittest.main()
