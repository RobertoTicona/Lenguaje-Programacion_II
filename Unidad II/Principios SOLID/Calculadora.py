#Principio S
class CalculadoraExtensible:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método a calcular")

#Principio O y L
class Suma(CalculadoraExtensible):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        print(f"La suma es {self.a + self.b}")

class Resta(CalculadoraExtensible):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        print(f"La resta es {self.a - self.b}")

class Producto(CalculadoraExtensible):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        print(f"La multiplicación es {self.a * self.b}")

class Cociente(CalculadoraExtensible):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def respuesta(self):
        print(f"La división es {self.a / self.b}")

#Principio D
class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        self.calculadora.respuesta()

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    suma = Suma(num1, num2)
    resta = Resta(num1, num2)
    mul = Producto(num1, num2)
    div = Cociente(num1, num2)
    app1 = Aplicacion(suma)
    app1.ejecutar()
    app2 = Aplicacion(resta)
    app2.ejecutar()
    app3 = Aplicacion(mul)
    app3.ejecutar()
    app4 = Aplicacion(div)
    app4.ejecutar()

if __name__=="__main__":
    main()
