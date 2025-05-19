#14.Crea un programa en Python para gestionar una agenda donde cada contacto
#tiene:
#a. un nombre (clave del diccionario)
#b. una tupla con teléfono y correo
#Implementa funciones para:
#a. Agregar un contacto,
#b. Buscar un contacto por nombre,
#c. Actualizar datos de un contacto




# Diccionario 
agenda = {}

def agregar_contacto():
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")
        agenda[nombre] = (telefono, correo)
        print("Contacto agregado.")

def buscar_contacto():
    nombre = input("Nombre del contacto a buscar: ")
    if nombre in agenda:
        telefono, correo = agenda[nombre]
        print(f" {nombre} - Teléfono: {telefono}, Correo: {correo}")
    else:
        print(" Contacto no encontrado.")

def actualizar_contacto():
    nombre = input("Nombre del contacto a actualizar: ")
    if nombre in agenda:
        telefono = input("Nuevo teléfono: ")
        correo = input("Nuevo correo: ")
        agenda[nombre] = (telefono, correo)
        print(" Contacto actualizado.")
    else:
        print(" Contacto no encontrado.")

# Menú 
def menu():
    while True:
        print("\n AGENDA DE CONTACTOS")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Ver todos los contactos")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            actualizar_contacto()
        elif opcion == "4":
            for nombre, datos in agenda.items():
                print(f"{nombre}: Tel: {datos[0]}, Correo: {datos[1]}")
        elif opcion == "5":
            print(" Saliendo de la agenda...")
            break
        else:
            print(" Opción inválida.")

#aqui ejecutamos
menu()
