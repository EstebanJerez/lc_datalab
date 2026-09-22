def obtenerValorEntero(numero):
 
  valor_float = float(numero)
  
  valorEntero = int(valor_float)
  
  if valor_float != valorEntero:
    print("Se han removido los decimales")
  else:
    print("No se han removido decimales")
  return valorEntero

valor = input("Ingrese un valor:")
resultado = obtenerValorEntero(valor)
print(resultado)


def obtenerPromedio():
  numnotas = int(input("Ingrese numero de notas: "))
  lista_notas = []
  for i in range(numnotas):
    nota = float(input(f"Ingrese la nota {i+1} (Con decimales): "))
    lista_notas.append(nota)

    promedio = sum(lista_notas) / numnotas
  return promedio

resultadoPromedio = obtenerPromedio()

if resultadoPromedio >= 2.0:
  print("El estudiante ha aprobado")
else:
  print("El estudiante ha reprobado")
print(resultadoPromedio)