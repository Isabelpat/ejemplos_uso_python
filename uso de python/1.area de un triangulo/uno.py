#1. Hacer un programa en Python que resuelva la siguiente expresión aritmética del área de un Triángulo, 
# donde el usuario ingresa la base y la altura.

#primero vamos a poner la solicitud al ussuario 
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# Calcula el área
area = (base * altura) / 2

# muestra el resultado
print(f"El área del triángulo es: {area:.2f}")
