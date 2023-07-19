def encontrar_subconjuntos(nums):
    subconjuntos = []
    n = len(nums)

    # Generar todos los subconjuntos posibles
    for i in range(2**n):
        subconjunto = []
        for j in range(n):
            # Verificar si el bit correspondiente está activado
            if (i >> j) & 1:
                subconjunto.append(nums[j])
        
        # Agregar el subconjunto a la lista
        subconjuntos.append(subconjunto)
    
    return subconjuntos

# Ejemplo de uso
nums = [0, 4, 9]

# Encontrar todos los subconjuntos sin duplicados
subconjuntos = encontrar_subconjuntos(nums)

# Imprimir los subconjuntos encontrados
for subconjunto in subconjuntos:
    print(subconjunto)
