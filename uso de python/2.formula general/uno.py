#2.-Hacer un programa en Python que resuelva la siguiente ecuación de 2o grado.
#El usuario ingresa los valores de a, b y c.

# Primero para manejar raíces cuadradas de números negativos vamos a importar una libreria
# tome en cuenta el no permitir que se escriba mas que letras por lo que pedira al usuario solo numeros
import cmath  

# segundo hacemos la función para solicitar coeficientes, no sea scrip solo numeros
def solicitar_coeficiente(nombre):
    while True:
        try:
            valor = float(input(f"Ingrese el valor de {nombre}: "))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

# Solicitar coeficientes a, b y c
a = solicitar_coeficiente("a")
while a == 0:
    print("El valor de 'a' no puede ser cero en una ecuación de segundo grado.")
    a = solicitar_coeficiente("a")

b = solicitar_coeficiente("b")
c = solicitar_coeficiente("c")

# Calcular el discriminante
discriminante = cmath.sqrt(b**2 - 4*a*c)

# Calcular las dos soluciones
x1 = (-b + discriminante) / (2 * a)
x2 = (-b - discriminante) / (2 * a)

# Mostrar los resultados
print(f"Las soluciones de la ecuación son:")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
