class Operaciones:
    def Sumar(self, a, b, c = None):
        if c is not None:
            return a + b + c
        else:
            return a + b

objeto = Operaciones()
suma = objeto.Sumar(1,2,0)
suma2 = objeto.Sumar(1,2)
print(suma)
print(suma2)
