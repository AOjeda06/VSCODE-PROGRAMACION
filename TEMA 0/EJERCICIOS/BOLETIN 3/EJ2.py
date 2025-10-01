#Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca. La 
# clase debe guardar el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados. 
# La clase contendrá los siguientes métodos:
#   Constructor con todos los parámetros (se le indica valores para todos los atributos).
#   prestamo(): incrementa el atributo correspondiente cada vez que se realice un préstamo. No 
#        se pueden prestar libros si no quedan ejemplares disponibles para prestar. Devuelve true si se ha podido realizar el préstamo y false en caso contrario.
#   devolucion(): decrementa el atributo correspondiente cada vez que se devuelva un libro. No 
#       se podrán devolver libros que no se hayan prestado. Devuelve true si se ha podido realizar la operación y false en caso contrario.
#   Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  libros son iguales 
#       si tienen el mismo título y el mismo autor. Los libros se ordenarán de menor a mayor por el nombre del autor.

class Libro:
    # Constructor con todos los parámetros
    def __init__(self, titulo, autor, num_ejemplares, num_prestados):
        self.titulo = titulo
        self.autor = autor
        self.num_ejemplares = num_ejemplares
        self.num_prestados = num_prestados

    # Método para realizar un préstamo
    def prestamo(self):
        exito = False
        if self.num_prestados < self.num_ejemplares:
            self.num_prestados += 1
            exito = True
        return exito

    # Método para realizar una devolución
    def devolucion(self):
        exito = False
        if self.num_prestados > 0:
            self.num_prestados -= 1
            exito = True
        return exito

    # toString
    def __str__(self):
        return f"Libro(Título: {self.titulo}, Autor: {self.autor}, Ejemplares: {self.num_ejemplares}, Prestados: {self.num_prestados})"

    # equals
    def __eq__(self, other):
        eq = False
        if isinstance(other, Libro):
            eq = self.titulo == other.titulo and self.autor == other.autor
        return eq

    # less than
    def __lt__(self, other):
        menor = False
        if self.autor < other.autor:
            menor = True
        return menor