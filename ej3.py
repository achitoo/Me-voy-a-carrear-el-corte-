import tkinter as tk
from tkinter import messagebox

# Nodo de la lista doblemente enlazada
class Cancion:
    def __init__(self, titulo):
        self.titulo = titulo
        self.siguiente = None
        self.anterior = None

# Lista de reproducción
class ListaReproduccion:
    def __init__(self):
        self.primera = None
        self.ultima = None
        self.actual = None

    def agregar_cancion(self, titulo):
        if not titulo.strip():
            return "❌ Título vacío"
        nueva = Cancion(titulo.strip())
        if not self.primera:
            self.primera = self.ultima = self.actual = nueva
        else:
            self.ultima.siguiente = nueva
            nueva.anterior = self.ultima
            self.ultima = nueva
        return f"✅ Canción agregada: {titulo}"

    def eliminar_cancion(self, titulo):
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
                return f"✅ Canción eliminada: {titulo}"
            temp = temp.siguiente
        return "❌ Canción no encontrada"

    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return f"▶ Reproduciendo: {self.actual.titulo}"
        return "ℹ No hay siguiente canción."

    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return f"▶ Reproduciendo: {self.actual.titulo}"
        return "ℹ No hay canción anterior."

    def mostrar_actual(self):
        if self.actual:
            return f"🎵 Actual: {self.actual.titulo}"
        return "ℹ No hay canción actual."

    def mostrar_lista(self):
        temp = self.primera
        canciones = []
        while temp:
            canciones.append(temp.titulo)
            temp = temp.siguiente
        return canciones if canciones else ["(Lista vacía)"]

# Interfaz gráfica con Tkinter
class Interfaz:
    def __init__(self, root):
        self.lista = ListaReproduccion()
        self.root = root
        self.root.title("🎧 Lista de Reproducción")
        self.root.geometry("400x400")

        # Entrada
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Botones
        botones = [
            ("Agregar canción", self.agregar),
            ("Eliminar canción", self.eliminar),
            ("Siguiente", self.siguiente),
            ("Anterior", self.anterior),
            ("Mostrar actual", self.actual),
            ("Mostrar lista", self.mostrar_lista)
        ]

        for texto, comando in botones:
            tk.Button(root, text=texto, command=comando, width=30).pack(pady=2)

        # Área de salida
        self.salida = tk.Listbox(root, width=50, height=10)
        self.salida.pack(pady=10)

    def agregar(self):
        titulo = self.entry.get()
        resultado = self.lista.agregar_cancion(titulo)
        messagebox.showinfo("Agregar", resultado)
        self.entry.delete(0, tk.END)

    def eliminar(self):
        titulo = self.entry.get()
        resultado = self.lista.eliminar_cancion(titulo)
        messagebox.showinfo("Eliminar", resultado)
        self.entry.delete(0, tk.END)

    def siguiente(self):
        resultado = self.lista.siguiente_cancion()
        messagebox.showinfo("Siguiente", resultado)

    def anterior(self):
        resultado = self.lista.anterior_cancion()
        messagebox.showinfo("Anterior", resultado)

    def actual(self):
        resultado = self.lista.mostrar_actual()
        messagebox.showinfo("Actual", resultado)

    def mostrar_lista(self):
        self.salida.delete(0, tk.END)
        for cancion in self.lista.mostrar_lista():
            self.salida.insert(tk.END, cancion)

# Ejecutar GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()