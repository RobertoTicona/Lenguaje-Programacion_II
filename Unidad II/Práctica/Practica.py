# ==============================
# Sistema de Control de Inventario
# Programación Orientada a Objetos
# ==============================

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# ------------------------------
# CLASE PRODUCTO
# ------------------------------
class Producto:
    def __init__(self, codigo, nombre, precio, stock=0,
                 categoria="General", marca="N/A",
                 descripcion="", stock_minimo=10):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.marca = marca
        self.descripcion = descripcion
        self.stock_minimo = stock_minimo

    def stock_bajo(self):
        return self.stock <= self.stock_minimo

    def entrada_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.stock += cantidad

    def salida_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

    def __str__(self):
        return (
            f"{self.codigo} | {self.nombre} | {self.marca} | "
            f"{self.categoria} | S/. {self.precio:.2f} | Stock: {self.stock}"
        )


# ------------------------------
# CLASE MOVIMIENTO
# ------------------------------
class Movimiento:
    def __init__(self, codigo_producto, tipo, cantidad):
        self.codigo_producto = codigo_producto
        self.tipo = tipo  # ENTRADA o SALIDA
        self.cantidad = cantidad
        self.fecha = datetime.now()

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%Y %H:%M')} | {self.codigo_producto} | {self.tipo} | {self.cantidad}"


# ------------------------------
# CLASE INVENTARIO
# ------------------------------
class Inventario:
    def __init__(self):
        self.productos = {}
        self.movimientos = []

    def registrar_producto(self, producto):
        if producto.codigo in self.productos:
            raise ValueError("El producto ya existe")
        self.productos[producto.codigo] = producto

    def entrada_producto(self, codigo, cantidad):
        self._verificar_producto(codigo)
        self.productos[codigo].entrada_stock(cantidad)
        self.movimientos.append(Movimiento(codigo, "ENTRADA", cantidad))

    def salida_producto(self, codigo, cantidad):
        self._verificar_producto(codigo)
        self.productos[codigo].salida_stock(cantidad)
        self.movimientos.append(Movimiento(codigo, "SALIDA", cantidad))

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        for producto in self.productos.values():
            print(producto)

    def buscar_por_categoria(self, categoria):
        print(f"\n--- PRODUCTOS EN LA CATEGORÍA: {categoria} ---")
        encontrados = False
        for producto in self.productos.values():
            if producto.categoria.lower() == categoria.lower():
                print(producto)
                encontrados = True
        if not encontrados:
            print("No se encontraron productos")

    def reporte_movimientos(self):
        print("\n--- REPORTE DE MOVIMIENTOS ---")
        for mov in self.movimientos:
            print(mov)

    def reporte_movimientos_filtrado(self, tipo):
        print(f"\n--- REPORTE DE {tipo} ---")
        for mov in self.movimientos:
            if mov.tipo == tipo:
                print(mov)

    def generar_reporte_pdf(self, archivo="reporte_inventario.pdf"):
        c = canvas.Canvas(archivo, pagesize=A4)
        width, height = A4

        y = height - 50

        # TÍTULO
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "REPORTE GENERAL DE INVENTARIO - BODEGA")
        y -= 30

        c.setFont("Helvetica", 10)
        c.drawString(50, y, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        y -= 30

        # =========================
        # INVENTARIO
        # =========================
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "1. INVENTARIO ACTUAL")
        y -= 20

        c.setFont("Helvetica-Bold", 9)
        c.drawString(50, y, "Código")
        c.drawString(100, y, "Producto")
        c.drawString(230, y, "Categoría")
        c.drawString(320, y, "Precio")
        c.drawString(380, y, "Stock")
        y -= 15

        c.setFont("Helvetica", 9)

        for p in self.productos.values():
            if y < 60:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 9)

            c.drawString(50, y, p.codigo)
            c.drawString(100, y, p.nombre[:18])
            c.drawString(230, y, p.categoria)
            c.drawString(320, y, f"S/. {p.precio:.2f}")
            c.drawString(380, y, str(p.stock))
            y -= 14

        # =========================
        # MOVIMIENTOS
        # =========================
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "2. MOVIMIENTOS DE STOCK")
        y -= 20

        c.setFont("Helvetica-Bold", 9)
        c.drawString(50, y, "Fecha")
        c.drawString(150, y, "Código")
        c.drawString(220, y, "Tipo")
        c.drawString(280, y, "Cantidad")
        y -= 15

        c.setFont("Helvetica", 9)

        for m in self.movimientos:
            if y < 60:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 9)

            c.drawString(50, y, m.fecha.strftime("%d/%m/%Y %H:%M"))
            c.drawString(150, y, m.codigo_producto)
            c.drawString(220, y, m.tipo)
            c.drawString(280, y, str(m.cantidad))
            y -= 14

        c.save()

    def _verificar_producto(self, codigo):
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado")


# ------------------------------
# CLASE SISTEMA
# ------------------------------
class SistemaInventario:
    def __init__(self):
        self.inventario = Inventario()
        self._cargar_demo()

    def ejecutar(self):
        while True:
            self._menu()
            opcion = input("Seleccione una opción: ")

            try:
                if opcion == "1":
                    self._registrar_producto()
                elif opcion == "2":
                    self._entrada_stock()
                elif opcion == "3":
                    self._salida_stock()
                elif opcion == "4":
                    self.inventario.mostrar_inventario()
                elif opcion == "5":
                    self.inventario.reporte_movimientos()
                elif opcion == "6":
                    cat = input("Categoría: ")
                    self.inventario.buscar_por_categoria(cat)
                elif opcion == "7":
                    tipo = input("ENTRADA o SALIDA: ").upper()
                    self.inventario.reporte_movimientos_filtrado(tipo)
                elif opcion == "8":
                    self.inventario.generar_reporte_pdf()
                    print("Reporte PDF generado correctamente")
                elif opcion == "0":
                    print("Saliendo del sistema...")
                    break
                else:
                    print("Opción inválida")
            except Exception as e:
                print(f"Error: {e}")

    def _menu(self):
        print("""
======== SISTEMA DE INVENTARIO ========
1. Registrar producto
2. Entrada de stock
3. Salida de stock
4. Mostrar inventario
5. Reporte de movimientos
6. Buscar por categoría
7. Reporte filtrado
8. Generar reporte PDF
0. Salir
""")

    def _registrar_producto(self):
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        marca = input("Marca: ")
        categoria = input("Categoría: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        stock_minimo = int(input("Stock mínimo: "))

        p = Producto(
            codigo, nombre, precio, stock,
            categoria, marca, descripcion, stock_minimo
        )
        self.inventario.registrar_producto(p)
        print("Producto registrado correctamente")

    def _entrada_stock(self):
        codigo = input("Código: ")
        cantidad = int(input("Cantidad: "))
        self.inventario.entrada_producto(codigo, cantidad)
        print("Entrada registrada")

    def _salida_stock(self):
        codigo = input("Código: ")
        cantidad = int(input("Cantidad: "))
        self.inventario.salida_producto(codigo, cantidad)
        print("Salida registrada")

    def _cargar_demo(self):
        productos_demo = [
            # ALIMENTOS
            Producto("A001", "Arroz Costeño 1Kg", 4.50, 120, "Alimentos", "Costeño", "Arroz extra graneado"),
            Producto("A002", "Azúcar Rubia 1Kg", 3.80, 90, "Alimentos", "Paramonga", "Azúcar rubia"),
            Producto("A003", "Fideos Tallarín", 2.50, 150, "Alimentos", "Don Vittorio", "Fideos largos"),
            Producto("A004", "Aceite Vegetal 1L", 9.80, 60, "Alimentos", "Primor", "Aceite vegetal"),
            Producto("A005", "Atún en lata", 6.20, 45, "Alimentos", "Florida", "Atún en aceite"),

            # LÁCTEOS
            Producto("L001", "Leche Evaporada", 3.20, 80, "Lácteos", "Gloria", "Leche evaporada"),
            Producto("L002", "Yogurt Fresa", 2.80, 35, "Lácteos", "Laive", "Yogurt sabor fresa"),
            Producto("L003", "Queso Fresco", 12.00, 20, "Lácteos", "Bonlé", "Queso fresco"),

            # LIMPIEZA
            Producto("LIM001", "Detergente 1Kg", 12.00, 40, "Limpieza", "Ariel", "Detergente en polvo"),
            Producto("LIM002", "Jabón Barra", 2.50, 70, "Limpieza", "Bolívar", "Jabón antibacterial"),
            Producto("LIM003", "Lejía 1L", 3.00, 30, "Limpieza", "Clorox", "Lejía concentrada"),

            # BEBIDAS
            Producto("B001", "Gaseosa Cola 1.5L", 7.50, 55, "Bebidas", "Coca-Cola", "Gaseosa cola"),
            Producto("B002", "Agua Mineral 625ml", 1.50, 120, "Bebidas", "San Luis", "Agua sin gas"),
            Producto("B003", "Jugo en caja", 2.00, 65, "Bebidas", "Frugos", "Jugo de frutas"),

            # ÚTILES
            Producto("U001", "Cuaderno A4", 6.00, 50, "Útiles", "Justus", "Cuaderno universitario"),
            Producto("U002", "Lapicero Azul", 1.50, 200, "Útiles", "Pilot", "Tinta azul"),
            Producto("U003", "Resaltador", 3.50, 40, "Útiles", "Stabilo", "Color amarillo"),

            # GOLOSINAS
            Producto("G001", "Galletas Chocolate", 2.20, 100, "Golosinas", "Oreo", "Galletas rellenas"),
            Producto("G002", "Chocolatina", 1.80, 150, "Golosinas", "Sublime", "Chocolate clásico"),
            Producto("G003", "Caramelos", 0.10, 500, "Golosinas", "Arcor", "Caramelos surtidos"),
        ]

        for p in productos_demo:
            self.inventario.registrar_producto(p)

# ------------------------------
# EJECUCIÓN
# ------------------------------
if __name__ == "__main__":
    sistema = SistemaInventario()
    sistema.ejecutar()
