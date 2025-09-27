class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - S/. {self.precio:.2f} stock: {self.stock}"

    def __eq__(self,otra):
        return self.nombre = otra.nombre

    def __add__(self,otra):
        return self.precio + otra.precio

prod1 = Producto("Arroz",3.50,20)
prod2 = Producto("Arroz",3.50,15)
prod3 = Producto("Azúcar",4.00,10)

print(prod1)
print(prod2)
print(prod3)

print(prod1 == prod2)
print(prod1 == prod3)

print("Suma de precios: ", prod1 + prod2)
