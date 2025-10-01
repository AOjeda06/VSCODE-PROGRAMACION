#Crea con un editor el fichero de texto Alumnos.txt y escribe en él los nombres, edades y estaturas de los alumnos de un grupo, cada uno en una línea:
#	juan 22 1.77
#	luis 21 1.80
#	pedro 20 1.73
#	…
#Implementa un programa que lea del fichero los datos, muestre los nombres y calcule la media de la edad y de las estaturas, mostrándolas por pantalla.

#Abrir el fichero en modo lectura
with open("Alumnos.txt", "r", encoding="utf-8") as file:
    # Inicializar variables para calcular la media
    total_edad = 0
    total_estatura = 0
    contador = 0

    print("Nombres de los alumnos:")
    # Leer cada línea del fichero
    for linea in file:
        # Dividir la línea en nombre, edad y estatura
        partes = linea.split()
        nombre = partes[0]
        edad = int(partes[1])
        estatura = float(partes[2])

        # Mostrar el nombre del alumno
        print(nombre)

        # Acumular la edad y la estatura
        total_edad += edad
        total_estatura += estatura
        contador += 1

    # Calcular la media de la edad y la estatura
    if contador > 0:
        media_edad = total_edad / contador
        media_estatura = total_estatura / contador

        # Mostrar las medias por pantalla
        print(f"\nMedia de edad: {media_edad:.2f} años")
        print(f"Media de estatura: {media_estatura:.2f} metros")
    else:
        print("No hay datos de alumnos en el fichero.")

    # Cerrar el fichero
    file.close()