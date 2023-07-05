# Función para obtener la altura de un nodo
def obtener_altura(nodo):
    if nodo is None:
        return 0
    return max(obtener_altura(nodo.izquierda), obtener_altura(nodo.derecha)) + 1

# Función para realizar una rotación simple a la izquierda
def rotacion_izquierda(nodo):
    nueva_raiz = nodo.derecha
    nodo.derecha = nueva_raiz.izquierda
    nueva_raiz.izquierda = nodo
    return nueva_raiz

# Función para realizar una rotación simple a la derecha
def rotacion_derecha(nodo):
    nueva_raiz = nodo.izquierda
    nodo.izquierda = nueva_raiz.derecha
    nueva_raiz.derecha = nodo
    return nueva_raiz

# Función para balancear un nodo
def balancear_nodo(nodo):
    if nodo is None:
        return nodo

    altura_izquierda = obtener_altura(nodo.izquierda)
    altura_derecha = obtener_altura(nodo.derecha)
    factor_equilibrio = altura_izquierda - altura_derecha

    # Caso de desequilibrio a la izquierda
    if factor_equilibrio > 1:
        if obtener_altura(nodo.izquierda.izquierda) >= obtener_altura(nodo.izquierda.derecha):
            nodo = rotacion_derecha(nodo)
        else:
            nodo.izquierda = rotacion_izquierda(nodo.izquierda)
            nodo = rotacion_derecha(nodo)

    # Caso de desequilibrio a la derecha
    elif factor_equilibrio < -1:
        if obtener_altura(nodo.derecha.derecha) >= obtener_altura(nodo.derecha.izquierda):
            nodo = rotacion_izquierda(nodo)
        else:
            nodo.derecha = rotacion_derecha(nodo.derecha)
            nodo = rotacion_izquierda(nodo)

    return nodo
