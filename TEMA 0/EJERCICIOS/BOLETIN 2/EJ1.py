#Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

import random

# Crear y rellenar la lista con números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(10)]

# Mostrar la lista
print(lista)