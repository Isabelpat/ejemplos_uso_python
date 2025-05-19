#8. Hacer un programa en Python que imprima la serie de la sumatoria Σ , donde 1𝑛
#n es ingresado por el usuario.
#a. Ejemplo de salida: 1/1, 1/2, 1/3, … , 1/n


# Solicitar al usuario el valor de n
try:
    n = int(input("Ingresa un número entero positivo (n): "))
    
    if n <= 0:
        print("Por favor, ingresa un número mayor que 0.")
    else:
        print("\nSerie de sumatoria Σ (1/k) hasta n:")
        for i in range(1, n + 1):
            print(f"1/{i}", end=", " if i < n else "\n")
except ValueError:
    print("Por favor, ingresa un número entero válido.")


