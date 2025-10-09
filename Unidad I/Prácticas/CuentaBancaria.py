class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        print(f"Cuenta creada, bienvenido {self.titular}")

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto} realizado. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes para retirar esa cantidad.")

    def __del__(self):
        print(f"Cuenta de {self.titular} cerrada")


def main():
    titular = input("Ingrese el nombre del titular: ")
    saldo = float(input("Ingrese su saldo inicial: "))
    
    cuenta = CuentaBancaria(titular, saldo)

    # Hacemos un depósito
    cuenta.depositar(200)

    # Hacemos un retiro
    cuenta.retirar(100)

    # Eliminamos el objeto (forzamos el destructor)
    del cuenta


if __name__ == "__main__":
    main()

