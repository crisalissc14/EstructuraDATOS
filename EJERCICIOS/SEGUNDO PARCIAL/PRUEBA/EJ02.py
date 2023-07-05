def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        max_index = i
        
        # Encuentra el índice del elemento máximo en el subarreglo no ordenado
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        
        # Intercambia el elemento máximo con el último elemento no ordenado
        arr[i], arr[max_index] = arr[max_index], arr[i]
    
    return arr

# Ejemplo de uso
arr = [6, 3, 1, 7, 8, 4]
sorted_arr = selection_sort(arr)
print(sorted_arr)

