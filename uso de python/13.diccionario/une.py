import string

def contar_palabras(frase):
    # Convertir a minúsculas
    frase = frase.lower()
    # Eliminar signos de puntuación
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    # Separar en palabras
    palabras = frase.split()
    
    # Contar palabras
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    return conteo

# Programa principal
def main():
    texto = input("Ingresa una frase o párrafo: ")
    resultado = contar_palabras(texto)

    print("\n Recuento de palabras:")
    for palabra, veces in resultado.items():
        print(f"'{palabra}': {veces} vez/veces")

# Ejecutar
main()
