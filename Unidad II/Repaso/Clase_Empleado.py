class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, dias):
        Empleado.__init__(self, nombre, 0)
        self.dias = dias

    def calcular_pago(self):
        self.salario = 60 * self.dias
        return self.salario


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, dias, horas):
        Empleado.__init__(self, nombre, 0)
        self.dias = dias
        self.horas = horas

    def calcular_pago(self):
        self.salario = 5 * self.dias * self.horas
        return self.salario

def main():
    empleados = [
        EmpleadoTiempoCompleto("Juan", 20),
        EmpleadoPorHoras("Ana", 10, 6),
        EmpleadoTiempoCompleto("Luis", 15),
        EmpleadoPorHoras("María", 12, 4)
    ]

    for emp in empleados:
        print(emp.nombre, "-> Pago:", emp.calcular_pago())

if __name__=="__main__":
    main()
