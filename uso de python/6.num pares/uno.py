#6.-Hacer un programa en Python que, por un número entero dado por el usuario,
#muestre la lista de números pares inferiores a él.


# Solicitar número al usuario
try:
    numero = int(input("Ingresa un número entero: "))
    if numero <= 1:
        print("No hay números pares menores a ese número.")
    else:
        print(f"Números pares menores que {numero}:")
        for i in range(2, numero, 2):
            print(i)
except ValueError:
    print("Por favor, ingresa un número entero válido.")
