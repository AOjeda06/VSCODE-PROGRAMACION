class Animal:

    # Constructor
    def __init__(self, nombre, numero_patas):
        self.nombre = nombre
        self.numero_patas = numero_patas

    # Hablar
    def hablar(self):
        return ""
    
    # toString
    def __str__(self):
        return f"Me llamno {self.nombre}, tengo {self.numero_patas} patas y sueno así: {self.hablar()}"