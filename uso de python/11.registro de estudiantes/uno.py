#11. Hacer un programa en Python que permita registrar las calificaciones de varios
#estudiantes. Cada estudiante tiene un nombre y una lista de calificaciones,
#implementa funciones para:
#a. Agregar un estudiante
#b. Agregar una calificación
#c. Calcular el promedio de cada estudiante
#Ejemplo de estructura de datos:
#estudiantes = {
# "Pedro": [8.5, 9.0],
# "Maria": [7.0, 9.5, 8.0]

# Diccionario de estudiantes
estudiantes = {}

# Función para registrar un estudiante con 3 calificaciones
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    # Validar que no se registre dos veces
    if nombre in estudiantes:
        print("Este estudiante ya ha sido registrado.")
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
    print(f"Estudiante {nombre} registrado con calificaciones: {calificaciones}")

# Función para mostrar los promedios
def mostrar_promedios():
    print("\nPromedios de los estudiantes:")
    for nombre, calificaciones in estudiantes.items():
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"{nombre}: {promedio:.2f}")

# Ejecución principal
registrar_estudiante()
registrar_estudiante()

mostrar_promedios()


