class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

operacion = Rectangulo(5, 6)

print("Área: ", operacion.area())
print("Perímetro: ", operacion.perimetro())
