#Crea una clase llamada Articulo con los siguientes atributos: nombre, precio (sin IVA), iva (siempre será 21) y 
# cuantosQuedan (representa cuántos quedan en el almacén).
#Añade los siguientes métodos:
#   Constructor con 3 parámetros que asigne valores a nombre, precio y cuantosQuedan. El IVA siempre lo pondrá a 21.
#   Método getPVP que devuelva el precio de venta al público (PVP) con iva incluido. 
#   Método getPVPDescuento que devuelva el PVP con un descuento pasado como argumento. 
#   Método vender que actualiza los atributos del objeto tras vender una cantidad ‘x’ (si es posible). Devolverá true si ha 
#       sido posible (false en caso contrario). La cantidad a vender se pasará como argumento al método.
#   Método almacenar que actualiza los atributos del objeto tras almacenar una cantidad ‘x’. La cantidad a almacenar se pasará
#        como argumento.
#   Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  artículos son iguales si tienen el mismo nombre. 
#       Los artículos se ordenarán de menor a mayor por el nombre.

class Articulo:
    # Constructor con 3 parámetros
    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.iva = 21
        self.cuantosQuedan = cuantosQuedan

    # Método para obtener el PVP con IVA incluido
    def getPVP(self):
        return (self.precio * (1 + self.iva / 100))

    # Método para obtener el PVP con descuento
    def getPVPDescuento(self, descuento):
        return ((self.getPVP()) * (1 - descuento / 100))

    # Método para vender una cantidad 'x'
    def vender(self, cantidad):
        exito = False
        if cantidad <= self.cuantosQuedan:
            self.cuantosQuedan -= cantidad
            exito = True
        return exito

    # Método para almacenar una cantidad 'x'
    def almacenar(self, cantidad):
        self.cuantosQuedan += cantidad

    # toString
    def __str__(self):
        return f"Artículo(Nombre: {self.nombre}, Precio sin IVA: {self.precio:.2f}, IVA: {self.iva}%, Cuántos quedan: {self.cuantosQuedan})"

    # equals
    def __eq__(self, other):
        eq = False
        if isinstance(other, Articulo):
            eq = self.nombre == other.nombre
        return eq

    # less than
    def __lt__(self, other):
        menor = False
        if self.nombre < other.nombre:
            menor = True
        return menor