class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        print("Objeto Temperatura creado")

    def a_fahrenheit(self):
            f = self.celsius * (9 / 5) + 32
            return f

    def __del__(self):
            print("Objeto Temperatura destruido")

def main():
    cel = float(input("Ingrese la temperatura en grados Celsius: "))
    temp = Temperatura(cel)
    rpta = temp.a_fahrenheit()
    print(f"Temperatura en grados fahrenheit: {rpta}")

if __name__=="__main__":
    main()
