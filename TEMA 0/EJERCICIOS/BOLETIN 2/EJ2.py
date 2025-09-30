#Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.

#Función para calcular el máximo
def maximo(a, b):
    resultado = a if a > b else b
    return resultado

#Función para calcular el mínimo
def minimo(a, b):
    resultado = a if a < b else b
    return resultado

#Lista para almacenar los números
numeros = []

#Pedir 10 números reales al usuario
for i in range(10):
    num = float(input("Introduce un número real: "))
    numeros.append(num)

#Inicializar máximo y mínimo con el primer número de la lista
max_num = numeros[0]
min_num = numeros[0]

#Recorrer la lista para encontrar el máximo y mínimo
for num in numeros:
    max_num = maximo(max_num, num)
    min_num = minimo(min_num, num)
    
#Mostrar los resultados
print("El número máximo es:", max_num)
print("El número mínimo es:", min_num)