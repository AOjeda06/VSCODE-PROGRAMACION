from Producto import Producto

class Perecedero(Producto):
    # Constructor
    def __init__(self, nombre, precio, dias):
        super().__init__(nombre, precio)
        self.dias = dias

    # Método para calcular el precio total con descuento según los días restantes
    def calcular(self, cantidad):
        if self.dias == 1:
            descuento = 4
        elif self.dias == 2:
            descuento = 3
        elif self.dias == 3:
            descuento = 2
        else:
            descuento = 1
        return super().calcular(cantidad) / descuento