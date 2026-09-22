#edad
edad = int(input("Ingrese la edad: "))

if edad < 0:
  print("Numero invalido. La edad no puede ser negativa.")
elif edad >= 18:
  print("Mayor de edad.")
  print("Es mayor de edad, puede votar.")
else: # This block handles ages between 0 and 17
  print("Menor de edad.")
  print("No es mayor de edad, no puede votar.")
  
#estado jugador
  def procesar_estado_jugador(jugador):
    mensaje = ""
    match jugador.estado:
        case "vivo" if jugador_salud > 75:
            mensaje = "El jugador está en óptimas condiciones."
        case "vivo" if jugador_salud > 25 and jugador_salud <= 75:
            mensaje = "El jugador tiene salud moderada. Está listo para seguir."
        case "vivo" if jugador_salud > 0 and jugador_salud <= 25:
            mensaje = "El jugador está gravemente herido y necesita curación urgente."
        case "vivo" if jugador_salud <= 1:
            mensaje = "El jugador ha sido derrotado y está inconsciente."
        case "inconsciente":
            mensaje = "El jugador ha caído. Iniciando cuenta regresiva de reanimación..."
        case "eliminado":
            mensaje = "Fin del juego para este personaje."
        case _: # Default case if no other matches or unknown state
            mensaje = "Estado desconocido o inválido."
    return mensaje