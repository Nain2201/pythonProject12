temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2
        # ... (datos de temperatura para Ciudad 2)
    ],
    [   # Ciudad 3
        # ... (datos de temperatura para Ciudad 3)
    ]
]

# Función para calcular el promedio de temperaturas para una ciudad y una semana específica
def calcular_promedio_temperaturas(ciudad, semana):
    suma_temp = 0
    num_dias = len(temperaturas[ciudad][semana])  # Número de días en la semana

    for dia in temperaturas[ciudad][semana]:
        temperatura = dia["temp"]
        suma_temp += temperatura

    promedio_temp_semana = suma_temp / num_dias
    return promedio_temp_semana

# Calcular el promedio de temperaturas para Ciudad 1 en cada semana e imprimirlo
ciudad = 0  # Ciudad 1

for semana in range(len(temperaturas[ciudad])):
    promedio = calcular_promedio_temperaturas(ciudad, semana)
    print(f"Promedio de temperatura para Semana {semana + 1} en Ciudad {ciudad + 1}: {promedio} grados")
