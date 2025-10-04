import gc
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado {self.titulo} de {self.autor} - {self.anio}")

    def mostrar_informacion(self):
        print(f"{self.titulo} fue escrito por {self.autor} en el año {self.anio}")

    def __del__(self):
        print(f"Libro {self.titulo} eliminado")

libros_datos = [("Cien años de soledad", "Gabriel García Marquez", 1967),
                ("1984", "George Orweli", 1949),
                ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)]

biblioteca = []

for datos in libros_datos:
    libro = Libro(*datos)
    libro.mostrar_informacion()
    biblioteca.append(libro)

biblioteca.clear()
del libro
gc.collect()
print("Fin de programa")
