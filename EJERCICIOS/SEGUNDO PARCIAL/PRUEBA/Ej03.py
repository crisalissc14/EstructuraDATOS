def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Ejemplo de uso
lista = [0, 3, 9, 1, 7, 5]
lista_ordenada = quicksort(lista)
print(lista_ordenada)
