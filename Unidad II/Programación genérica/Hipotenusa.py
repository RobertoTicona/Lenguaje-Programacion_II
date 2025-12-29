from typing import TypeVar
import math

T = TypeVar('T', int, float)

def calcular_hipotenusa(cateto_a : T, cateto_b : T):
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)

def main():
    a = float(input("Ingrese cateto a: "))
    b = float(input("Ingrese cateto b: "))
    h = calcular_hipotenusa(a, b)
    print(f"La hipotenusa es {h}")

if __name__=="__main__":
    main()
