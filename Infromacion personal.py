# Crear el diccionario informacion_personal
informacion_personal = {
    "nombre": "Juan Leon",
    "edad": 25,
    "ciudad": "Ciudad Original",
    "profesion": "Ingeniera Industrial"
}

# Acceder y modificar el valor de la clave "ciudad"
nueva_ciudad = "Ciudad Patate"
informacion_personal["ciudad"] = nueva_ciudad

# Agregar una nueva clave-valor para representar la "profesion"
informacion_personal["profesion"] = "Analista de Datos"

# Verificar la existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "2831734"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)