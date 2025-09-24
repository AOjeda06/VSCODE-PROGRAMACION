#Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
#   *
#  * *
# * * *
#* * * *

n = int(input("Introduce un número entero positivo: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i) # n-1 espacios (" ") y i asteriscos (* )
