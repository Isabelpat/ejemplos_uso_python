#5. Hacer un programa en Python que calcule el Índice de Masa Corporal de una
#persona (IMC = peso[kg] / altura 2 [m]) e indique el estado en el que se encuentra
#esa persona en función del valor de IMC.Valor de IMC Diagnóstico
#< 16 Criterio de ingreso en hospital
#de 16 a 17 Infrapeso
#de 17 a 18 Bajo peso
#de 18 a 25 peso normal (saludable)
#de 25 a 30 Sobrepeso (obesidad de grado I)
#de 30 a 35 Sobrepeso crónico (obesidad de grado II)
#de 35 a 40 Obesidad premórbida (obesidad de grado III)
#> 40 Obesidad mórbida (obesidad de grado IV)

# Función para solicitar un valor positivo ya que seguimos evitando meter numeros negativos
def solicitar_valor_positivo(nombre):
    while True:
        try:
            valor = float(input(f"Ingrese su {nombre} en {'kg' if nombre == 'peso' else 'metros'}: "))
            if valor > 0:
                return valor
            else:
                print("Por favor, ingrese un número mayor que cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Solicitar datos del usuario
peso = solicitar_valor_positivo("peso")
altura = solicitar_valor_positivo("altura")

# Calcular el IMC
imc = peso / (altura ** 2)

# Determinar el diagnóstico
if imc < 16:
    diagnostico = "Criterio de ingreso en hospital"
elif imc < 17:
    diagnostico = "Infrapeso"
elif imc < 18:
    diagnostico = "Bajo peso"
elif imc < 25:
    diagnostico = "Peso normal (saludable)"
elif imc < 30:
    diagnostico = "Sobrepeso (obesidad de grado I)"
elif imc < 35:
    diagnostico = "Sobrepeso crónico (obesidad de grado II)"
elif imc < 40:
    diagnostico = "Obesidad premórbida (obesidad de grado III)"
else:
    diagnostico = "Obesidad mórbida (obesidad de grado IV)"

# Mostrar resultados
print(f"\nSu IMC es: {imc:.2f}")
print(f"Diagnóstico: {diagnostico}")
