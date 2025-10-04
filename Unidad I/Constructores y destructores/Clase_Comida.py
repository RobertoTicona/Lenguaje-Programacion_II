class Comida:
    def __init__(self, proteinas, carbohidratos, grasas):
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas
        print("Comida creada")
        print(f"{self.proteinas} g. {self.carbohidratos} g. {self.grasas} g.")

    def calcular_calorias(self):
        calorias = self.proteinas * 4 + self.carbohidratos * 4 + self.grasas * 4
        return calorias

    def mostrar_informacion(self):
        print("INFORMACIÓN NUTRICIONAL")
        print(f"Proteínas: {self.proteinas} g.")
        print(f"Carbohidratos: {self.carbohidratos} g.")
        print(f"Grasas: {self.grasas} g.")
        print(f"Calorías totales: {self.calcular_calorias()} kcal.")

prot = float(input("Ingrese gramos de proteinas: "))
carb = float(input("Ingrese gramos de carbohidratos: "))
lip = float(input("Ingrese gramos de lípidos: "))

almuerzo = Comida(prot, carb, lip)
almuerzo.mostrar_informacion()

del almuerzo

try:
    almuerzo.mostrar_informacion()
except:
    print("Objeto almuerzo eliminado")
