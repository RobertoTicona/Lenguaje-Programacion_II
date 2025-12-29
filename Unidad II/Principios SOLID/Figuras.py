import math
#Principio S
class CalcularFiguras:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método a calcular")

#Principio O y L
class Rectangulo(CalcularFiguras):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        rpt = self.base * self.altura
        print(f"Área del rectángulo es {rpt}")

    def perimetro(self):
        rpt2 = 2 * (self.base + self.altura)
        print(f"Perímetro del rectángulo es {rpt2}")

class Circulo(CalcularFiguras):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        rpt = math.pi * self.radio ** 2
        print(f"Área del circulo es {rpt:.2f}")

    def perimetro(self):
        rpt2 = 2 * math.pi * self.radio
        print(f"Perímetro del círculo es {rpt2:.2f}")

#Principio D
class Aplicacion:
    def __init__(self, figura):
        self.figura = figura

    def ejecutar(self):
        self.figura.area()
        self.figura.perimetro()

base = int(input("Ingrese la base del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))
radio = int(input("Ingrese el radio del circulo: "))
rec = Rectangulo(base,altura)
app = Aplicacion(rec)
app.ejecutar()
cir = Circulo(radio)
app2 = Aplicacion(cir)
app2.ejecutar()
