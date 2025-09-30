#Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de 
# cada palabra en el texto.

#Cadena de texto de ejemplo
texto = input("Introduce una cadena de texto: ")

#Dividir el texto en palabras
palabras = texto.split()

#Diccionario para almacenar la frecuencia de cada palabra
frecuencia = {}

#Contar la frecuencia de cada palabra
for palabra in palabras:
    palabra = palabra.lower()  # Convertir a minúsculas para evitar distinciones entre mayúsculas y minúsculas
    
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

# Mostrar la frecuencia de cada palabra
for palabra, conteo in frecuencia.items():
    print(f"La palabra '{palabra}' aparece {conteo} veces.")
