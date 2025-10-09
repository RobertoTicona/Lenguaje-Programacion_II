class Estudiante:
    def __init__(self, nombre, dni, codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo_estudiante = codigo_estudiante
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)
        curso.agregar_estudiante(self)

    def mostrar_informacion(self):
        print(f"Estudiante: {self.nombre} DNI: {self.dni} Código: {self.codigo_estudiante}")
        print("Cursos inscritos:")
        for curso in self.cursos:
            print(f"{curso.nombre_curso}")

class Profesor:
    def __init__(self, nombre, dni, especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Profesor: {self.nombre} DNI: {self.dni}, Especialidad: {self.especialidad}")

class Curso:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def mostrar_detalles(self):
        print(f"\nCurso: {self.nombre_curso}")
        self.profesor.mostrar_informacion()
        print("Estudiantes inscritos:")
        for est in self.estudiantes:
            print(f"  {est.nombre} ({est.codigo_estudiante})")

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_cursos(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        for curso in self.cursos:
            curso.mostrar_detalles()

prof1 = Profesor("Ing. Coyla Leonel", "01323043", "Programación")
prof2 = Profesor("Ing. Tito Jose", "02839212", "Programación")
prof3 = Profesor("Dr. Valvede Confesor", "02839312", "Estadística")
prof4 = Profesor("Ing. Torres Fred", "03987412", "Programación")
prof5 = Profesor("Ing. Roque Elvis", "94847311", "Estadística")
prof6 = Profesor("Ing. Rossel Luis", "83474711", "Programación")

curso1 = Curso("Lenguajes de Programación II", prof1)
curso2 = Curso("Sistema de gestión de base de datos", prof2)
curso3 = Curso("Modelos discretos", prof3)
curso4 = Curso("Programación numérica", prof4)
curso5 = Curso("Inferencia estadística", prof5)
curso6 = Curso("Análisis y diseños de sistemas de información", prof6)

est1 = Estudiante("Milena Kely", "01345621", "2025007")
est2 = Estudiante("Henry Quispe", "23345182", "2025089")

univ = Universidad("Universidad Nacional del Altiplano")
univ.agregar_cursos(curso1)
univ.agregar_cursos(curso2)

est1.inscribirse(curso1)
est1.inscribirse(curso2)
est1.inscribirse(curso3)
est1.inscribirse(curso4)
est1.inscribirse(curso5)
est1.inscribirse(curso6)
est2.inscribirse(curso2)

print(univ.nombre)
univ.mostrar_cursos()
est1.mostrar_informacion()
est2.mostrar_informacion()
