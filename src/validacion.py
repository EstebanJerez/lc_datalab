def validar_cadena_no_vacia(texto):
    """
    Verifica que una cadena tenga contenido.

    strip() elimina espacios al inicio y al final.
    """
    if texto is None:
        return False

    return texto.strip() != ""

def validar_longitud(texto, minimo, maximo):
    """
    Verifica que la longitud de una cadena esté dentro de un rango.

    Ejemplo:
        validar_longitud("Python", 3, 10) -> True
    """
    if texto is None:
        return False

    longitud = len(texto.strip())

    return minimo <= longitud <= maximo

