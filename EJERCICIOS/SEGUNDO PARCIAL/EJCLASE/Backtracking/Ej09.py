import itertools

def encontrar_combinaciones(nums, k):
    # Utilizamos la función combinations del módulo itertools para obtener todas las combinaciones
    combinaciones = list(itertools.combinations(nums, k))
    
    # Convertimos las combinaciones de tuplas a listas
    combinaciones = [list(comb) for comb in combinaciones]
    
    return combinaciones

# Ejemplo de uso
nums = [4, 2, 1, 8, 6]
k = 4

# Encontrar todas las combinaciones de k elementos en el conjunto de números
combinaciones = encontrar_combinaciones(nums, k)

# Imprimir las combinaciones encontradas
for comb in combinaciones:
    print(comb)
