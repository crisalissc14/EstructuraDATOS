def encontrar_minimo(arbol):
    while arbol.izquierdo:
        arbol = arbol.izquierdo
    return arbol

def eliminar_valor(arbol, valor):
    if arbol is None:
        return None
    
    if valor < arbol.valor:
        arbol.izquierdo = eliminar_valor(arbol.izquierdo, valor)
    elif valor > arbol.valor:
        arbol.derecho = eliminar_valor(arbol.derecho, valor)
    else:
        if arbol.izquierdo is None:
            return arbol.derecho
        elif arbol.derecho is None:
            return arbol.izquierdo
        else:
            minimo = encontrar_minimo(arbol.derecho)
            arbol.valor = minimo.valor
            arbol.derecho = eliminar_valor(arbol.derecho, minimo.valor)
    
    return arbol
