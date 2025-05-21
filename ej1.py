#o	Ejercicio #1: Inversión de palabras en una frase. 
#   Desarrolle un programa que utilice una pila para invertir el orden de las palabras
#   en una frase dada.
#   Por ejemplo, la frase "Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola".

def invertir_frase():
    # Pedir al usuario que ingrese una oración
    frase = input("Ingresa una oración: ")
    
    # Dividir la oración en palabras y almacenarlas en una pila
    pila = frase.split()
    
    # Extraer las palabras desde la pila para invertir el orden
    frase_invertida = []
    while pila:
        frase_invertida.append(pila.pop())  # Sacamos cada palabra en orden inverso
    
    # Mostrar el resultado al usuario
    print("Oración invertida:", " ".join(frase_invertida))

# Ejecutar la función
invertir_frase()