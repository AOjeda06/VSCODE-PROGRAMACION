# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")
    