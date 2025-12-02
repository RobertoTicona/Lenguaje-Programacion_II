def fibonacci(n):
    a = 0
    b = 1
    for i in range (n):
        print(a)
        c = a + b
        b = a
        a = c

def main():
    try:
        n = int(input("Ingrese el valor de n: "))
        if n <= 0:
            raise ValueError("El valor de n tiene que ser positivo")
        fibonacci(n)
    except ValueError as ve:
        print("Error", ve)
    except Exception as e:
        print("Ocurrio un error inesperado", e)

if __name__=="__main__":
    main()
