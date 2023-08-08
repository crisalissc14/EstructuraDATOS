import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generar una lista de números para ordenar
input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Medir el tiempo de ejecución del algoritmo de ordenamiento por inserción
start_time = time.time()
insertion_sort(input_list)
end_time = time.time()

execution_time = end_time - start_time
print("Tiempo de ejecución de ordenamiento por inserción:", execution_time, "segundos")
