import itertools

def encontrar_combinaciones(nums, k):
    combinaciones = []
    
    # Obtener todas las combinaciones de tamaño k permitiendo repeticiones
    for combinacion in itertools.combinations_with_replacement(nums, k):
        combinaciones.append(combinacion)
    
    return combinaciones

# Ejemplo de uso
nums = [4, 5, 7]
k = 2

# Encontrar todas las combinaciones de tamaño k permitiendo repeticiones
combinaciones = encontrar_combinaciones(nums, k)

# Imprimir las combinaciones encontradas
for combinacion in combinaciones:
    print(combinacion)
