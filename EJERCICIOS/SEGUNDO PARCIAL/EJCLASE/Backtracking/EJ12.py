import itertools

def encontrar_subconjuntos(nums, k):
    subconjuntos = []
    
    # Obtener todos los subconjuntos de tamaño k
    for subconjunto in itertools.combinations(nums, k):
        subconjuntos.append(subconjunto)
    
    return subconjuntos

# Ejemplo de uso
nums = [1, 2, 3, 4, 5]
k = 4

# Encontrar todos los subconjuntos de tamaño k
subconjuntos = encontrar_subconjuntos(nums, k)

# Imprimir los subconjuntos encontrados
for subconjunto in subconjuntos:
    print(subconjunto)
