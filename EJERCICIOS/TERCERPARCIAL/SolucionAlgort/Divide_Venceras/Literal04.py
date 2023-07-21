def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Ejemplo de uso:
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 56
index = binary_search(arr, target)
print("Elemento encontrado en el índice:", index)
