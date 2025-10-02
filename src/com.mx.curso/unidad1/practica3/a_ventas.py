# Ejercicio 6: Análisis de Ventas Diarias con Arreglos

dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
ventas = []

for dia in dias:
    valor = float(input(f"Ingrese las ventas del {dia}: "))
    ventas.append(valor)

total = sum(ventas)
maximo = max(ventas)
minimo = min(ventas)

print("Total de ventas en la semana:", total)
print("Día con más ventas:", dias[ventas.index(maximo)], "-", maximo)
print("Día con menos ventas:", dias[ventas.index(minimo)], "-", minimo)
