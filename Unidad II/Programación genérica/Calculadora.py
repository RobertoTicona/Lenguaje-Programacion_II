import tkinter as tk
from tkinter import ttk
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def sumar(self): return self.a + self.b
    def restar(self): return self.a - self.b
    def multiplicar(self): return self.a * self.b

    def dividir(self):
        if self.b == 0:
            raise ZeroDivisionError("No puedes dividir entre 0 😢")
        return self.a / self.b

# ------------------------- FUNCIÓN -------------------------

def operar(op):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        calc = Calculadora(a, b)

        if op == "sumar": r = calc.sumar()
        elif op == "restar": r = calc.restar()
        elif op == "multiplicar": r = calc.multiplicar()
        elif op == "dividir": r = calc.dividir()

        lbl_result["text"] = f"✨ Resultado: {r}"
        lbl_error["text"] = ""

    except Exception as e:
        lbl_error["text"] = f"❌ Error: {e}"
        lbl_result["text"] = "✨ Resultado: —"

# ------------------------- VENTANA -------------------------

root = tk.Tk()
root.title("Calculadora Mágica ✨")
root.geometry("600x420")
root.configure(bg="#FFEFD5")   # durazno pastel

# ----------- ESTILOS -----------

style = ttk.Style()
style.configure("TButton",
                font=("Comic Sans MS", 14, "bold"),
                padding=12,
                relief="flat")

def boton_color(widget, color):
    widget.configure(style=f"{color}.TButton")
    style.configure(f"{color}.TButton",
                    background=color,
                    foreground="white")

# ----------- TITULO -----------

titulo = tk.Label(root,
                  text="🧮✨ Calculadora Mágica para Niños ✨🧮",
                  font=("Comic Sans MS", 22, "bold"),
                  bg="#FFEFD5",
                  fg="#FF6347")
titulo.pack(pady=10)

# ----------- ENTRADAS -----------

frame = tk.Frame(root, bg="#FFEFD5")
frame.pack(pady=10)

tk.Label(frame, text="Número A:", font=("Comic Sans MS", 16),
         bg="#FFEFD5").grid(row=0, column=0, padx=10, pady=10)

entry_a = ttk.Entry(frame, width=15, font=("Comic Sans MS", 16))
entry_a.grid(row=0, column=1)

tk.Label(frame, text="Número B:", font=("Comic Sans MS", 16),
         bg="#FFEFD5").grid(row=1, column=0, padx=10, pady=10)

entry_b = ttk.Entry(frame, width=15, font=("Comic Sans MS", 16))
entry_b.grid(row=1, column=1)

# ----------- BOTONES GRANDES Y REDONDOS -----------

btn_frame = tk.Frame(root, bg="#FFEFD5")
btn_frame.pack(pady=10)

btn_sumar = ttk.Button(btn_frame, text="➕ Sumar",
                       command=lambda: operar("sumar"))
btn_sumar.grid(row=0, column=0, padx=10)
boton_color(btn_sumar, "#FF6F61")

btn_restar = ttk.Button(btn_frame, text="➖ Restar",
                        command=lambda: operar("restar"))
btn_restar.grid(row=0, column=1, padx=10)
boton_color(btn_restar, "#6A5ACD")

btn_multi = ttk.Button(btn_frame, text="✖ Multiplicar",
                       command=lambda: operar("multiplicar"))
btn_multi.grid(row=0, column=2, padx=10)
boton_color(btn_multi, "#20B2AA")

btn_div = ttk.Button(btn_frame, text="➗ Dividir",
                     command=lambda: operar("dividir"))
btn_div.grid(row=0, column=3, padx=10)
boton_color(btn_div, "#FF8C00")

# ----------- RESULTADO -----------

lbl_result = tk.Label(root,
                      text="✨ Resultado: —",
                      font=("Comic Sans MS", 20, "bold"),
                      fg="#2E8B57",
                      bg="#FFEFD5")
lbl_result.pack(pady=15)

# ----------- ERROR -----------

lbl_error = tk.Label(root,
                     text="",
                     font=("Comic Sans MS", 14),
                     fg="red",
                     bg="#FFEFD5")
lbl_error.pack()

root.mainloop()
