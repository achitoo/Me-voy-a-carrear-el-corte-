import os

class Cancion:
    def __init__(self, titulo):
        self.titulo = titulo
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.actual = None
        self.primera = None
        self.ultima = None

    def agregar_cancion(self, titulo):
        if not titulo.strip():
            print("El título no puede estar vacío.")
            return
        nueva = Cancion(titulo.strip())
        if not self.primera:
            self.primera = self.ultima = self.actual = nueva
        else:
            self.ultima.siguiente = nueva
            nueva.anterior = self.ultima
            self.ultima = nueva
        print(f"Canción agregada: {titulo.strip()}")

    def eliminar_cancion(self, titulo):
        if not self.primera:
            print("La lista está vacía.")
            return
        if not titulo.strip():
            print("El título no puede estar vacío.")
            return
        temp = self.primera
        while temp:
            if temp.titulo.lower() == titulo.lower():
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primera = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                else:
                    self.ultima = temp.anterior
                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior
                print(f"✅ Canción eliminada: {titulo}")
                return
            temp = temp.siguiente
        print("Canción no encontrada.")

    def siguiente_cancion(self):
        if not self.actual:
            print("No hay canciones en la lista.")
        elif self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Reproduciendo: {self.actual.titulo}")
        else:
            print("Ya estás en la última canción.")

    def anterior_cancion(self):
        if not self.actual:
            print("No hay canciones en la lista.")
        elif self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Reproduciendo: {self.actual.titulo}")
        else:
            print("Ya estás en la primera canción.")

    def mostrar_lista(self):
        if not self.primera:
            print("\nLa lista de reproducción está vacía.\n")
            return
        temp = self.primera
        print("\nLista de Reproducción:")
        while temp:
            marcador = "->" if temp == self.actual else "  "
            print(f"{marcador} {temp.titulo}")
            temp = temp.siguiente
        print()

def menu():
    playlist = ListaReproduccion()
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente canción")
        print("4. Reproducir canción anterior")
        print("5. Mostrar lista de reproducción")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            titulo = input("Ingresa el título de la canción: ")
            playlist.agregar_cancion(titulo)
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "2":
            titulo = input("Ingresa el título de la canción a eliminar: ")
            playlist.eliminar_cancion(titulo)
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "3":
            playlist.siguiente_cancion()
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "4":
            playlist.anterior_cancion()
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "5":
            playlist.mostrar_lista()
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Ingresa un número del 1 al 6.")

menu()
