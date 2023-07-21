def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verificar si el candidato es el elemento mayoritario
    count = arr.count(candidate)
    if count > len(arr) // 2:
        return candidate
    else:
        return None

# Ejemplo de uso:
arr = [4, 6, 6, 6, 2]
result = majority_element(arr)
print("Elemento mayoritario:", result)
