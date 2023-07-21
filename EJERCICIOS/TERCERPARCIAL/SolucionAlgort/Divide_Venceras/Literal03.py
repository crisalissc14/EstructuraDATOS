def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return None

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    if len(A) == 1 and len(A[0]) == 1 and len(B) == 1 and len(B[0]) == 1:
        result[0][0] = A[0][0] * B[0][0]
        return result

    a, b, c, d = divide_matrix(A)
    e, f, g, h = divide_matrix(B)

    p1 = matrix_multiply(a, subtract_matrix(f, h))
    p2 = matrix_multiply(add_matrix(a, b), h)
    p3 = matrix_multiply(add_matrix(c, d), e)
    p4 = matrix_multiply(d, subtract_matrix(g, e))
    p5 = matrix_multiply(add_matrix(a, d), add_matrix(e, h))
    p6 = matrix_multiply(subtract_matrix(b, d), add_matrix(g, h))
    p7 = matrix_multiply(subtract_matrix(a, c), add_matrix(e, f))

    result = [
        [p5[i][j] + p4[i][j] - p2[i][j] + p6[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]
    for i in range(len(A) // 2):
        for j in range(len(A[0]) // 2):
            result[i][j] = p1[i][j] + p2[i][j]
            result[i][j + len(A[0]) // 2] = p3[i][j]
            result[i + len(A) // 2][j] = p4[i][j]
            result[i + len(A) // 2][j + len(A[0]) // 2] = p5[i][j] + p1[i][j] - p3[i][j] - p7[i][j]

    return result

def divide_matrix(matrix):
    middle = len(matrix) // 2
    a = [row[:middle] for row in matrix[:middle]]
    b = [row[middle:] for row in matrix[:middle]]
    c = [row[:middle] for row in matrix[middle:]]
    d = [row[middle:] for row in matrix[middle:]]
    return a, b, c, d

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Ejemplo de uso:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
print(result)
