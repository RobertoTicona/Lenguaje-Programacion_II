from typing import TypeVar, Generic
import math

T = TypeVar('T', int, float)

class Triangulo(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def hipotenusa(self) -> float:
        a = int(self.a)
        b = int(self.b)
        if a < 0 or b < 0:
            raise ValueError("Los catetos deben ser positivos")
        return math.sqrt(a ** 2 + b **2)

    def area(self) -> float:
        a = int(self.a)
        b = int(self.b)
        return a * b / 2

    def perimetro(self) -> float:
        return self.a + self.b + self.hipotenusa()

def main():
    try:
        a = float(input("Ingrese cateto a: "))
        b = float(input("Ingrese cateto b: "))
        triangulo = Triangulo(a, b)
        print(f"Lado a es {triangulo.a}")
        print(f"Lado b es {triangulo.b}")
        print(f"La hipotenusa es {triangulo.hipotenusa()}")
        print(f"El área es {triangulo.area()}")
        print(f"El perimetro es {triangulo.perimetro()}")

    except ValueError as e:
        print(f"Error {e}")

if __name__=="__main__":
    main()
