#12.Crea un programa en Python para gestionar un pequeño catálogo de
#productos. Cada producto tendrá:
#a. un código clave
#b. una tupla con nombre, precio y cantidad disponible
#Implementa funciones para:
#a. Agregar productos,
#b. Consultar un producto por código,
#c. Calcular el valor total del inventario



# Diccionario de productos
productos = {}

# Función para agregar productos
def agregar_producto():
    codigo = input("Ingresa el código del producto: ")
    if codigo in productos:
        print("⚠️ Ese código ya está registrado.")
        return
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad disponible: "))
    except ValueError:
        print("❌ Error: Precio o cantidad no válidos.")
        return
    productos[codigo] = (nombre, precio, cantidad)
    print(f"✅ Producto '{nombre}' agregado con código {codigo}.")

# Función para consultar un producto por su código
def consultar_producto():
    codigo = input("Ingresa el código del producto a consultar: ")
    if codigo in productos:
        nombre, precio, cantidad = productos[codigo]
        print(f"\n🔎 Producto encontrado:")
        print(f"Nombre: {nombre}")
        print(f"Precio: ${precio}")
        print(f"Cantidad disponible: {cantidad}\n")
    else:
        print("❌ No existe un producto con ese código.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = 0
    for nombre, precio, cantidad in productos.values():
        total += precio * cantidad
    print(f"\n💰 Valor total del inventario: ${total:.2f}\n")

# Menú principal
def menu():
    while True:
        print("----- MENÚ -----")
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Calcular valor total del inventario")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            calcular_valor_total()
        elif opcion == "4":
            print("👋 Programa finalizado.")
            break
        else:
            print("❌ Opción inválida.\n")

# Ejecutar programa
menu()
