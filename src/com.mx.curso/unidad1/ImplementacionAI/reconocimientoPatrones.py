# Características de una flor
caract = [3.5, 1.4, 0.2]

sumaTotal = sum(caract) 
print("Suma total del vector:", sumaTotal)

# Normalizar cada valor
normalizado = [i / sumaTotal for i in caract] #normalización

print("Vector normalizado:", normalizado)
