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

# Menú interactivo
def menu():
    while True:
        cadena = input("\nIngresa una cadena para verificar si los paréntesis están balanceados (o escribe 'salir' para terminar): ").strip()
        if cadena.lower() == 'salir':
            print("Programa finalizado.")
            break
        if esta_balanceado(cadena):
            print("La cadena tiene los paréntesis balanceados.")
        else:
            print("La cadena NO tiene los paréntesis balanceados.")

menu()
