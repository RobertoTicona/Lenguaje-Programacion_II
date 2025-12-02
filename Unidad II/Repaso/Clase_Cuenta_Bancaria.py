class CuentaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= monto

    def mostrarSaldo(self):
        print(f"El saldo de {self.titular} es {self.saldo}")

def prueba_cuenta_bancaria():
    c1 = CuentaBancaria("Ana", 500)
    c2 = CuentaBancaria("Luis", 300)

    c1.depositar(200)
    c1.retirar(100)
    c1.mostrarSaldo()
    c2.retirar(500)
    c2.mostrarSaldo()

def main():
    print("==== Probando CuentaBancaria ====")
    prueba_cuenta_bancaria()

if __name__=="__main__":
    main()
