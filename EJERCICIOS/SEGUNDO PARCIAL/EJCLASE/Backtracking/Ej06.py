def encontrar_soluciones_n_reinas(n):
    soluciones = []
    
    # Función auxiliar para verificar si una posición es segura para colocar una reina
    def es_posicion_segura(tablero, fila, columna):
        # Verificar la columna actual
        for i in range(fila):
            if tablero[i] == columna:
                return False
        
        # Verificar las diagonales
        for i in range(fila):
            if abs(tablero[i] - columna) == abs(i - fila):
                return False
        
        return True
    
    # Función auxiliar para realizar el backtracking
    def backtrack(tablero, fila):
        # Caso base: si hemos colocado todas las reinas, agregamos el tablero a las soluciones
        if fila == n:
            soluciones.append(tablero[:])
            return
        
        # Para cada columna en la fila actual, intentamos colocar una reina y llamamos recursivamente al backtracking
        for columna in range(n):
            if es_posicion_segura(tablero, fila, columna):
                tablero[fila] = columna
                backtrack(tablero, fila + 1)
    
    # Llamar al backtracking con un tablero vacío y la primera fila
    backtrack([None] * n, 0)
    
    return soluciones

# Ejemplo de uso
n = 6  # Tamaño del tablero y número de reinas

# Encontrar todas las soluciones para colocar las reinas
soluciones = encontrar_soluciones_n_reinas(n)

# Imprimir las soluciones
for solucion in soluciones:
    print(solucion)
