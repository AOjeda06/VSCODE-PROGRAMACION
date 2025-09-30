#Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10 
# (utiliza 1 + Math.random()*10). Luego pedirá un valor N y mostrará cuántas veces aparece N. 

import random

#Lista para almacenar los números
numeros = []

#Rellenar la lista con 100 números enteros aleatorios entre 1 y 10
for i in range(100):
    num = int(1 + random.random() * 10)
    numeros.append(num)

#Pedir un valor N al usuario
N = int(input("Introduce un número entero entre 1 y 10: "))

#Contar cuántas veces aparece N en la lista
contador = 0
for num in numeros:
    if num == N:
        contador += 1

#Mostrar el resultado
print(f"El número {N} aparece {contador} veces en la lista.")