class Empleado:
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Getters y Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    # toString
    def __str__(self):
        return f"Empleado: {self.nombre}"