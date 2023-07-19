import itertools

def encontrar_permutaciones(nums):
    # Utilizamos la función permutations del módulo itertools para obtener todas las permutaciones
    permutaciones = list(itertools.permutations(nums))
    
    # Convertimos las permutaciones de tuplas a listas
    permutaciones = [list(perm) for perm in permutaciones]
    
    return permutaciones

# Ejemplo de uso
nums = [4, 9, 7]

# Encontrar todas las posibles permutaciones de los números
permutaciones = encontrar_permutaciones(nums)

# Imprimir las permutaciones encontradas
for perm in permutaciones:
    print(perm)
