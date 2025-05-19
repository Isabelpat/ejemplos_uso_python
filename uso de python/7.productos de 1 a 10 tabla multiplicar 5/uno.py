#Hacer un programa en Python que muestre los productos del 1 al 10 de la tabla
#de multiplicar del número 5

# Mostrar la tabla de multiplicar del 5
numero = 5
print(f"Tabla del {numero}:")

for i in range(1, 11):  # Del 1 al 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# o que el usuario de el numero por el cual se multiplicara
# Pedir al usuario el número de la tabla
try:
    numero = int(input("¿De qué número quieres ver la tabla de multiplicar? "))
    print(f"\nTabla del {numero}:")
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
