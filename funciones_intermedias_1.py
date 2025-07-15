# ================================
# Actualización de estructuras
# ================================

# 1.1 Actualizar valor en matriz
def actualizar_matriz():
    matriz = [[10, 15, 20], [3, 7, 14]]
    matriz[1][0] = 6
    print("=== 1.1 MATRIZ ACTUALIZADA ===")
    print(matriz)
    print()

actualizar_matriz()

# 1.2 Actualizar nombre de un cantante
def actualizar_cantantes():
    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"}
    ]
    cantantes[0]["nombre"] = "Enrique Martin Morales"
    print("=== 1.2 CANTANTES ACTUALIZADOS ===")
    print(cantantes)
    print()

actualizar_cantantes()

# 1.3 Actualizar ciudad en diccionario
def actualizar_ciudades():
    ciudades = {
        "México": ["Ciudad de México", "Guadalajara", "Cancún"],
        "Chile": ["Santiago", "Concepción", "Viña del Mar"]
    }
    ciudades["México"][2] = "Monterrey"
    print("=== 1.3 CIUDADES ACTUALIZADAS ===")
    print(ciudades)
    print()

actualizar_ciudades()

# 1.4 Actualizar coordenadas
def actualizar_coordenadas():
    coordenadas = [
        {"latitud": 8.2588997, "longitud": -84.9399704}
    ]
    coordenadas[0]["latitud"] = 9.9355431
    print("=== 1.4 COORDENADAS ACTUALIZADAS ===")
    print(coordenadas)
    print()

actualizar_coordenadas()

# ================================
# 2. Iterar a través de una lista de diccionarios
# ================================

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
def iterar_diccionario(lista):
    for diccionario in lista:
        # BONUS: imprimir en una sola línea
        salida = ""
        for clave, valor in diccionario.items():
            salida += f"{clave} - {valor}, "
        print(salida.rstrip(", "))  # eliminar coma final

print("\n=== 2. CANTANTES ===")
iterar_diccionario(cantantes)

# ================================
# 3. Obtener valores de una lista de diccionarios
# ================================

def iterar_diccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
        else:
            print(f"La clave '{llave}' no se encuentra en el diccionario.")

print("\n=== 3.1 SOLO NOMBRES ===")
iterar_diccionario2("nombre", cantantes)

print("\n=== 3.2 SOLO PAÍSES ===")
iterar_diccionario2("pais", cantantes)

# ================================
# 4. Iterar un diccionario con listas como valores
# ================================

def imprimir_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for valor in lista:
            print(valor)
        print()  # línea en blanco para separar secciones

print("\n=== 4.INFORMACIÓN DE COSTA RICA ===")
costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }

imprimir_informacion(costa_rica)


if __name__ == "__main__":
    pass