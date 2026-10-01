# reto 1 
def contador_edades():

    contador = 0 
    print("Ingrese edades una por una.")
 
    edad = int(input("Edad: "))
 
    while edad >= 0:
        contador = contador + 1
        edad = int(input("Edad: "))
 
    print("Total de edades válidas ingresadas:", contador)
