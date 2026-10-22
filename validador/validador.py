def validar_password(pwd):
    errores = []
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in pwd):
        errores.append("Al menos una mayúscula")
    if not any(c.islower() for c in pwd):
        errores.append("Al menos una minúscula")
    return {"valida": len(errores) == 0, "errores": errores}
