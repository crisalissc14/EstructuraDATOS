def encontrar_subconjuntos_rango(nums, rango_min, rango_max):
    resultados = []
    
    # Función auxiliar para generar todos los subconjuntos
    def generar_subconjuntos(nums, indice, suma_actual, conjunto_actual):
        # Si la suma actual está dentro del rango dado, agregamos el subconjunto a los resultados
        if rango_min <= suma_actual <= rango_max:
            resultados.append(conjunto_actual[:])
        
        # Generar subconjuntos recursivamente
        for i in range(indice, len(nums)):
            num = nums[i]
            conjunto_actual.append(num)
            generar_subconjuntos(nums, i + 1, suma_actual + num, conjunto_actual)
            conjunto_actual.pop()
    
    # Llamar a la función auxiliar con el conjunto vacío, índice inicial y suma inicial igual a cero
    generar_subconjuntos(nums, 0, 0, [])
    
    return resultados

# Ejemplo de uso
nums = [5, 6, 7, 8, 9]
rango_min = 4
rango_max = 8

# Encontrar todos los subconjuntos cuya suma esté dentro del rango dado
subconjuntos = encontrar_subconjuntos_rango(nums, rango_min, rango_max)

# Imprimir los subconjuntos encontrados
for subconjunto in subconjuntos:
    print(subconjunto)
