#Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

import random
lista = [random.randint(1, 100) for _ in range(10)]
print(lista)