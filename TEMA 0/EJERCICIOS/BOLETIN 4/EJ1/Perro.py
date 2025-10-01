from Animal import Animal
class Perro (Animal):
    # Constructor
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    # Hablar
    def hablar(self):
        return "Guau"
    
    # toString
    def __str__(self):
        return f"Soy un perro y {super().__str__()}"