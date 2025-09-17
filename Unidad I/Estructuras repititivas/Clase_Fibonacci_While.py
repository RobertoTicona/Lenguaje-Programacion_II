class Fibonacci:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.a = 0
        self.b = 1
        self.contador = 0

    def generarSerie(self):
        print(f"Serie de Fibonacci")
        while self.contador < self.cantidad:
            print(self.a, end = " ")
            c = self.a + self.b
            self.a = self.b
            self.b = c
            self.contador += 1

def main():
    cant = int(input("Ingrese una cantidad: "))
    miFibonacci = Fibonacci(cant)
    miFibonacci.generarSerie()
if __name__=="__main__":
    main()
