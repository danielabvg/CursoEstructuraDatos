# Ejercicio 1 - Simulación de Sensores en un Robot

# Lecturas de los sensores (cm)
sensores = [120, 85, 210, 150]
umbral = 100

# Recorrer los sensores
for i in range(len(sensores)):
    print(f"Sensor {i+1}: {sensores[i]} cm")
    if sensores[i] < umbral:
        print("⚠ Advertencia: Obstáculo demasiado cerca")
