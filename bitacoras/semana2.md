# Semana 2
## ¿Qué significa una condición? 
- estructura determinada por condiciones para tomar desiciones y ejecutar diferentes bloques de codigo segun si la condicion se es verdadera o falsa (se comple o no se cumple )
## ¿Qué ocurre cuando es verdadera?
- el programa ejecuta el bloque de codigo asociado a esa condicion 
## ¿Qué ocurre cuando es falsa?
- el progrma ignora el bloque de codigo principal de esa condicion y busca si existe una condicion alternativa 
## ¿Por qué puede haber varias alternativas? 
- para evaluar múltiples escenarios cuando la respuesta no es solo de "sí o no"
## Actividad Feynman

**Explicación sencilla:**
Imagínate un termómetro en una habitación. Tenemos una temperatura ideal (por ejemplo, entre 18 y 24 grados). Si la temperatura está más fría de 18, encendemos la calefacción. Si está más caliente de 24, encendemos el aire acondicionado. Si está justo entre 18 y 24, no hacemos nada porque está perfecta. Así es como DataLab decide qué hacer según el número que recibe.

## Respuestas a las preguntas:

- ¿Cuántos caminos existen?

   Existen 3 caminos posibles (por debajo del rango, dentro del rango, y por encima del rango).

- ¿Qué condición permite seleccionar cada camino?
   - Camino 1 (Por debajo): Que el valor sea menor que el límite dado (18).
   - Camino 2 (Dentro): Que el valor sea mayor o igual al límite (18) Y menor o igual al límite (24).
   - Camino 3 (Por encima): Que el valor sea mayor que el límite superior del rango.

- ¿Qué ocurre si el valor está exactamente en el límite?

   Se considera que está dentro del rango esperado a menos que las reglas definan explícitamente

# Diseñar antes de programar

### Entrada
- Un valor numérico (recibido por DataLab) y los valores límites del rango (mínimo y máximo).

### Reglas
- Si el valor es menor que el límite mínimo -> es "por debajo".
- Si el valor es mayor o igual al mínimo Y menor o igual al máximo -> está "dentro".
- Si el valor es mayor que el límite máximo -> es "por encima".

### Salidas
- Un mensaje o texto con la clasificación del valor: "Por debajo", "Dentro" o "Por encima" del rango esperado.

# Explicacion de la modificacion del comando if 
 **-Se agregaron tres reglas:**
  - Si no se ingresa el identificador del registro devuelve un error.
  - Si no se ingresa un valor de registro devuelve un error. 
  - Si no se ingresa un valor numerico devuelve un error.  

  ## pseudocodigo 

    inicio

        leer valor 
        Si el usuario no registra un valor muestra "no se ingreso un valor para el registro"
        Si el usuariono ingresa el identificador del registro muestra "no se ha ingresado un identificador de registro"
        Si el valor es mayor o igual a 50 muestra "clasificacion igual ALTO"
        Si no muestra "Clasificacion igual NORMAL"

        Mostrar clasificacion 
    
    Fin
