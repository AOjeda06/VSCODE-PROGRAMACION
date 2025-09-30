#Realiza un programa que pida 8 números enteros y los almacene en una lista. A continuación, recorrerá esa tabla y mostrará 
# esos números junto con la palabra “par” o “impar” según proceda.

#Lista para almacenar los números
numeros = []

#Pedir 8 números enteros al usuario
for i in range(8):
    num = int(input("Introduce un número entero: "))
    numeros.append(num)

#Recorrer la lista y mostrar si cada número es par o impar
for num in numeros:
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")
