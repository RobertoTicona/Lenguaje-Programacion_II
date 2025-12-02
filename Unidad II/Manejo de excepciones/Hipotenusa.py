import math

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)

def main():
    try:
        a = float(input("Ingrese el valor del cateto a: "))
        b = float(input("Ingrese el valor del cateto b: "))
        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser números positivos")
        hipotenusa = calcular_hipotenusa(a, b)
        print(f"La hipotenusa es: {hipotenusa:.2f}")
    except ValueError as ve:
        print("Error", ve)
    except Exception as e:
        print("Ocurrio un error inesperado", e)

if __name__=="__main__":
    main()
