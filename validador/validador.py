"""Módulo de validación de contraseñas implementado mediante TDD."""

from typing import Any

CARACTERES_ESPECIALES: str = "!@#$%^&*"


def validar_password(pwd: str) -> dict[str, Any]:
    """Valida una contraseña según 5 reglas de seguridad:

    1. Mínimo 8 caracteres.
    2. Al menos una letra mayúscula.
    3. Al menos una letra minúscula.
    4. Al menos un dígito numérico.
    5. Al menos un carácter especial (!@#$%^&*).

    Retorna un diccionario con:
    - 'valida': bool (True si cumple todas las reglas, False si no)
    - 'errores': list[str] (lista con los mensajes de error detectados)
    """
    errores: list[str] = []

    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in pwd):
        errores.append("Al menos una mayúscula")
    if not any(c.islower() for c in pwd):
        errores.append("Al menos una minúscula")
    if not any(c.isdigit() for c in pwd):
        errores.append("Al menos un dígito")
    if not any(c in CARACTERES_ESPECIALES for c in pwd):
        errores.append("Al menos un carácter especial")

    return {
        "valida": len(errores) == 0,
        "errores": errores,
    }
