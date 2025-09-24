#Pedir dos números y mostrarlos ordenados de menor a mayor.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 < num2:
    print(f"Números ordenados de menor a mayor: {num1}, {num2}")
else:
    print(f"Números ordenados de menor a mayor: {num2}, {num1}")