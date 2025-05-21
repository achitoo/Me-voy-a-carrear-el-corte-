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

        while actual:
            if actual.valor == valor:
                return f"Valor {valor} encontrado en la posición {posicion}."
            actual = actual.siguiente
            posicion += 1

        return f"El valor {valor} no está en la lista."

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar(1)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

# Búsqueda en la lista
valor_a_buscar = int(input("Ingrese el valor a buscar: "))
resultado = lista.buscar(valor_a_buscar)
print(resultado)