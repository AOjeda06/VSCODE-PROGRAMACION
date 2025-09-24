#Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos.
#Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.

def mostrar_numeros_entre(a, b):
    if a > b:
        a, b = b, a  # Intercambiar valores si a es mayor que b
    for num in range(a + 1, b):
        print(num)
#Ejemplo de uso
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
mostrar_numeros_entre(num1, num2)