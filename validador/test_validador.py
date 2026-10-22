import unittest
from validador.validador import validar_password


class TestValidarPassword(unittest.TestCase):
    def test_password_muy_corta(self):
        res = validar_password("Abc1!")
        self.assertFalse(res["valida"])
        self.assertIn("Mínimo 8 caracteres", res["errores"])

    def test_password_longitud_ok(self):
        res = validar_password("Abcdefg1!")
        # Solo verificamos que NO tenga error de longitud
        self.assertNotIn("Mínimo 8 caracteres", res["errores"])

    def test_sin_mayuscula(self):
        res = validar_password("abcdefg1!")
        self.assertFalse(res["valida"])
        self.assertIn("Al menos una mayúscula", res["errores"])

    def test_sin_minuscula(self):
        res = validar_password("ABCDEFG1!")
        self.assertFalse(res["valida"])
        self.assertIn("Al menos una minúscula", res["errores"])

    def test_sin_digito(self):
        res = validar_password("Abcdefgh!")
        self.assertFalse(res["valida"])
        self.assertIn("Al menos un dígito", res["errores"])


if __name__ == '__main__':
    unittest.main()
