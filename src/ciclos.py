#from validaciones import validar_nombre

for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    if validar_nombre(nombre):
        print("Nombre válido")
    else:
        print("Nombre inválido")

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