import tkinter as tk
from tkinter import messagebox

def invertir_frase():
    frase = entrada.get()
    if not frase.strip():
        messagebox.showwarning("Error", "¡Ingresa una frase primero!")
        return
    
    pila = frase.split()
    frase_invertida = " ".join([pila.pop() for _ in range(len(pila))])
    resultado.config(text=f"Frase invertida: {frase_invertida}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Inversor de Frases")

# Widgets
tk.Label(ventana, text="Ingresa una frase:").pack(pady=5)
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

tk.Button(ventana, text="Invertir", command=invertir_frase).pack(pady=5)
resultado = tk.Label(ventana, text="", fg="blue")
resultado.pack(pady=10)

ventana.mainloop()