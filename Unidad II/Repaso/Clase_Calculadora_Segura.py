class CalculadoraSegura:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self):
        try:
            resultado = self.a / self.b
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."
        except Excepcion as e:
            return f"Ocurrió un error: {e}"
        finally:
            print("Operación finalizada.")

operacion = CalculadoraSegura(10, 0)
print(operacion.dividir())
