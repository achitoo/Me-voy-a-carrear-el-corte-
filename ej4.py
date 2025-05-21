import tkinter as tk
from tkinter import messagebox

class Elemento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
    def __str__(self): return f"{self.nombre} (Prioridad: {self.prioridad})"

class ColaPrioridad:
    def __init__(self): self.cola = []
    def encolar(self, nombre, prioridad):
        try:
            prioridad = int(prioridad)
            if prioridad < 0: return "Prioridad debe ser positiva"
        except ValueError:
            return "Prioridad inválida"
        if not nombre.strip(): return "Nombre vacío"
        nuevo = Elemento(nombre.strip(), prioridad)
        self.cola.append(nuevo)
        self.cola.sort(key=lambda x: x.prioridad)
        return f"Elemento encolado: {nuevo}"
    def desencolar(self):
        if not self.cola: return "La cola está vacía"
        elemento = self.cola.pop(0)
        return f"Elemento desencolado: {elemento}"
    def mostrar_cola(self):
        if not self.cola: return ["(Cola vacía)"]
        return [str(elem) for elem in self.cola]

class Interfaz:
    def __init__(self, root):
        self.cola = ColaPrioridad()
        self.root = root
        root.title("Cola de Prioridad")
        root.geometry("400x400")

        self.entry_nombre = tk.Entry(root, width=30)
        self.entry_nombre.pack(pady=5)
        self.entry_nombre.insert(0, "Nombre")

        self.entry_prioridad = tk.Entry(root, width=30)
        self.entry_prioridad.pack(pady=5)
        self.entry_prioridad.insert(0, "Prioridad")

        tk.Button(root, text="Encolar", command=self.encolar).pack(pady=2)
        tk.Button(root, text="Desencolar", command=self.desencolar).pack(pady=2)
        tk.Button(root, text="Mostrar Cola", command=self.mostrar).pack(pady=2)

        self.lista = tk.Listbox(root, width=50, height=10)
        self.lista.pack(pady=10)

    def encolar(self):
        nombre = self.entry_nombre.get()
        prioridad = self.entry_prioridad.get()
        resultado = self.cola.encolar(nombre, prioridad)
        messagebox.showinfo("Resultado", resultado)
        self.mostrar()

    def desencolar(self):
        resultado = self.cola.desencolar()
        messagebox.showinfo("Resultado", resultado)
        self.mostrar()

    def mostrar(self):
        self.lista.delete(0, tk.END)
        for item in self.cola.mostrar_cola():
            self.lista.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()