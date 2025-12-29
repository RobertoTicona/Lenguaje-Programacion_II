from typing import TypeVar, Generic
import math
import tkinter as tk
from tkinter import ttk

T = TypeVar('T', int, float)

# ======================================================
#                 CLASES DE FIGURAS
# ======================================================
class Figura(Generic[T]):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def area(self) -> T:
        raise NotImplementedError

    def perimetro(self) -> T:
        raise NotImplementedError


class Circulo(Figura[T]):
    def __init__(self, radio: T):
        super().__init__("Círculo")
        try:
            if not isinstance(radio, (int, float)):
                raise TypeError("El radio debe ser un número.")
            if radio < 0:
                raise ValueError("El radio no puede ser negativo.")
            self.radio = radio
        except Exception as e:
            raise TypeError(f"Error al asignar radio: {e}")

    def area(self) -> T:
        return math.pi * self.radio ** 2

    def perimetro(self) -> T:
        return 2 * math.pi * self.radio


class Rectangulo(Figura[T]):
    def __init__(self, base: T, altura: T):
        super().__init__("Rectángulo")
        try:
            if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
                raise TypeError("Base y altura deben ser números.")
            if base < 0 or altura < 0:
                raise ValueError("Base y altura no pueden ser negativas.")
            self.base = base
            self.altura = altura
        except Exception as e:
            raise TypeError(f"Error al asignar valores: {e}")

    def area(self) -> T:
        return self.base * self.altura

    def perimetro(self) -> T:
        return 2 * (self.base + self.altura)


# ======================================================
#                 INTERFAZ TKINTER
# ======================================================
class App:
    def __init__(self, root):
        self.root = root
        root.title("Figuras Geométricas para Niños")
        root.geometry("600x500")
        root.configure(bg="#F7E9A0")  # Fondo pastel

        title = tk.Label(
            root,
            text="🎨 Calculadora de Figuras Geométricas 🎨",
            bg="#F7E9A0",
            fg="#D35400",
            font=("Comic Sans MS", 22, "bold")
        )
        title.pack(pady=10)

        # Selección de figura
        self.figura_var = tk.StringVar(value="Círculo")
        frame_select = tk.Frame(root, bg="#F7E9A0")
        frame_select.pack(pady=10)

        tk.Label(frame_select, text="Elige una figura:",
                 font=("Comic Sans MS", 14),
                 bg="#F7E9A0").pack(side=tk.LEFT, padx=5)

        ttk.Combobox(
            frame_select,
            textvariable=self.figura_var,
            values=["Círculo", "Rectángulo"],
            width=12,
            font=("Comic Sans MS", 12)
        ).pack(side=tk.LEFT)

        # Frame de entradas
        self.frame_inputs = tk.Frame(root, bg="#F7E9A0")
        self.frame_inputs.pack(pady=10)

        # Entrada 1
        self.label1 = tk.Label(self.frame_inputs, text="Radio:",
                               font=("Comic Sans MS", 14),
                               bg="#F7E9A0")
        self.label1.grid(row=0, column=0, padx=5)

        self.entry1 = tk.Entry(self.frame_inputs, font=("Comic Sans MS", 14), width=8)
        self.entry1.grid(row=0, column=1)

        # Entrada 2 (solo rectángulo)
        self.label2 = tk.Label(self.frame_inputs, text="Altura:",
                               font=("Comic Sans MS", 14),
                               bg="#F7E9A0")

        self.entry2 = tk.Entry(self.frame_inputs, font=("Comic Sans MS", 14), width=8)

        # Botón calcular
        tk.Button(
            root,
            text="Calcular",
            command=self.calcular,
            bg="#FFB74D",
            fg="black",
            font=("Comic Sans MS", 16, "bold"),
            width=12
        ).pack(pady=10)

        # Canvas para dibujar
        self.canvas = tk.Canvas(root, width=300, height=200, bg="#FFF")
        self.canvas.pack(pady=10)

        # Resultado
        self.resultado = tk.Label(root, text="", font=("Comic Sans MS", 14),
                                  bg="#F7E9A0", fg="blue")
        self.resultado.pack()

        # Error
        self.error = tk.Label(root, text="", font=("Comic Sans MS", 12),
                              bg="#F7E9A0", fg="red")
        self.error.pack()

        # Actualizar entradas según selección
        self.figura_var.trace("w", self.actualizar_inputs)
        self.actualizar_inputs()

    # ---------------------------------------------------
    # Actualiza las casillas dependiendo de la figura
    # ---------------------------------------------------
    def actualizar_inputs(self, *args):
        figura = self.figura_var.get()
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.error.config(text="")
        self.resultado.config(text="")
        self.canvas.delete("all")

        if figura == "Círculo":
            self.label1.config(text="Radio:")
            self.label2.grid_remove()
            self.entry2.grid_remove()
        else:
            self.label1.config(text="Base:")
            self.label2.config(text="Altura:")
            self.label2.grid(row=1, column=0, padx=5)
            self.entry2.grid(row=1, column=1)

    # ---------------------------------------------------
    # Realiza cálculos y dibuja la figura
    # ---------------------------------------------------
    def calcular(self):
        self.error.config(text="")
        self.resultado.config(text="")
        self.canvas.delete("all")

        figura = self.figura_var.get()

        try:
            val1 = float(self.entry1.get())
            if figura == "Rectángulo":
                val2 = float(self.entry2.get())

            if val1 < 0 or (figura == "Rectángulo" and val2 < 0):
                raise ValueError("Los valores no pueden ser negativos.")

            if figura == "Círculo":
                obj = Circulo(val1)
                area = obj.area()
                peri = obj.perimetro()
                self.dibujar_circulo(val1)
            else:
                obj = Rectangulo(val1, val2)
                area = obj.area()
                peri = obj.perimetro()
                self.dibujar_rectangulo(val1, val2)

            self.resultado.config(
                text=f"Área: {area:.2f}   |   Perímetro: {peri:.2f}"
            )

        except ValueError:
            self.error.config(text="❌ Ingresa números válidos.")
        except Exception as e:
            self.error.config(text=f"❌ Error: {e}")

    # ---------------------------------------------------
    # Gráficos en Canvas
    # ---------------------------------------------------
    def dibujar_circulo(self, radio):
        r = min(80, radio * 5)
        self.canvas.create_oval(150 - r, 100 - r, 150 + r, 100 + r,
                                outline="blue", width=3)

    def dibujar_rectangulo(self, base, altura):
        b = min(150, base * 10)
        h = min(120, altura * 10)
        x1, y1 = 150 - b/2, 100 - h/2
        x2, y2 = 150 + b/2, 100 + h/2
        self.canvas.create_rectangle(x1, y1, x2, y2,
                                     outline="green", width=3)


# ======================================================
#               INICIO DE LA APP
# ======================================================
root = tk.Tk()
app = App(root)
root.mainloop()
