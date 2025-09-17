class Verificar:
    def __init__(self):
        pass

    def respuesta(self):
        print("Verificar si un número es nulo, par o impar")
        print("Escribe números o 'fin' para terminar")
        entrada = ""
        while entrada.lower() != "fin":
            entrada = input("Ingrese un número: ")
            if entrada.isdigit():
                if int(entrada) == 0:
                    print("Es nulo")
                elif int(entrada) % 2 == 0:
                    print("Es par")
                else:
                    print("Es impar")
            elif entrada.lower() != "fin":
                print("Entrada invalida: Escriba un número o 'fin' ")

def main():
    numeros = Verificar()
    numeros.respuesta()
if __name__=="__main__":
    main()
