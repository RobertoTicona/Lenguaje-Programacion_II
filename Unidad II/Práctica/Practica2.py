# ==============================
# Sistema de Control de Inventario
# Interfaz Gráfica con Tkinter
# ==============================

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# =====================
# MODELO
# =====================
class Producto:
    def __init__(
        self, codigo, nombre, precio, stock=0,
        categoria="General", marca="N/A",
        descripcion="", stock_minimo=10
    ):
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


class Movimiento:
    def __init__(self, codigo, tipo, cantidad):
        self.codigo = codigo
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = datetime.now()


class Inventario:
    def __init__(self):
        self.productos = {}
        self.movimientos = []

    def registrar_producto(self, producto):
        if producto.codigo in self.productos:
            raise ValueError("El producto ya existe")
        self.productos[producto.codigo] = producto

    def entrada_producto(self, codigo, cantidad):
        self._verificar(codigo)
        self.productos[codigo].entrada_stock(cantidad)
        self.movimientos.append(Movimiento(codigo, "ENTRADA", cantidad))

    def salida_producto(self, codigo, cantidad):
        self._verificar(codigo)
        self.productos[codigo].salida_stock(cantidad)
        self.movimientos.append(Movimiento(codigo, "SALIDA", cantidad))

    def _verificar(self, codigo):
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado")

    # =====================
    # REPORTE PDF
    # =====================
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

# =====================
# VISTA / CONTROLADOR
# =====================
class AppInventario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Inventario - Bodega")
        self.geometry("1100x560")
        self.resizable(False, False)

        self.inventario = Inventario()
        self._estilos()
        self._interfaz()
        self._cargar_demo()
        self._actualizar_tabla()

    def _estilos(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        bg = "#f4f6f8"
        ok = "#2fb344"
        err = "#d63939"

        self.configure(bg=bg)
        style.configure("TLabel", background=bg)
        style.configure("TLabelframe", background=bg)
        style.configure("TLabelframe.Label", font=("Segoe UI", 10, "bold"))
        style.configure("Success.TLabel", foreground=ok, background=bg)
        style.configure("Error.TLabel", foreground=err, background=bg)

    def _interfaz(self):
        # FORMULARIO
        frame_form = ttk.LabelFrame(self, text="Registro de Producto", padding=10)
        frame_form.place(x=20, y=20, width=350, height=320)

        campos = [
            "Código", "Nombre", "Marca", "Categoría",
            "Descripción", "Precio", "Stock", "Stock mínimo"
        ]
        self.entries = {}

        for i, campo in enumerate(campos):
            ttk.Label(frame_form, text=campo).grid(row=i, column=0, sticky="w", pady=4)
            e = ttk.Entry(frame_form, width=25)
            e.grid(row=i, column=1, pady=4)
            self.entries[campo] = e

        ttk.Button(frame_form, text="Registrar", command=self.registrar).grid(columnspan=2, pady=8)
        self.lbl_msg = ttk.Label(frame_form)
        self.lbl_msg.grid(columnspan=2)

        # TABLA
        frame_tabla = ttk.LabelFrame(self, text="Inventario", padding=10)
        frame_tabla.place(x=400, y=20, width=660, height=320)

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=("c", "n", "m", "cat", "p", "s"),
            show="headings"
        )

        for col, txt in zip(
            self.tabla["columns"],
            ["Código", "Nombre", "Marca", "Categoría", "Precio", "Stock"]
        ):
            self.tabla.heading(col, text=txt)
            self.tabla.column(col, width=100, anchor="center")

        self.tabla.tag_configure("bajo", background="#ffe3e3")
        self.tabla.pack(fill="both", expand=True)

        # MOVIMIENTOS
        frame_mov = ttk.LabelFrame(self, text="Movimientos", padding=10)
        frame_mov.place(x=20, y=360, width=1040, height=160)

        ttk.Label(frame_mov, text="Código").grid(row=0, column=0)
        self.codigo_mov = ttk.Entry(frame_mov, width=15)
        self.codigo_mov.grid(row=0, column=1)

        ttk.Label(frame_mov, text="Cantidad").grid(row=0, column=2)
        self.cantidad_mov = ttk.Entry(frame_mov, width=10)
        self.cantidad_mov.grid(row=0, column=3)

        ttk.Button(frame_mov, text="Entrada", command=self.entrada).grid(row=0, column=4, padx=5)
        ttk.Button(frame_mov, text="Salida", command=self.salida).grid(row=0, column=5, padx=5)

        ttk.Button(
            frame_mov,
            text="Generar PDF",
            command=self.generar_pdf
        ).grid(row=0, column=6, padx=20)

        self.lbl_msg2 = ttk.Label(frame_mov)
        self.lbl_msg2.grid(row=1, columnspan=10, pady=10)

    # =====================
    # FUNCIONES
    # =====================
    def registrar(self):
        try:
            p = Producto(
                self.entries["Código"].get(),
                self.entries["Nombre"].get(),
                float(self.entries["Precio"].get()),
                int(self.entries["Stock"].get()),
                self.entries["Categoría"].get(),
                self.entries["Marca"].get(),
                self.entries["Descripción"].get(),
                int(self.entries["Stock mínimo"].get())
            )
            self.inventario.registrar_producto(p)
            self._actualizar_tabla()
            self.lbl_msg.config(text="Producto registrado correctamente", style="Success.TLabel")
        except Exception as e:
            self.lbl_msg.config(text=str(e), style="Error.TLabel")

    def entrada(self):
        self._movimiento("ENTRADA")

    def salida(self):
        self._movimiento("SALIDA")

    def _movimiento(self, tipo):
        try:
            codigo = self.codigo_mov.get()
            cantidad = int(self.cantidad_mov.get())
            if tipo == "ENTRADA":
                self.inventario.entrada_producto(codigo, cantidad)
            else:
                self.inventario.salida_producto(codigo, cantidad)
            self._actualizar_tabla()
            self.lbl_msg2.config(text=f"{tipo} registrada correctamente", style="Success.TLabel")
        except Exception as e:
            self.lbl_msg2.config(text=str(e), style="Error.TLabel")

    def _actualizar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        for p in self.inventario.productos.values():
            tag = "bajo" if p.stock_bajo() else ""
            self.tabla.insert(
                "",
                "end",
                values=(p.codigo, p.nombre, p.marca, p.categoria, p.precio, p.stock),
                tags=(tag,)
            )

    def generar_pdf(self):
        self.inventario.generar_reporte_pdf()
        self.lbl_msg2.config(text="Reporte PDF generado correctamente", style="Success.TLabel")

    def _cargar_demo(self):
        demo = [
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

        for p in demo:
            self.inventario.registrar_producto(p)

# =====================
# EJECUCIÓN
# =====================
if __name__ == "__main__":
    app = AppInventario()
    app.mainloop()

