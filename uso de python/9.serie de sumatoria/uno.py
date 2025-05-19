#Hacer un programa en Python que imprima el valor obtenido de la sumatoria
#Σ 1/n , donde n es ingresado por el usu

# Calcular la sumatoria de 1/i desde i=1 hasta n

try:
    n = int(input("Ingresa un número entero positivo (n): "))
    
    if n <= 0:
        print("Por favor, ingresa un número mayor que 0.")
    else:
        suma = 0.0
        for i in range(1, n + 1):
            suma += 1 / i
        
        print(f"\nLa sumatoria de 1/i desde 1 hasta {n} es: {suma:.4f}")
except ValueError:
    print("Entrada no válida. Ingresa un número entero.")
