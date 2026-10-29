# Reto 1
def contador_edades():

    contador = 0 
    print("Ingrese edades una por una.")
 
    edad = int(input("Edad: "))
 
    while edad >= 0:
        contador = contador + 1
        edad = int(input("Edad: "))
 
    print("Total de edades válidas ingresadas:", contador)

# Reto 2

    for n in range(1, 11):

        print("Sensor", n , ": Temperatura  procesada")

    print("Lote completo")

# Reto 3

clave_correcta = "Data2026"

    while True:
        clave = input("Ingrese la contraseña: ")

        if clave == clave_correcta:
            print("Acceso concedido")
            break

        else:

    print("Acceso denegado, intente de nuevo")

# Reto 4

valores = [10, 55, 2, 80, 15, 100, 40]

    for valor in valores:
        if valor > 50:

        print(valor)
        else:

            print("Valor descartado")