import tkinter as tk
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class CalculadoraFactorial(Generic[T]):
    def __init__(self, numero: T):
        self.numero = numero

    def calcular_factorial(self) -> int:
        n = int(self.numero)
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


def calcular():
    label_error.config(text="")
    label_resultado.config(text="Factorial: ---")

    try:
        n = int(entry_n.get())
        cal = CalculadoraFactorial(n)
        resultado = cal.calcular_factorial()
        label_resultado.config(text=f"Factorial: {resultado}")

    except ValueError as e:
        label_error.config(text=f"Error: {e}", fg="red")
    except Exception as e:
        label_error.config(text=f"Error inesperado: {e}", fg="red")


# ------------------------------
#        INTERFAZ TKINTER
# ------------------------------

root = tk.Tk()
root.title("Calculadora de Factorial")
root.geometry("320x220")

label_n = tk.Label(root, text="Ingrese n:")
label_n.pack()

entry_n = tk.Entry(root)
entry_n.pack()

btn = tk.Button(root, text="Calcular factorial", command=calcular)
btn.pack(pady=10)

label_resultado = tk.Label(root, text="Factorial: ---", font=("Arial", 12))
label_resultado.pack()

label_error = tk.Label(root, text="", font=("Arial", 10))
label_error.pack(pady=5)

root.mainloop()
