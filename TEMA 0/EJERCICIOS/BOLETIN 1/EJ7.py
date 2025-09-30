#Realiza un programa que pida un número entero positivo y nos diga si es primo o no.

num = int(input("Introduce un número entero positivo: "))
if num < 2:
    print(f"{num} no es un número primo.")
else:
    es_primo = True
    i = 2
    #Explicación: un número no es primo si tiene divisores distintos de 1 y de sí mismo. Basta con comprobar hasta la raíz cuadrada del número.
    while i <= int(num**0.5): #**0.5 es la raíz cuadrada
        if num % i == 0:
            es_primo = False
        i += 1
    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")