class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def agregarDepartamento(self, departamento):
        self.departamentos.append(departamento)

dep1 = Departamento("Ingeniería Estadística")
dep2 = Departamento("Informática")

uni = Universidad("Universidad Nacional del Altiplano")

uni.agregarDepartamento(dep1)
uni.agregarDepartamento(dep2)

for d in uni.departamentos:
    print(d.nombre)
