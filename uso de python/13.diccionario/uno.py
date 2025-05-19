


import string

def contar_palabras(frase):
    # Convertir a minúsculas
    frase = frase.lower()
    # Eliminar signos de puntuación
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    # Separar en palabras
    palabras = frase.split()
    
    # Crear diccionario de conteo
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    # Encontrar la palabra más repetida
    palabra_mas_frecuente = max(conteo, key=conteo.get)
    frecuencia = conteo[palabra_mas_frecuente]

    return conteo, palabra_mas_frecuente, frecuencia
frase = "Hola, hola mundo! Mundo mundo..."
conteo, palabra_frecuente, veces = contar_palabras(frase)

print("Conteo de palabras:", conteo)
print("Palabra más frecuente:", palabra_frecuente)
print("Aparece:", veces, "veces")