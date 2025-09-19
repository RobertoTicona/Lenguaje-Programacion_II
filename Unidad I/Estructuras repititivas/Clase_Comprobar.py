class Comprobar:
    def __init__(self):
        pass

    def rpta(self):
        print("Verificar números")
        entrada = int(input("Ingrese un número: "))
        while entrada > 0 and entrada <= 10:
            print(f"El número {entrada} está en el rango (1-10)")
            entrada = int(input("Ingrese otro número (fuera de 1-10) para salir: "))

def main():
    numeros = Comprobar()
    numeros.rpta()

if __name__=="__main__":
    main()



