import itertools

def encontrar_subconjuntos(nums, objetivo):
    subconjuntos = []
    
    # Iteramos sobre todas las posibles combinaciones de números
    for r in range(len(nums) + 1):
        for comb in itertools.combinations(nums, r):
            # Calculamos el producto de cada combinación
            producto = 1
            for num in comb:
                producto *= num
            
            # Verificamos si el producto es múltiplo del objetivo
            if producto % objetivo == 0:
                subconjuntos.append(list(comb))
    
    return subconjuntos

# Ejemplo de uso
nums = [1, 2, 3, 4, 5]
objetivo = 4

# Encontrar todos los subconjuntos cuyo producto sea múltiplo de 6
subconjuntos = encontrar_subconjuntos(nums, objetivo)

# Imprimir los subconjuntos encontrados
for subconjunto in subconjuntos:
    print(subconjunto)
