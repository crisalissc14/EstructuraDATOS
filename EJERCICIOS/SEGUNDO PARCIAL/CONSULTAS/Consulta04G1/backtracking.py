def es_valido(tablero, fila, col):
    # Verificar si una reina en la posición (fila, col) es atacada por otras reinas

    # Verificar la fila actual
    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    # Verificar la diagonal superior izquierda
    i, j = fila, col
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verificar la diagonal inferior izquierda
    i, j = fila, col
    while i < len(tablero) and j >= 0:
        if tablero[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def resolver_n_reinas(tablero, col):
    # Caso base: si todas las reinas están colocadas
    if col >= len(tablero):
        return True

    # Recorrer todas las filas en la columna actual
    for fila in range(len(tablero)):
        if es_valido(tablero, fila, col):
            # Colocar una reina en la posición (fila, col)
            tablero[fila][col] = 1

            # Llamar recursivamente para colocar las reinas restantes
            if resolver_n_reinas(tablero, col + 1):
                return True

            # Si no se encontró una solución, retroceder (backtrack) y probar otra opción
            tablero[fila][col] = 0

    # Si no se encuentra ninguna solución válida
    return False

def n_reinas(n):
    # Crear un tablero vacío de NxN
    tablero = [[0] * n for _ in range(n)]

    # Llamar a la función recursiva para resolver el problema
    if resolver_n_reinas(tablero, 0):
        # Imprimir la solución encontrada
        for fila in tablero:
            print(fila)
    else:
        print("No se encontró ninguna solución para", n, "reinas.")

# Ejemplo de uso
n_reinas(4)