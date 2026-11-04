# Clase para crear los nodos del árbol
class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor


# Se crea el árbol con su raíz
raiz = Nodo(1)

# Se agregan los nodos del segundo nivel
raiz.izq = Nodo(2)
raiz.der = Nodo(3)

# Se agregan los nodos del tercer nivel
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)


# Función para recorrer el árbol en preorden
def print_preorder(raiz):
    if raiz:
        print(raiz.val, end=" ")
        print_preorder(raiz.izq)
        print_preorder(raiz.der)


# Se muestran los números del árbol
print("Recorrido en preorden:")
print_preorder(raiz)