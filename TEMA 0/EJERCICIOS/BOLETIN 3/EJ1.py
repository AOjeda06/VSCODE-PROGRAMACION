#Diseñar la clase CuentaCorriente, que almacena los datos DNI, nombre y el saldo. 
#Añade los siguientes constructores:
#   Con el DNI del titular de la cuenta y un saldo inicial. El nombre se inicializará a cadena vacía.
#   Con el DNI, nombre y el saldo inicial.
#Las operaciones típicas de una cuenta corriente son:
#   Sacar dinero: el método debe indicar si ha sido posible llevar a cabo la operación, si existe saldo suficiente. 
#       Si es posible llevar a cabo la operación se resta la cantidad a sacar al saldo de la cuenta.
#   Ingresar dinero: se incrementa el saldo.
#   Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos cuentas corrientes son iguales si tienen el 
#       mismo DNI. Las cuentas corrientes se ordenarán de menor a mayor por el saldo.

class CuentaCorriente:
    # Constructor con DNI y saldo inicial, nombre vacío
    def __init__(self, dni, nombre="", saldo=0.0):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo

    # Constructor con DNI, nombre y saldo inicial
    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo

    # Operación para sacar dinero
    def sacar_dinero(self, cantidad):
        res = False
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            res = True
        return res
    
    # Operación para ingresar dinero
    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad

    # toString
    def __str__(self):
        return f"CuentaCorriente(DNI: {self.dni}, Nombre: {self.nombre}, Saldo: {self.saldo:.2f})"

    # equals
    def __eq__(self, other):
        eq = False
        if isinstance(other, CuentaCorriente):
            eq = self.dni == other.dni and self.nombre == other.nombre and self.saldo == other.saldo
        return eq

    # less than
    def __lt__(self, other):
        menor = False
        if self.saldo < other.saldo:
            menor = True
        return menor
