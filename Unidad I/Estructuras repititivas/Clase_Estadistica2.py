import tkinter as tk
from tkinter import messagebox, scrolledtext

class Estadistica:
    def __init__(self, datos):
        self.datos = datos
        self.cantidad = len(datos)

    def promedio(self):
        return sum(self.datos) / self.cantidad

    def varianza1P(self):
        prom = self.promedio()
        return sum((x - prom) ** 2 for x in self.datos) / self.cantidad

    def varianza2P(self):
        suma = sum(self.datos)
        suma_cuadrados = sum(z ** 2 for z in self.datos)
        return (suma_cuadrados - (suma ** 2) / self.cantidad) / self.cantidad

    def varianza1M(self):
        prom = self.promedio()
        return sum((x - prom) ** 2 for x in self.datos) / (self.cantidad - 1)

    def varianza2M(self):
        suma = sum(self.datos)
        suma_cuadrados = sum(z ** 2 for z in self.datos)
        return (suma_cuadrados - (suma ** 2) / self.cantidad) / (self.cantidad - 1)


# ---------------- INTERFAZ ----------------
def calcular():
    try:
        datos = [float(x) for x in entry_datos.get().split(",")]
        calc = Estadistica(datos)

        prom = calc.promedio()
        v1p = calc.varianza1P()
        v2p = calc.varianza2P()
        v1m = calc.varianza1M()
        v2m = calc.varianza2M()

        texto = f"""
Promedio:
   Fórmula:  x̄ = Σx / n
   Resultado: {prom:.4f}

Varianza Poblacional (clásica):
   Fórmula: σ² = Σ(x - x̄)² / n
   Resultado: {v1p:.4f}
   Desviación estándar: {v1p**0.5:.4f}

Varianza Poblacional (reducida):
   Fórmula: σ² = (Σx² - (Σx)² / n) / n
   Resultado: {v2p:.4f}
   Desviación estándar: {v2p**0.5:.4f}

Varianza Muestral (clásica):
   Fórmula: s² = Σ(x - x̄)² / (n - 1)
   Resultado: {v1m:.4f}
   Desviación estándar: {v1m**0.5:.4f}

Varianza Muestral (reducida):
   Fórmula: s² = (Σx² - (Σx)² / n) / (n - 1)
   Resultado: {v2m:.4f}
   Desviación estándar: {v2m**0.5:.4f}
"""
        text_resultado.config(state="normal")
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, texto)
        text_resultado.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")


# Ventana principal
root = tk.Tk()
root.title("Estadística: Promedio y Varianza")
root.geometry("800x600")
root.config(bg="#f4f4f4")

# Frame principal
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", bd=2)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Título
tk.Label(frame, text="Cálculo de Promedio y Varianza", 
         font=("Arial", 18, "bold"), bg="#ffffff", fg="#2c3e50").pack(pady=10)

# Entrada de datos
tk.Label(frame, text="Ingrese los datos separados por coma:", 
         font=("Arial", 14), bg="#ffffff", fg="#2c3e50").pack(anchor="w")
entry_datos = tk.Entry(frame, width=60, font=("Arial", 14))
entry_datos.pack(pady=5)

# Botón calcular
tk.Button(frame, text="Calcular", command=calcular, 
          font=("Arial", 14, "bold"), bg="#2980b9", fg="white", padx=10, pady=5).pack(pady=15)

# Resultados (scrolled text)
text_resultado = scrolledtext.ScrolledText(frame, width=90, height=20, font=("Consolas", 12))
text_resultado.pack(pady=10)
text_resultado.config(state="disabled")

root.mainloop()

