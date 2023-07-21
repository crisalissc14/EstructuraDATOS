def find_queen_solutions(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)

    result = []
    board = [-2] * n
    backtrack(0, board)
    return result

# Ejemplo de uso:
n =4
print(find_queen_solutions(n))
