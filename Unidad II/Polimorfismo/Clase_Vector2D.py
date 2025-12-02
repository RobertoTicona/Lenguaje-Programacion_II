class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        return Vector2D(self.x * escalar, self.y * escalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

def main():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print("v1 =", v1)
    print("v2 =", v2)

    print("Suma:", v1 + v2)          
    print("Resta:", v1 - v2)         
    print("Multiplicación:", v1 * 3) 

if __name__ == "__main__":
    main()
