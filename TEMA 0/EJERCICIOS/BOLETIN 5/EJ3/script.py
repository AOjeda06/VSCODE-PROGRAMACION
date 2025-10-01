#Diseña una aplicación que pida al usuario su nombre y edad. Estos datos deben guardarse en el fichero datos.txt. 
# Si este fichero existe, deben añadirse al final en una nueva línea, y en caso de no existir, debe crearse.

#Abrir el fichero en modo append (añadir al final) o crear si no existe
with open("datos.txt", "a", encoding="utf-8") as file:
    #Pedir al usuario su nombre y edad
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")

    #Escribir los datos en el fichero
    file.write(f"{nombre} {edad}\n")

    #Cerrar el fichero
    file.close()