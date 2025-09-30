#Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.

#Lista para almacenar los números
numeros = []

#Pedir 10 números al usuario
for i in range(10):
    num = int(input("Introduce un número entero: "))
    numeros.append(num)

#Ordenar la lista de mayor a menor
numeros.sort(reverse=True)

#Mostrar los números ordenados
print("Números ordenados de mayor a menor:")
for num in numeros:
    print(num)