import math

def find_asymptotic_notation(f, g, n_range):
    for n in n_range:
        if f(n) <= g(n):
            return "O(g(n))"
    return "O(f(n))"

def function_f(n):
    return 3 * n ** 2 + 2 * n + 1

def function_g(n):
    return 5 * n * math.log2(n) + 10

n_range = range(1, 1001)  # Rango de valores de n para analizar

result = find_asymptotic_notation(function_f, function_g, n_range)
print(f"La notación asintótica de f(n) = 3n^2 + 2n + 1 y g(n) = 5nlog(n) + 10 es: {result}")
