class Animal: # clase base
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        pass

class Perro(Animal): # clase derivada
    def hacerSonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacerSonido(self):
        return "¡Miauuu!"

perro = Perro("Rex")
print(f"{perro.nombre} dice {perro.hacerSonido()}")

gato = Gato("Charlotte")
print(f"{gato.nombre} dice {gato.hacerSonido()}")
