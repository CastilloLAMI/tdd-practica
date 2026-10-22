"""Módulo FizzBuzz implementado mediante TDD."""


def fizzbuzz(n: int) -> str:
    """Retorna una cadena según las reglas de FizzBuzz:

    - "FizzBuzz" si n es divisible por 3 y por 5 (por 15).
    - "Fizz" si n es divisible por 3.
    - "Buzz" si n es divisible por 5.
    - str(n) en cualquier otro caso.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
