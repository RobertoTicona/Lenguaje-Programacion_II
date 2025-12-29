from typing import TypeVar, Generic
import math

T = TypeVar('T', int, float)

class Figura(Generic[T]):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def area(self) -> T:
        raise NotImplementedError("Las subclases deben implementar este método")

    def perimetro(self) -> T:
        raise NotImplementedError("Las subclases deben implementar este método")


# ------------------------------
#      CÍRCULO
# ------------------------------
class Circulo(Figura[T]):
    def __init__(self, radio: T):
        super().__init__("Círculo")
        try:
            if not isinstance(radio, (int, float)):
                raise TypeError("El radio debe ser un número (int o float).")

            if radio < 0:
                raise ValueError("El radio no puede ser negativo.")

            self.radio = radio

        except Exception as e:
            raise TypeError(f"Error al asignar radio: {e}")

    def area(self) -> T:
        try:
            return math.pi * (self.radio ** 2)
        except Exception as e:
            raise TypeError(f"Error al calcular el área del círculo: {e}")

    def perimetro(self) -> T:
        try:
            return 2 * math.pi * self.radio
        except Exception as e:
            raise TypeError(f"Error al calcular el perímetro del círculo: {e}")


# ------------------------------
#      RECTÁNGULO
# ------------------------------
class Rectangulo(Figura[T]):
    def __init__(self, base: T, altura: T):
        super().__init__("Rectángulo")
        try:
            # Validación de tipo
            if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
                raise TypeError("Base y altura deben ser números (int o float).")

            # Validación de negativos
            if base < 0 or altura < 0:
                raise ValueError("Base y altura no pueden ser negativas.")

            self.base = base
            self.altura = altura

        except Exception as e:
            raise TypeError(f"Error al asignar valores del rectángulo: {e}")

    def area(self) -> T:
        try:
            return self.base * self.altura
        except Exception as e:
            raise TypeError(f"Error al calcular el área del rectángulo: {e}")

    def perimetro(self) -> T:
        try:
            return 2 * (self.base + self.altura)
        except Exception as e:
            raise TypeError(f"Error al calcular el perímetro del rectángulo: {e}")


# ------------------------------
#     PRUEBAS
# ------------------------------
try:
    circulo = Circulo[int](3)
    print(f"Nombre: {circulo.nombre}")
    print(f"Área: {circulo.area():.2f}")
    print(f"Perímetro: {circulo.perimetro():.2f}")

    rectangulo = Rectangulo[int](8, 6)
    print(f"Nombre: {rectangulo.nombre}")
    print(f"Área: {rectangulo.area()}")
    print(f"Perímetro: {rectangulo.perimetro()}")

except Exception as error:
    print(f"❌ Error: {error}")

