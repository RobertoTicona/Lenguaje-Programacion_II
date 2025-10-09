class IMC:
    def __init__(self, peso, talla):
        self.peso = peso
        self.talla = talla

    def calculo(self):
        return self.peso / self.talla ** 2

    def clasificar(self):
        if self.calculo() <= 18.5:
            return "Bajo peso"
        elif self.calculo() <= 24.9:
            return "Normal"
        elif self.calculo() <= 29.9:
            return "Sobrepeso"
        elif self.calculo() <= 34.9:
            return "Obesidad grado I"
        elif self.calculo() <= 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III"

def main():
    peso = float(input("Ingrese su peso en kilogramos: "))
    talla = float(input("Ingrese su talla en metros: "))
    persona1 = IMC(peso,talla)
    rpta = persona1.calculo()
    categoria = persona1.clasificar()
    print(f"Su IMC es {rpta:.2f} - {categoria}")
if __name__=="__main__":
    main()
