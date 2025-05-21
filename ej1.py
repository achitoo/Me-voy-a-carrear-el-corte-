#o	Ejercicio #1: Inversión de palabras en una frase. 
#   Desarrolle un programa que utilice una pila para invertir el orden de las palabras
#   en una frase dada.
#   Por ejemplo, la frase "Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola".
from collections import deque

def invertir_oracion():
    cola = deque()
    oracion = input("Ingresa una oración: ")
    
    # Agregar caracteres a la cola
    for caracter in oracion:
        cola.appendleft(caracter)  # Se inserta al inicio para invertir

    # Construir la oración invertida
    oracion_invertida = ''.join(cola)
    print("Oración invertida:", oracion_invertida)

# Ejecutar la función
invertir_oracion()