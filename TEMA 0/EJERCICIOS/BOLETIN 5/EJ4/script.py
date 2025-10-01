#Implementa un programa que lea números enteros no ordenados de un archivo, con un número por línea, y 
# los almacene en una lista. A continuación, debe guardar los números de la lista en otro fichero distinto pero ordenados de forma ascendente.

#Abrir el fichero de entrada en modo lectura
with open("numeros.txt", "r", encoding="utf-8") as file:
    #Leer los números del fichero y almacenarlos en una lista
    numeros = [int(linea.strip()) for linea in file]
    #Ordenar la lista de números de forma ascendente
    numeros.sort()

    #Cerrar el fichero
    file.close()

#Abrir el fichero de salida en modo escritura
with open("numeros_ordenados.txt", "w", encoding="utf-8") as file:
    #Escribir los números ordenados en el nuevo fichero, uno por línea
    for num in numeros:
        file.write(f"{num}\n")

    #Cerrar el fichero
    file.close()