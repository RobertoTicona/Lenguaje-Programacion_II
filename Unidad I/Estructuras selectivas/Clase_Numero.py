class Numero:
    def __init__(self,valor):
        self.valor = valor

    def clasificar(self):
        if self.valor == 0:
            return "Nulo"
        elif self.valor % 2 == 0:
            return "Par"
        else:
            return "Impar"

ejemplos = [Numero(0), Numero(2), Numero(5)]

for num in ejemplos:
    tipo = num.clasificar()
    print(f"El número {num.valor} es {tipo}")
