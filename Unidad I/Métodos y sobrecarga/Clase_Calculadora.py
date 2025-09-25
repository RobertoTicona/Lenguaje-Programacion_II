class Calculadora:
    def sumar(self, a, b):
        self.a = a
        self.b = b
        return a + b

miCalculadora = Calculadora()
suma = miCalculadora.sumar(1,3)
print(f"La suma de {miCalculadora.a} y {miCalculadora.b} es {suma}")
