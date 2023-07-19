def encontrar_combinaciones(nums, objetivo):
    resultados = []
    combinacion_actual = []

    # Función auxiliar para realizar el backtracking
    def backtrack(start, objetivo_actual):
        # Si hemos alcanzado el objetivo, agregamos la combinación actual a los resultados
        if objetivo_actual == 0:
            resultados.append(combinacion_actual[:])
            return
        
        # Si el objetivo actual es menor a 0, o hemos recorrido todos los números, terminamos la recursión
        if objetivo_actual < 0 or start == len(nums):
            return
        
        # Recorremos todos los números a partir del índice "start"
        for i in range(start, len(nums)):
            # Agregamos el número actual a la combinación actual
            combinacion_actual.append(nums[i])
            
            # Realizamos el backtracking con el nuevo objetivo actualizado
            backtrack(i, objetivo_actual - nums[i])
            
            # Eliminamos el último número agregado para explorar otras posibilidades
            combinacion_actual.pop()
    
    # Iniciamos el backtracking desde el primer número con el objetivo inicial
    backtrack(0, objetivo)
    
    return resultados

# Ejemplo de uso
nums = [1, 5, 8, 4]
objetivo = 5

# Encontrar todas las combinaciones de números que sumen al objetivo
combinaciones = encontrar_combinaciones(nums, objetivo)

# Imprimir las combinaciones encontradas
for combinacion in combinaciones:
    print(combinacion)
