# ================================
# Actualización de estructuras
# ================================

# 1. Actualizar valores en diccionarios y listas

matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6  # Cambia el 3 por 6

print("=== 1.1 MATRIZ ACTUALIZADA ===")
print(matriz)
print()  # línea en blanco para separar secciones

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

cantantes[0]["nombre"] = "Enrique Martin Morales"  # Cambia el nombre del primer cantante

print("=== 1.2 CANTANTES ACTUALIZADOS ===")
print(cantantes)
print()  # línea en blanco para separar secciones

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

ciudades["México"][2] = "Monterrey"  # Cambia "Cancún" por "Monterrey"

print("=== 1.3 CIUDADES ACTUALIZADAS ===")
print(ciudades)
print()  # línea en blanco para separar secciones

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

coordenadas[0]["latitud"] = 9.9355431  # Cambia la latitud

print("=== 1.4 COORDENADAS ACTUALIZADAS ===")
print(coordenadas)
print()  # línea en blanco para separar secciones

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