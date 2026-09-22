def validar_nombre(nombre):
    nombre = nombre.strip()

    if not nombre:
        return False

    return nombre.replace(" ", "").isalpha()


def validar_correo(correo):
    correo = correo.strip()

    if not correo:
        return False

    return "@" in correo and "." in correo


def validar_rango(valor, minimo, maximo):
    return minimo <= valor <= maximo

