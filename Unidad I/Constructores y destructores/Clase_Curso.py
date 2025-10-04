import gc
class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"\nCurso {self.nombre} registrado | Código {self.codigo} | Docente {self.profesor}")

    def mostrar_informacion(self):
        print(f"Curso {self.nombre} con código {self.codigo} y docente {self.profesor}")

    def __del__(self):
        print(f"Curso {self.nombre} finiquitado")

alumnos_datos = [("Sistemas de gestión de base de datos I", "EST304", "Jose Panfilo Tito Lipa"),
                 ("Lenguajes de programación II", "EST305", "Leonel Coyla Idme"),
                 ("Programación numérica", "EST207", "Fred Torres Cruz"),
                 ]

registros = []

for datos in alumnos_datos:
    curso = Curso(*datos)
    curso.mostrar_informacion()
    registros.append(curso)

registros.clear()
del curso
gc.collect()
print("Fin de programa")
