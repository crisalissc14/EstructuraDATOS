def encontrar_combinaciones(nums, objetivo):
    resultados = []
    
    # Función auxiliar para realizar el backtracking
    def backtrack(comb, index, suma_actual):
        # Si la suma actual es igual al objetivo, añadir la combinación a los resultados
        if suma_actual == objetivo:
            resultados.append(comb[:])
        
        # Explorar las opciones de los números restantes
        for i in range(index, len(nums)):
            # Agregar el número a la combinación y actualizar la suma
            comb.append(nums[i])
            suma_actual += nums[i]
            
            # Llamar recursivamente al backtracking con el siguiente número
            backtrack(comb, i, suma_actual)
            
            # Retroceder: eliminar el número de la combinación y restar su valor a la suma
            comb.pop()
            suma_actual -= nums[i]
    
    # Llamar al backtracking con la combinación vacía y el índice inicial
    backtrack([], 0, 0)
    
    return resultados

# Ejemplo de uso
conjunto = [2, 4, 6, 8]
objetivo = 10

# Encontrar todas las combinaciones de números que sumen al objetivo
resultados = encontrar_combinaciones(conjunto, objetivo)

# Imprimir los resultados
for comb in resultados:
    print(comb)


