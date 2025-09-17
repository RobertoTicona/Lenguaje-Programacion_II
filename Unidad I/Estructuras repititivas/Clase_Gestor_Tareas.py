class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print("Tarea agregada")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes")
        else:
            print("Tareas pendientes")
            for i, tarea in enumerate(self.tareas,1):
                print(f"{i}.- {tarea}")

def main():
    mi_gestor = GestorTareas()
    while True:
        print("\n. ---- MENU ----")
        print("1.- Agregar tarea: ")
        print("2.- Mostrar tarea: ")
        print("3.- Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Escribe la tarea: ")
            mi_gestor.agregar_tarea(tarea)

        elif opcion == "2":
            mi_gestor.mostrar_tareas()

        elif opcion == "3":
            print("Saliendo del gestor de tareas")
            break
        else:
            print("Opción no valida. Intenta de nuevo")
if __name__=="__main__":
    main()
