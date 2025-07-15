# AE6_ABP-Ejercicio individual del Módulo 3 del Bootcamp Fullstack Python Django

Por Álvaro Ortega Hamel


## Contenido del archivo `funciones_intermedias_1.py`

### 1. Actualización de valores

Se modifican valores dentro de estructuras de datos:

- Se cambia un número dentro de una matriz.
- Se modifica el nombre del primer cantante dentro de una lista de diccionarios.
- Se reemplaza un valor dentro de una lista contenida en un diccionario.
- Se actualiza la latitud en un diccionario que forma parte de una lista.

### 2. Función `iterar_diccionario(lista)`

Recibe una lista de diccionarios y recorre cada uno para imprimir sus llaves y valores en una sola línea por elemento.  
Formato de salida esperado:
nombre - Ricky Martin, pais - Puerto Rico
nombre - Chayanne, pais - Puerto Rico
nombre - José José, pais - México
nombre - Juan Luis Guerra, pais - República Dominicana

### 3. Función `iterar_diccionario2(llave, lista)`

Recibe una llave y una lista de diccionarios. Imprime únicamente los valores asociados a esa llave en cada diccionario.  

Ejemplo de uso:
iterar_diccionario2("nombre", cantantes)

Resultado "nombre":
Ricky Martin
Chayanne
José José
Juan Luis Guerra

Resultado "pais":
Puerto Rico
Puerto Rico
México
República Dominicana

### 4. Función imprimir_informacion(diccionario)

Recorre un diccionario cuyas claves apuntan a listas.
La función imprime el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

Ejemplo de salida:

4 CIUDADES
San José
Limón
Cartago
Puntarenas

5 COMIDAS
gallo pinto
casado
tamales
chifrijo
olla de carne