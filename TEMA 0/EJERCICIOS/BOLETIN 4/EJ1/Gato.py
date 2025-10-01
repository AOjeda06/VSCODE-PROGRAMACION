from Animal import Animal

class Gato (Animal):
    # Constructor
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    # Hablar
    def hablar(self):
        return "Miau"
    
    # toString
    def __str__(self):
        return f"Soy un gato y {super().__str__()}"