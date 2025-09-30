#Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
# Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor
#  o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).

import random
numero_secreto = random.randint(1, 100)
print("¡Bienvenido al juego del número secreto!")
print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")
intento = int(input("Introduce tu número (o -1 para rendirte): "))
while intento != -1 and intento != numero_secreto:
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    intento = int(input("Introduce tu número (o -1 para rendirte): "))
if intento == -1:
    print(f"Te has rendido. El número secreto era {numero_secreto}.")
else:
    print(f"¡Felicidades! Has acertado el número secreto {numero_secreto}")
