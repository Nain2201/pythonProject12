def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad en un período de tiempo dado.

    Args:
    datos (list): Una lista de listas que contiene los datos de temperatura para cada ciudad y semana.

    Returns:
    dict: Un diccionario donde las claves son el nombre de las ciudades y los valores son las temperaturas promedio.
    """
    temperatura_promedio_por_ciudad = {}  # Creamos un diccionario para almacenar los resultados

    for ciudad_data in datos:
        ciudad = ciudad_data[0]  # El primer elemento de cada lista es el nombre de la ciudad
        temperaturas_semana = ciudad_data[1:]  # El resto de elementos son temperaturas de las semanas
        suma_temperaturas = sum(temperaturas_semana)
        temperatura_promedio = suma_temperaturas / len(temperaturas_semana)

        # Almacenamos la temperatura promedio en el diccionario
        temperatura_promedio_por_ciudad[ciudad] = temperatura_promedio

    return temperatura_promedio_por_ciudad

# Ejemplo de datos de temperaturas para 3 ciudades durante 4 semanas
datos_temperaturas = [
    ["Ciudad A", 25, 28, 30, 27],
    ["Ciudad B", 22, 26, 24, 23],
    ["Ciudad C", 30, 32, 31, 29]
]

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = calcular_temperatura_promedio(datos_temperaturas)

# Imprimimos los resultados
for ciudad, promedio in temperaturas_promedio.items():
    print(f"La temperatura promedio en {ciudad} es {promedio} grados Celsius.")
