from Producto import Producto

class NoPerecedero(Producto):
    # Constructor
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    # Método para calcular el precio total sin descuento
    def calcular(self, cantidad):
        return super().calcular(cantidad)