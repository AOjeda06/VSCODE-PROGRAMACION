#Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son los nombres 
# de los productos y los valores son las cantidades vendidas. El programa debe permitir al usuario agregar nuevas 
# ventas y calcular el total de ventas para un producto específico. Implementa un menú con ambas opciones. 

# Diccionario para almacenar las ventas
ventas = {}

# Función para agregar una venta
def agregar_venta(producto, cantidad):
    if producto in ventas: 
        ventas[producto] += cantidad
    else:
        ventas[producto] = cantidad
    print(f"Se han agregado {cantidad} unidades de {producto}. Total vendido: {ventas[producto]}")

# Función para calcular el total de ventas de un producto específico
def total_ventas(producto):
    if producto in ventas:
        print(f"Total de ventas de {producto}: {ventas[producto]}")
    else:
        print(f"No se han registrado ventas para el producto {producto}.")
        
# Menú de opciones
opcion = None
while opcion != '0':
    print("\nMenú de opciones:")
    print("1. Agregar venta")
    print("2. Calcular total de ventas de un producto")
    print("0. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        producto = input("Introduce el nombre del producto: ")
        cantidad = int(input("Introduce la cantidad vendida: "))
        agregar_venta(producto, cantidad)
    elif opcion == '2':
        producto = input("Introduce el nombre del producto para calcular el total de ventas: ")
        total_ventas(producto)
    elif opcion == '0':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")