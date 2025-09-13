class Estadistica:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.datos = []

    def promedio(self):
        suma = 0
        for i in range(1, self.cantidad + 1):
            dato = float(input(f"Dato {i}: "))
            self.datos.append(dato)
            suma += dato

        return suma / self.cantidad

    def varianza1P(self):
        prom = sum(self.datos) / self.cantidad
        suma_dif = 0
        for x in self.datos:
            suma_dif += (x - prom) ** 2
        return suma_dif / self.cantidad

    def varianza2P(self):
        suma = sum(self.datos)
        suma_cuadrados = 0
        for z in self.datos:
            suma_cuadrados += z ** 2
        return (suma_cuadrados - (suma ** 2) / self.cantidad) / self.cantidad

    def varianza1M(self):
        prom = sum(self.datos) / self.cantidad
        suma_dif = 0
        for x in self.datos:
            suma_dif += (x - prom) ** 2
        return suma_dif / (self.cantidad - 1)

    def varianza2M(self):
        suma = sum(self.datos)
        suma_cuadrados = 0
        for z in self.datos:
            suma_cuadrados += z ** 2
        return (suma_cuadrados - (suma ** 2) / self.cantidad) / (self.cantidad - 1)
        
def main():
    
    cant = int(input("Ingrese la cantidad de datos: "))
    misCalculos = Estadistica(cant)
    promedio = misCalculos.promedio()
    
    varianza1 = misCalculos.varianza1P()
    varianza2 = misCalculos.varianza2P()
    varianza1M = misCalculos.varianza1M()
    varianza2M = misCalculos.varianza2M()
    
    print(f"El Promedio es: {promedio}")
    print(f"La Varianza Poblacional calculada con la formula 1 es: {varianza1}")
    print("Su Desviación Estándar es: ", varianza1 ** (1/2))
    print(f"La Varianza Poblacional calculada con la formula 2 es: {varianza2}")
    print("Su Desviación Estándar es: ", varianza2 ** (1/2))
    print(f"La Varianza Muestral calculada con la formula 1 es: {varianza1M}")
    print("Su Desviación Estándar es: ", varianza1 ** (1/2))
    print(f"La Varianza Muestral calculada con la formula 2 es: {varianza2M}")
    print("Su Desviación Estándar es: ", varianza2 ** (1/2))

if __name__=="__main__":
    main()
