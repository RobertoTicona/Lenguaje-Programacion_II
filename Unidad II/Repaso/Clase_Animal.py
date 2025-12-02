from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")


def main():
    animales = [Perro(), Gato(), Perro()]

    for animal in animales:
        animal.hacer_sonido()

if __name__ == "__main__":
    main()
