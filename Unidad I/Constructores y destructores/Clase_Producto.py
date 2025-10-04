import gc
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"\nProducto registrado {self.nombre} - $. {self.precio:.2f} en stock {self.cantidad}")

    def mostrar_informacion(self):
        print(f"{self.nombre} precio en $. {self.precio:.2f} en stock {self.cantidad}")

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")

producto_datos = [("Manzana", 0.5, 100),
                  ("Pan", 0.3, 50),
                  ("Leche", 3.5, 30)]

inventario = []

for datos in producto_datos:
    producto = Producto(*datos)
    producto.mostrar_informacion()
    inventario.append(producto)

inventario.clear()
del producto
gc.collect()
print("Fin de programa")
