class Ladrillos:
    def __init__(self,longitud,altura,ancho):
        self.longitud = longitud
        self.altura = altura
        self.ancho = ancho

    def calcular(self):
        return (1 / ((self.longitud + 0.015) * (self.altura + 0.015)))

#Solicitar datos al usuario

longitud = float(input("Ingrese la longitud del ladrillo: "))
altura = float(input("Ingrese la altura del ladrillo: "))
ancho = float(input("Ingrese el ancho del ladrillo: "))

#Objeto

cantidad = Ladrillos(longitud,altura,ancho)

print("La cantidad de ladrillos en 1 metro^2 es: ",cantidad.calcular()," sin desperdicios")
print("La cantidad de ladrillos corregido en 1 metro^2 es: ", cantidad.calcular()*1.05, " con desperdicios")
print("La cantidad de ladrillos en 8.05 metros^2 es: ", cantidad.calcular()*1.05*8.05)
