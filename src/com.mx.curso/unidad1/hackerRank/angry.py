# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, 
# the professor decides to cancel class if fewer than some number of students are present when class starts. 
# Arrival times go from on time (arrivalTime </ 0 ) to arrived late (arrivalTime > 0 ).

# Construir arreglo vacío
listaAlumnos = []

# Input Determinar el largo del arrglo dado por el usuario [n]
n = int(input("Ingresa el total de estudiantes: "))
print("n = ", n)

# Input Datos del arreglo uno por uno 
# Mensajes iniciales
print("=== Registro de llegadas de alumnos ===")

# Repetir hasta que el usuario escriba "fin"
for i in range(n):
    valor = int(input(f"Ingrese el tiempo de llegada del estudiante {i+1}: "))
    listaAlumnos.append(valor)

print("Lista de llegadas:", listaAlumnos)

# Return [k] total de alumnos que llegaron a tiempo (umbral)
k = int(input("Ingresa el número mínimo de alumnos que deben llegar a tiempo: "))
print("k = ", k)

# Non-positive arrival times (a[i] <= 0) indicate the student arrived early or on time; 
# positive arrival times (a[i] > 0) indicate the student arrived minutes late.
# Contar alumnos puntuales
puntuales = sum(1 for x in listaAlumnos if x <= 0)
print("Total de alumnos puntuales:", puntuales)

# Return YES if class is cancelled
# Return NO if class goes on
if puntuales < k:
    print("YES")
else:
    print("NO")



