class SumaNaturales:
    def __init__(self, limite):
        self.limite = limite
        self.suma = 0

    def calcularSuma(self):
        for i in range (1, self.limite + 1):
            self.suma = self.suma + i
        return self.suma

def main():

    miSuma = SumaNaturales(10)
    resultado = miSuma.calcularSuma()
    print(f"La suma de los primeros {miSuma.limite} números naturales es {resultado}")

if __name__=="__main__":
    main()
