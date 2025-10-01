class Producto:
    # Constructor
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Método para calcular el precio total por una cantidad dada
    def calcular(self, cantidad):
        return self.precio * cantidad
    
    #toString
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"
    
    #less than (por precio)
    def __lt__(self, other):
        return self.precio < other.precio