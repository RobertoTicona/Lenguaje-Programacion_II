class NumeroNatural:
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"Número natural: {self.valor}")

def main():

    i = 1
    while i <= 10:
        numero = NumeroNatural(i)
        numero.mostrar()
        i += 1

if __name__=="__main__":
    main()
