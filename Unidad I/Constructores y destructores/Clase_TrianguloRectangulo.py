import math
class TrianguloRectangulo:
    def __init__(self, cateto_a, cateto_b):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b

    def calcular_hipotenusa(self):
        hipotenusa = math.sqrt(self.cateto_a ** 2 + self.cateto_b **2)
        return hipotenusa

    def __del__(self):
        print("Objeto TrianguloRectangulo destruido")

def main():
    try:
        cateto1 = float(input("Ingrese el valor del primer cateto: "))
        cateto2 = float(input("Ingrese el valor del segundo cateto: "))

        triangulo = TrianguloRectangulo(cateto1, cateto2)
        resultado = triangulo.calcular_hipotenusa()
        print(f"La hipotenusa del triángulo es {resultado:.2f}")
    except NameError:
        print("El objeto triangulo ya no existe (fue destruido)")
if __name__=="__main__":
    main()
