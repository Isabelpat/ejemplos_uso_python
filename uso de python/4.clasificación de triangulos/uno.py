#Hacer un programa en Python que clasifique el tipo de triángulo a partir de sus
#lados ingresados:
#Triángulo Medidas de los lados
#Equilátero Los 3 son iguales
#Isósceles Tiene 2 lagos iguales y un lado distinto
#Escaleno Los 3 lados son distintos

#vamos a tomar en cuenta que es posible metan numeros negativos y lo vamos a evitar
# Función para solicitar un valor positivo
def solicitar_lado(nombre):
    while True:
        try:
            valor = float(input(f"Ingrese la longitud del lado {nombre}: "))
            if valor > 0:
                return valor
            else:
                print("Por favor, ingresa un número mayor que cero.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

# Solicitar los tres lados
lado1 = solicitar_lado("A")
lado2 = solicitar_lado("B")
lado3 = solicitar_lado("C")

# Verificar si los lados forman un triángulo válido (desigualdad triangular)
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Clasificación del triángulo
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"El triángulo es {tipo}.")
else:
    print("Los lados ingresados no forman un triángulo válido.")

