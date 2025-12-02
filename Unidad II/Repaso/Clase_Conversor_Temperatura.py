class ConversorTemperatura:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
        
    def celsius_a_fahrenheit(self, c):
        return (c * 9/5) + 32

    def desde_celsius(self, c):
        f = self.celsius_a_fahrenheit(c)
        return ConversorTemperatura(f)

def main():
    conversor = ConversorTemperatura(0)     
    t1 = conversor.desde_celsius(25)        
    print("Temperatura en Fahrenheit:", t1.fahrenheit)

if __name__ == "__main__":
    main()
