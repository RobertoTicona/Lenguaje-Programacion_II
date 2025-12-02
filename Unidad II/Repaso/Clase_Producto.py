class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def set_nombre(self, nuevoN):
        self.__nombre = nuevoN
        return self.__nombre

    def set_precio(self, nuevoP):
        if nuevoP > 0:
            self.__precio = nuevoP
        else:
            print("No puede ser negativo")

    def descuento(self, descuento):
        if 0 < descuento < 100:
            self.__precio *= (100 - descuento) / 100
        else:
            print("Descuento inválido")

def probarProductos():
    producto1 = Producto("Zapatilla", 250)
    producto2 = Producto("Casaca", 300)
    print(producto1.get_nombre())
    print(producto1.get_precio())
    producto1.descuento(10)
    producto1.descuento(120)
    print(producto1.get_nombre())
    print(producto1.get_precio())
    print(producto2.get_nombre())
    print(producto2.get_precio())
    producto2.descuento(50)
    print(producto2.get_nombre())
    print(producto2.get_precio())
    
def main():
    probarProductos()

if __name__=="__main__":
    main()
