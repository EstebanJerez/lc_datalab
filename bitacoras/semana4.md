# ¿Cuántas veces se ejecuta validar_nombre()?
Se ejecuta 5 veces.
# ¿Cuántas veces se ejecuta el if?
Se ejecuta 5 veces.
# ¿Qué parte cambia en cada iteración?
Cambian las variables 3 y 5 porque el modulo validar nombre tiene la linea isalpha y strip que solo permiten letras y eliminan numeros y caracteres especiales.
# ¿Qué parte permanece igual?
Las variables 1, 2 y 4 quedan igual porque solo contienen letras.

# Ejercicio integrador

from validaciones import validar_nombre, validar_correo, validar_rango


cantidad = int(input("¿Cuántos registros desea procesar? "))

validos = 0
invalidos = 0

    for i in range(cantidad):

    print(f"\nRegistro {i + 1}")

    nombre = input("Nombre: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))
    valor = float(input("Valor: "))

    nombre_valido = validar_nombre(nombre)
    correo_valido = validar_correo(correo)
    edad_valida = validar_rango(edad, 0, 120)
    valor_valido = validar_rango(valor, 0, 100)

    if nombre_valido and correo_valido and edad_valida and valor_valido:
        validos += 1
        print("Registro válido")
    else:
        invalidos += 1
        print("Registro inválido")


calidad = (validos / cantidad) * 100

 ## salida 

print("\n===== RESUMEN =====")

print("Total:", cantidad)

print("Válidos:", validos)

print("Inválidos:", invalidos)

print("Calidad:", calidad, "%")

# Reflexión 
- ¿Qué problema resuelve un ciclo?
    - Optimizar el codigo sin necesidad de intervenir. 
- ¿Por qué range(5) produce cinco iteraciones?
    - Porque el parametro que se la es 5 y arroja 5 datos (del 0 al 4).
- ¿Qué diferencia existe entre una función y un ciclo?
    - La función es la que genera valores (secuencia) dependiendo del parametro que se le da. Ciclo es una accion repetitiva con un codigo ya predefinido o parametro.
- ¿Por qué una validación debería ser una función reutilizable?
    - Si, porque ya es un codigo guardado con un nombre en especifico que se le fue establecido, al momento de "llamar" al nombre en un nuevo codigo sera ejecutado el codigo que tiene el nombre. 
- ¿Por qué separar las validaciones en un módulo?
    - Para organizarlas y sean mas facil de encontrarlas, y para cuando sea necesario la utilidad de las mismas solo sera necesario llamar a la validacion que se necesite. 
- ¿Qué función cumplen los contadores?
    - Para verificar la cantidad de daatos en especificos, puede funcionar como un filtro o un resultado. 
- ¿Qué diferencia existe entre procesar un registro y procesar muchos registros?
    - La cantidad de procesos que tiene que hacer el codigo. 
- ¿Qué ocurre si cambia una regla de validación?
    - Pueden ocurrir dos cosas puede cambiar el resultado o ni siquiera botar un resultado o error.  
- ¿Por qué no conviene copiar y pegar una validación?
    - Porque hay validaciones que dependen de otras validaciones, entonces al copiar una independiente, es muy probable que no sea ejecutable. 
- ¿Cómo contribuye esta arquitectura al crecimiento de DataLab?
    - Permite ejecutar muchas operaciones, sin necesidad de estar creando nuevo codigo o haciendo extenso el mismo y mas limpio. 