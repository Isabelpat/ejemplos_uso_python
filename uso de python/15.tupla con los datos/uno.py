#Crea una función en Python que reciba una lista de números y devuelva una
#tupla con los siguientes datos:
#a. número mayor,
#b. número menor,
#c. promedio,
#d. cantidad de números pares,
#e. cantidad de números impares



def analizar_lista(numeros):
    if not numeros:
        return None

    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)
    pares = sum(1 for n in numeros if n % 2 == 0)
    impares = len(numeros) - pares

    return (mayor, menor, promedio, pares, impares)

# parte pricipal 
entrada = input("Ingresa números separados por coma (ej. 4, 7, 2): ")

try:
    # a enteros
    lista = [int(x.strip()) for x in entrada.split(",")]
    resultado = analizar_lista(lista)

    if resultado:
        print("\nResultados:")
        print(f"Mayor: {resultado[0]}")
        print(f"Menor: {resultado[1]}")
        print(f"Promedio: {resultado[2]}")
        print(f"Pares: {resultado[3]}")
        print(f"Impares: {resultado[4]}")
    else:
        print("La lista está vacía.")
except ValueError:
    # Si los valores no son numerose muestra este mensaje
    print("Error: Asegúrate de ingresar solo números separados por comas.")


