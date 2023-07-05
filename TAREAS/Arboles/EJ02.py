def buscar_valor(arbol, valor):
    if arbol is None:
        return False
    
    if arbol.valor == valor:
        return True
    
    return buscar_valor(arbol.izquierdo, valor) or buscar_valor(arbol.derecho, valor)
