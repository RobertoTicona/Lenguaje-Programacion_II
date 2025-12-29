from typing import TypeVar, Generic
import tkinter as tk

# ------------------------------
# Modelo: Tu clase Calculadora
# ------------------------------

T = TypeVar('T', int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        try:
            self.a = a
            self.b = b
        except Exception as e:
            raise TypeError(f"Error al asignar valores en el constructor: {e}")

    def sumar(self) -> T:
        try:
            return self.a + self.b
        except Exception as e:
            raise TypeError(f"Error al sumar: {e}")

    def restar(self) -> T:
        try:
            return self.a - self.b
        except Exception as e:
            raise TypeError(f"Error al restar: {e}")

    def multiplicar(self) -> T:
        try:
            return self.a * self.b
        except Exception as e:
            raise TypeError(f"Error al multiplicar: {e}")

    def dividir(self) -> T:
        try:
            if self.b == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            return self.a / self.b
        except Exception as e:
            raise TypeError(f"Error al dividir: {e}")

# ------------------------------
# Vista y Controlador: Tkinter
# ------------------------------

def crear_calculadora():
    try:
        a_val = float(entry_a.get())
        b_val = float(entry_b.get())
        return Calculadora(a_val, b_val)
    except ValueError:
        label_resultado.config(text="❌ Error: ingresa solo números")
        return None

def ejecutar_operacion(operacion):
    calc = crear_calculadora()
    if calc is None:
        return

    try:
        if operacion == "sumar":
            res = calc.sumar()
        elif operacion == "restar":
            res = calc.restar()
        elif operacion == "multiplicar":
            res = calc.multiplicar()
        elif operacion == "dividir":
            res = calc.dividir()

        label_resultado.config(text=f"Resultado: {res}")

    except Exception as e:
        label_resultado.config(text=f"❌ Error: {e}")

# ------------------------------
# Construcción de la interfaz
# ------------------------------

root = tk.Tk()
root.title("Calculadora Genérica")
root.geometry("350x300")
root.resizable(False, False)

# Entrada A
tk.Label(root, text="Valor A:").pack()
entry_a = tk.Entry(root, width=20)
entry_a.pack()

# Entrada B
tk.Label(root, text="Valor B:").pack()
entry_b = tk.Entry(root, width=20)
entry_b.pack()

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Sumar", width=12, command=lambda: ejecutar_operacion("sumar")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="Restar", width=12, command=lambda: ejecutar_operacion("restar")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="Multiplicar", width=12, command=lambda: ejecutar_operacion("multiplicar")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="Dividir", width=12, command=lambda: ejecutar_operacion("dividir")).grid(row=1, column=1, padx=5, pady=5)

# Label para mostrar resultados y errores
label_resultado = tk.Label(root, text="Resultado:", fg="blue", font=("Arial", 12))
label_resultado.pack(pady=15)

# Ejecutar interfaz
root.mainloop()
