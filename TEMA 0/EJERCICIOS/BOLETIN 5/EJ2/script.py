#Crea un programa en python que cree un fichero en modo escritura. A continuación, irá leyendo línea a línea de 
# teclado hasta que el usuario introduzca la cadena “fin”. Debe escribir cada línea en el fichero creado.

#Creando y abriendo el fichero en modo escritura
with open("ArchivoDePrueba.txt", "w", encoding="utf-8") as file:
    linea = ""
    while linea.lower() != "fin":
        linea = input("Introduce una línea (o 'fin' para terminar): ")
        if linea.lower() != "fin":
            file.write(linea + "\n")
#Cerrando el fichero
file.close()