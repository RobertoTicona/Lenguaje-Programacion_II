import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def mostrar_informacion(self):
        print(f"El radio del circulo es: {self.radio}")
        print(f"El área es: {self.calcular_area():.2f}")
        print(f"El perímetro es: {self.calcular_perimetro():.2f}")

circulo = Circulo(7)
circulo.mostrar_informacion()
