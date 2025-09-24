#Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
# Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, 
# antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.

suma = 0
num = int(input("Ingrese un número entero positivo (o un número negativo para terminar): "))
while num >= 0:
    suma += num
    num = int(input("Ingrese un número entero positivo (o un número negativo para terminar): "))
print(f"La suma de los números positivos introducidos es: {suma}")
