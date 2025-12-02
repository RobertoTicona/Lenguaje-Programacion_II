import math
class Figura:
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return ((self.base * self.altura) / 2)
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

def main():
    figuras = [Rectangulo(4,5), Circulo(3), Triangulo(5,2)]

    for figura in figuras:
        print(f"Área : {figura.area():.2f}")

if __name__=="__main__":
    main()
