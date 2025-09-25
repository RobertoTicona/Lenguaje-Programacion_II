class Hipotenusa:
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2

    def hipotenusa(self):
        return (self.cateto1 ** 2 + self.cateto2 ** 2) ** 0.5

    def mostrar(self):
        print(f"La hipotenusa de {self.cateto1} y {self.cateto2} es {self.hipotenusa()}")

hipotenusa = Hipotenusa(3,4)
hipotenusa.mostrar()
