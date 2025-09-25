class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

def main():
    miPersona = Persona("Roberto")
    miPersona2 = Persona("Maria")
    miPersona.saludar()
    miPersona2.saludar()

if __name__=="__main__":
    main()
