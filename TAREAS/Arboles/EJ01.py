def contar_nodos(arbol):
    if arbol is None:
        return 0
    
    count = 0
    stack = [arbol]
    
    while stack:
        nodo = stack.pop()
        count += 1
        
        if nodo.izquierdo:
            stack.append(nodo.izquierdo)
        if nodo.derecho:
            stack.append(nodo.derecho)
    
    return count
