def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Lista de números
numbers = [9, 2, 5, 1, 7]

print("Lista antes de la ordenación:", numbers)
selection_sort(numbers)
print("Lista después de la ordenación:", numbers)
