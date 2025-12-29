import tkinter as tk
from tkinter import ttk, messagebox
import math

# ========= Principio S =========
class CalcularFiguras:
    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


# ========= Principio O y L =========
class Rectangulo(CalcularFiguras):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(CalcularFiguras):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


# ========= Principio D =========
class Aplicacion:
    def __init__(self, figura: CalcularFiguras):
        self.figura = figura

    def ejecutar(self):
        return self.figura.area(), self.figura.perimetro()


# ========= Funciones =========
def calcular_rectangulo():
    try:
        rec = Rectangulo(float(base_entry.get()), float(altura_entry.get()))
        app = Aplicacion(rec)
        area, perimetro = app.ejecutar()
        resultado.set(
            f"▭ rectángulo\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")


def calcular_circulo():
    try:
        cir = Circulo(float(radio_entry.get()))
        app = Aplicacion(cir)
        area, perimetro = app.ejecutar()
        resultado.set(
            f"⚪ Círculo\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido")


# ========= Ventana =========
root = tk.Tk()
root.title("Calculadora de Figuras - SOLID")
root.geometry("380x480")
root.configure(bg="#1e1e2f")

# ========= Estilos =========
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TFrame",
    background="#1e1e2f"
)

style.configure(
    "Title.TLabel",
    font=("Segoe UI", 18, "bold"),
    foreground="#ffffff",
    background="#1e1e2f"
)

style.configure(
    "Section.TLabel",
    font=("Segoe UI", 12, "bold"),
    foreground="#f5c542",
    background="#1e1e2f"
)

style.configure(
    "TLabel",
    font=("Segoe UI", 10),
    foreground="#ffffff",
    background="#1e1e2f"
)

style.configure(
    "TButton",
    font=("Segoe UI", 10, "bold"),
    padding=8,
    background="#4f46e5",
    foreground="white"
)

style.map(
    "TButton",
    background=[("active", "#6366f1")]
)

# ========= Contenedor =========
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

# ========= Título =========
ttk.Label(frame, text="Calculadora de Figuras", style="Title.TLabel")\
    .pack(pady=10)

# ========= Rectángulo =========
ttk.Label(frame, text="Rectángulo", style="Section.TLabel").pack(pady=5)

base_entry = ttk.Entry(frame)
base_entry.pack(fill="x", pady=2)
base_entry.insert(0, "Base")

altura_entry = ttk.Entry(frame)
altura_entry.pack(fill="x", pady=2)
altura_entry.insert(0, "Altura")

ttk.Button(frame, text="Calcular Rectángulo", command=calcular_rectangulo)\
    .pack(pady=6)

# ========= Círculo =========
ttk.Label(frame, text="Círculo", style="Section.TLabel").pack(pady=5)

radio_entry = ttk.Entry(frame)
radio_entry.pack(fill="x", pady=2)
radio_entry.insert(0, "Radio")

ttk.Button(frame, text="Calcular Círculo", command=calcular_circulo)\
    .pack(pady=6)

# ========= Resultado =========
resultado = tk.StringVar()
ttk.Label(
    frame,
    textvariable=resultado,
    font=("Segoe UI", 11, "bold"),
    foreground="#22c55e",
    background="#1e1e2f",
    justify="center"
).pack(pady=15)

root.mainloop()

