import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        print("Objeto circulo creado")

    def calcularArea(self):
        area = math.pi * self.radio ** 2
        return area

radio_usuario = float(input("Ingrese el radio del circulo: "))
circulo = Circulo(radio_usuario)
rpta = circulo.calcularArea()
print(f"El área del circulo con radio {circulo.radio} es {rpta:.2f}")

del circulo

try:
    print(circulo)
except NameError:
    print("El objeto fue finiquitado")
