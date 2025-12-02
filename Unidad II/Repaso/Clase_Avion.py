class Vehiculo:
    def acelerar(self):
        print("El vehículo esta acelerando")

class Volador:
    def volar(self):
        print("Estamos volando")

class Avion(Vehiculo, Volador):
    pass

def main():
    avion1 = Avion()
    avion1.acelerar()
    avion1.volar()

if __name__ == "__main__":
    main()
