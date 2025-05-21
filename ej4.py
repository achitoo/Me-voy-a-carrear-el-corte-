class Elemento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def encolar(self, nombre, prioridad):
        try:
            prioridad = int(prioridad)
            if prioridad < 0:
                print("La prioridad debe ser un número entero positivo.")
                return
        except ValueError:
            print("Prioridad inválida. Debe ser un número entero.")
            return

        nuevo = Elemento(nombre.strip(), prioridad)
        self.cola.append(nuevo)
        self.cola.sort(key=lambda x: x.prioridad)  # Ordena por prioridad ascendente
        print(f"Elemento encolado: {nuevo}")

    def desencolar(self):
        if not self.cola:
            print("La cola está vacía.")
            return
        elemento = self.cola.pop(0)
        print(f"Elemento desencolado: {elemento}")

    def mostrar_cola(self):
        if not self.cola:
            print("La cola está vacía.")
            return
        print("\nCola de Prioridad:")
        for i, elem in enumerate(self.cola, start=1):
            print(f"{i}. {elem}")
        print()

# Menú interactivo
def menu():
    cola = ColaPrioridad()
    while True:
        print("\n--- MENÚ ---")
        print("1. Encolar elemento")
        print("2. Desencolar elemento")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            nombre = input("Ingresa el nombre del elemento: ").strip()
            prioridad = input("Ingresa la prioridad (entero): ").strip()
            if nombre:
                cola.encolar(nombre, prioridad)
            else:
                print("El nombre no puede estar vacío.")
        elif opcion == "2":
            cola.desencolar()
        elif opcion == "3":
            cola.mostrar_cola()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Ingresa un número del 1 al 4.")

menu()
