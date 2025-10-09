class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print("Libro creado")

    def mostrar_info(self):
        print(f"Libro {self.titulo} escritó por {self.autor} en el año {self.anio}")

    def __del__(self):
        print("Objeto destruido")
        
def main():
    titulo = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    an = int(input("Ingrese el año del libro: "))
    miLibro = Libro(titulo,autor,an)
    miLibro.mostrar_info()
if __name__=="__main__":
    main()
