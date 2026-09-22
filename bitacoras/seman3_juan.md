## Ejemplo con validacion de cuantos caracteres cuenta un texto para crear un ID  


print("nombre de usuario")
id_usuario = input("cree su nombre de usuario: ")

if not id_usuario:
    print("invalido")

elif len(id_usuario) > 10:
    print("invalido")

elif not id_usuario.isalpha():
    print("invalido")

else:
    print(f"nuevo id creado es: {id_usuario}")

## Segundo ejemplo que el programa directamente quite los numeros que pueda encontrar en un texto 

texto = input("Introduce un texto: ")

palabras = texto.split()
cantidad_palabras = len(palabras)

if cantidad_palabras < 15:
    print("Inválido: El texto es demasiado corto (debe tener al menos 15 palabras).")

elif cantidad_palabras > 30:
    print("Inválido: El texto es demasiado largo (no debe superar las 30 palabras).")

else:
    texto_sin_numeros = "".join(c for c in texto if not c.isdigit())
    
    print("Texto procesado:")
    print(texto_sin_numeros)