import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0
        posiciones = []

        while actual:
            if actual.valor == valor:
                posiciones.append(posicion)
            actual = actual.siguiente
            posicion += 1

        if posiciones:
            if len(posiciones) > 1:
                return f"Valor {valor} encontrado en las posiciones: {', '.join(map(str, posiciones))}. Se encuentra repetido."
            else:
                return f"Valor {valor} encontrado en la posición {posiciones[0]}."
        else:
            return f"El valor {valor} no está en la lista."

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return elementos if elementos else ["(Lista vacía)"]

# Interfaz gráfica
class InterfazLista:
    def __init__(self, root):
        self.lista = ListaEnlazada()
        self.root = root
        root.title("Lista Enlazada")
        root.geometry("400x400")

        self.entry_valor = tk.Entry(root, width=30)
        self.entry_valor.pack(pady=5)
        self.entry_valor.insert(0, "Ingrese valor entero")

        tk.Button(root, text="Insertar", command=self.insertar).pack(pady=2)
        tk.Button(root, text="Buscar", command=self.buscar).pack(pady=2)
        tk.Button(root, text="Mostrar Lista", command=self.mostrar).pack(pady=2)

        self.lista_box = tk.Listbox(root, width=40, height=10)
        self.lista_box.pack(pady=10)

    def insertar(self):
        valor = self.entry_valor.get().strip()
        if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
            self.lista.insertar(int(valor))
            messagebox.showinfo("Insertado", f"Se insertó el valor: {valor}")
            self.mostrar()
        else:
            messagebox.showerror("Error", "Debe ingresar un número entero válido.")

    def buscar(self):
        valor = self.entry_valor.get().strip()
        if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
            resultado = self.lista.buscar(int(valor))
            messagebox.showinfo("Búsqueda", resultado)
        else:
            messagebox.showerror("Error", "Debe ingresar un número entero válido.")

    def mostrar(self):
        self.lista_box.delete(0, tk.END)
        for item in self.lista.mostrar():
            self.lista_box.insert(tk.END, item)

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazLista(root)
    root.mainloop()