#Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada
#  como un diccionario. La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. Crea un 
# menú para las distintas opciones e implementa una función para cada opción.

#Diccionario para almacenar los contactos
libreta_contactos = {}

#Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    libreta_contactos[nombre] = telefono
    print(f"Contacto {nombre} agregado con el teléfono {telefono}.")   
     
#Función para eliminar un contacto
def eliminar_contacto(nombre):
    if nombre in libreta_contactos:
        del libreta_contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"El contacto {nombre} no existe.")

#Función para buscar un contacto
def buscar_contacto(nombre):
    if nombre in libreta_contactos:
        print(f"El teléfono de {nombre} es {libreta_contactos[nombre]}.")
    else:
        print(f"El contacto {nombre} no existe.")

#Menú de opciones
opcion = None
while opcion != '0':
    print("\nMenú de opciones:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("0. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el número de teléfono: ")
        agregar_contacto(nombre, telefono)
    elif opcion == '2':
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == '3':
        nombre = input("Introduce el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == '0':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")      
