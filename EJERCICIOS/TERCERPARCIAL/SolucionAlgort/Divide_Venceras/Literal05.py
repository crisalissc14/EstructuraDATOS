import random

def quickselect(arr, k):
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))

# Ejemplo de uso:
arr = [3, 7, 1, 9, 4, 2, 8, 6, 5]
k = 5
k_smallest = quickselect(arr, k)
print("Elemento k-ésimo más pequeño:", k_smallest)
