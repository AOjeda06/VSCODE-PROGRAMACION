from Empleado import Empleado

class Directivo(Empleado):
    # Constructor
    def __init__(self, nombre):
        super().__init__(nombre)

    # toString
    def __str__(self):
        return f"Empleado: {self.nombre} -> Directivo"