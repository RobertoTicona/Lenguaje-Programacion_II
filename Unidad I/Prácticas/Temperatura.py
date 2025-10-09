class Temperatura:
    def __init__(self, fahrenheit, celsius):
        self.__fahrenheit = fahrenheit
        self.__celsius = celsius

    def get_fahrenheit(self):
        return self.__fahrenheit

    def get_celsius(self):
        return self.__celsius

    def set_fahrenheit(self, nuevo_temp):
        if nuevo_temp > 0:
            self.__fahrenheit = nuevo_temp
        else:
            print("Temperatura invalida")

    def set_celsius(self, nuevo_c):
        if nuevo_c > 0:
            self.__celsius = nuevo_c
        else:
            print("Temperatura invalida")

    def calcular(self):
        return ((self.__fahrenheit - 32) * 5) / 9

    def calcular2(self):
        return ((self.__celsius * (9/5)) + 32)

def main():
    dato = float(input("Ingrese la temperatura en grados fahrenheit: "))
    dato2 = float(input("Ingrese otra temperatura en grados celsius: "))
    temperatura = Temperatura(dato,dato2)
    print("La temperatura en grados celcius es: ", temperatura.calcular())
    print("La temperatura en grados fahrenheit es: ", temperatura.calcular2())

if __name__=="__main__":
    main()
