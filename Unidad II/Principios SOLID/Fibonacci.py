#Principio S
class CalcularFibonacci:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método a calcular")

#Principio O y L
class Fibonacci(CalcularFibonacci):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        a = 0
        b = 1
        for i in range(1, self.numero + 1):
            print(a)
            c = a + b
            b = a
            a = c

#Principio D
class Aplicacion:
    def __init__(self, fibonacci):
        self.fibonacci = fibonacci

    def ejecutar(self):
        self.fibonacci.calcular()
        
fib = Fibonacci(10)
app = Aplicacion(fib)
app.ejecutar()
