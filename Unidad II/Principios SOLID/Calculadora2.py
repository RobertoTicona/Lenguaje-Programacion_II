# ===============================
# EJEMPLO SOLID – CALCULADORA
# ===============================

# -------- Principio I --------
# Interfaz pequeña y específica
class Operacion:
    def respuesta(self):
        raise NotImplementedError("Debe implementar el método respuesta")


# -------- Principio S --------
# Cada clase tiene una sola responsabilidad
class Suma(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        print(f"La suma es {self.a + self.b}")


class Resta(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        print(f"La resta es {self.a - self.b}")


class Producto(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        print(f"La multiplicación es {self.a * self.b}")


class Cociente(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        if self.b == 0:
            print("Error: división entre cero")
        else:
            print(f"La división es {self.a / self.b}")


# -------- Principio D --------
# La aplicación depende de la abstracción, no de la clase concreta
class Aplicacion:
    def __init__(self, operacion: Operacion):
        self.operacion = operacion

    def ejecutar(self):
        self.operacion.respuesta()


# -------- Programa principal --------
def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    operaciones = [
        Suma(num1, num2),
        Resta(num1, num2),
        Producto(num1, num2),
        Cociente(num1, num2)
    ]

    for op in operaciones:
        app = Aplicacion(op)
        app.ejecutar()


if __name__ == "__main__":
    main()
