def validar_password(pwd):
    errores = []
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    return {"valida": len(errores) == 0, "errores": errores}
