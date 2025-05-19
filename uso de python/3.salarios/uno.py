#Hacer un programa en Python que calcule el salario semanal de un obrero,
#según los siguientes criterios:
#○ Si trabajó 40 horas o menos, sele paga $16 por hora.
#○ Si trabajó más de 40 horas, se le paga $16 por las primeras 40 horas, y $20
#por cada hora extra



# vamos a solicita al usuario las horas trabajadas
horas_trabajadas = float(input("Ingresa el número de horas trabajadas en la semana: "))

# Define las tarifas
tarifa_normal = 16
tarifa_extra = 20
limite_horas = 40

# Calcula el salario
if horas_trabajadas <= limite_horas:
    salario = horas_trabajadas * tarifa_normal
else:
    horas_extra = horas_trabajadas - limite_horas
    salario = (limite_horas * tarifa_normal) + (horas_extra * tarifa_extra)

# Muestra el resultado
print(f"El salario semanal del obrero es: ${salario:.2f}")
