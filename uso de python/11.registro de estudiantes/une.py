# Diccionario para guardar estudiantes y calificaciones
estudiantes = {}

# Límite de estudiantes
limite = 5

# Función para registrar un estudiante
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    # Validar si ya fue registrado
    if nombre in estudiantes:
        print("Este estudiante ya fue registrado.")
        return

    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación #{i} de {nombre}: "))
                if 0 <= nota <= 10:
                    calificaciones.append(nota)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    estudiantes[nombre] = calificaciones
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre} registrado. Promedio: {promedio:.2f}\n")

# Registro de hasta 5 estudiantes
print("Registro de estudiantes (máximo 5):\n")
while len(estudiantes) < limite:
    registrar_estudiante()

print("Registro completo. Lista de estudiantes y promedios:")
for nombre, calificaciones in estudiantes.items():
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre}: {promedio:.2f}")

