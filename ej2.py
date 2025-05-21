import tkinter as tk
from tkinter import messagebox

def esta_balanceado(cadena): 
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()

    return len(pila) == 0

def verificar():
    cadena = entrada.get()
    if not cadena.strip():
        messagebox.showwarning("Advertencia", "Por favor, ingresa una cadena.")
        return
    if esta_balanceado(cadena):
        resultado.set("✅ Los paréntesis están balanceados.")
    else:
        resultado.set("❌ Los paréntesis NO están balanceados.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificador de Paréntesis Balanceados")
ventana.geometry("400x200")

# Elementos de la interfaz
tk.Label(ventana, text="Ingresa la cadena:").pack(pady=5)

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

tk.Button(ventana, text="Verificar", command=verificar).pack(pady=10)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
