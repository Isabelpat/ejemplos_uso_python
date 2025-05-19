#Hacer un programa en Python que imprima la serie y además el valor obtenido
#de la sumatoria n
#2 Σ , donde n es ingresado por el usuario (n no debe ser mayor
#de 5).

# Solicitar al usuario el valor de n
n = int(input("Ingrese un valor de n (no mayor que 5): "))

# Verificar que n no sea mayor que 5
if n > 5:
    print("El valor de n debe ser menor o igual a 5.")
else:
    # Imprimir la serie de números cuadrados
    serie = [i**2 for i in range(1, n+1)]
    print("Serie de los cuadrados: ", serie)
    
    # Calcular la sumatoria
    suma = sum(serie)
    print(f"El valor de la sumatoria es: {suma}")

