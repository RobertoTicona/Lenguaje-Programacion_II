import math
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Subclases deben implementar este método")

    def perimetro(self):
        raise NotImplementedError("Subclases deben implementar este método")

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura


    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

circulo = Circulo(5)
print(f"Nombre: {circulo.nombre}")
print(f"Área: {circulo.area():.2f}")
print(f"Perímetro: {circulo.perimetro():.2f}")
rectangulo = Rectangulo(8,6)
print(f"Nombre: {rectangulo.nombre}")
print(f"Área: {rectangulo.area()}")
print(f"Perímetro: {rectangulo.perimetro()}")
