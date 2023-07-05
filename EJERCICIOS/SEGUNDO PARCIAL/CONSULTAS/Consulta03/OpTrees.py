# Creación del árbol
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Creando un árbol con un nodo raíz de valor 5
raiz = NodoArbol(5)

# Inserción de nodos
def insertar_nodo(arbol, clave):
    if arbol is None:
        return NodoArbol(clave)
    if clave < arbol.valor:
        arbol.izquierda = insertar_nodo(arbol.izquierda, clave)
    elif clave > arbol.valor:
        arbol.derecha = insertar_nodo(arbol.derecha, clave)
    return arbol

# Insertando un nodo con valor 3
raiz = insertar_nodo(raiz, 3)

# Eliminación de nodos
def encontrar_nodo_valor_minimo(nodo):
    actual = nodo
    while actual.izquierda is not None:
        actual = actual.izquierda
    return actual

def eliminar_nodo(raiz, clave):
    if raiz is None:
        return raiz
    if clave < raiz.valor:
        raiz.izquierda = eliminar_nodo(raiz.izquierda, clave)
    elif clave > raiz.valor:
        raiz.derecha = eliminar_nodo(raiz.derecha, clave)
    else:
        if raiz.izquierda is None:
            return raiz.derecha
        elif raiz.derecha is None:
            return raiz.izquierda
        temp = encontrar_nodo_valor_minimo(raiz.derecha)
        raiz.valor = temp.valor
        raiz.derecha = eliminar_nodo(raiz.derecha, temp.valor)
    return raiz

# Eliminando un nodo con valor 3
raiz = eliminar_nodo(raiz, 3)

# Recorridos del árbol
def recorrido_en_orden(arbol):
    if arbol:
        recorrido_en_orden(arbol.izquierda)
        print(arbol.valor)
        recorrido_en_orden(arbol.derecha)

# Recorrido en orden del árbol
recorrido_en_orden(raiz)

def recorrido_preorden(arbol):
    if arbol:
        print(arbol.valor)
        recorrido_preorden(arbol.izquierda)
        recorrido_preorden(arbol.derecha)

# Recorrido preorden del árbol
recorrido_preorden(raiz)

def recorrido_postorden(arbol):
    if arbol:
        recorrido_postorden(arbol.izquierda)
        recorrido_postorden(arbol.derecha)
        print(arbol.valor)

# Recorrido postorden del árbol
recorrido_postorden(raiz)

# Balanceo del árbol
def balancear_arbol(arbol):
    # Implementación del algoritmo de balanceo del árbol
    ...

# Balanceando el árbol
raiz = balancear_arbol(raiz)
