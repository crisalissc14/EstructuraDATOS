def resolver_sudoku(sudoku):
    # Definir la función para verificar si un número es válido en una posición específica
    def es_valido(sudoku, fila, columna, num):
        # Verificar si el número ya está presente en la fila
        if num in sudoku[fila]:
            return False
        
        # Verificar si el número ya está presente en la columna
        for i in range(9):
            if sudoku[i][columna] == num:
                return False
        
        # Verificar si el número ya está presente en el bloque 3x3
        start_row = fila - fila % 3
        start_col = columna - columna % 3
        for i in range(3):
            for j in range(3):
                if sudoku[start_row + i][start_col + j] == num:
                    return False
        
        # Si el número no se encuentra en ninguna posición conflictiva, es válido
        return True

    # Definir la función para encontrar la próxima celda vacía
    def encontrar_celda_vacia(sudoku):
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return i, j
        return None, None

    # Definir la función principal de backtracking
    def backtracking(sudoku):
        fila, columna = encontrar_celda_vacia(sudoku)

        # Verificar si se ha llenado todo el tablero
        if fila is None:
            return True

        # Probar todos los números pares del 2 al 8 en la celda vacía actual
        for num in range(2, 10, 2):
            if es_valido(sudoku, fila, columna, num):
                sudoku[fila][columna] = num

                # Llamar recursivamente a la función para la siguiente celda vacía
                if backtracking(sudoku):
                    return True

                # Si no se encuentra ninguna solución, retroceder y probar el siguiente número
                sudoku[fila][columna] = 0

        # Si se han probado todos los números sin éxito, retornar False
        return False

    # Llamar a la función de backtracking para resolver el Sudoku
    if backtracking(sudoku):
        # Imprimir el Sudoku resuelto
        for fila in sudoku:
            print(fila)
    else:
        print("No se encontró solución para el Sudoku.")

# Ejemplo de Sudoku parcialmente completado con números pares
sudoku = [
    [0, 0, 2, 0, 0, 6, 4, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 6],
    [0, 2, 0, 0, 0, 0, 0, 6, 0],
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 6, 0, 0, 0, 2, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 1, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 2, 0, 0, 7, 0, 0]
]

# Resolver el Sudoku utilizando el algoritmo de Backtracking
resolver_sudoku(sudoku)

