def radixSort(arr):
    # Encontrar el máximo valor en la lista
    max_val = max(arr)

    # Realizar el ordenamiento por cada dígito
    exp = 1
    while max_val // exp > 0:
        countingSort(arr, exp)
        exp *= 10

def countingSort(arr, exp):
    base = 10  # Base decimal

    n = len(arr)
    count = [0] * base  # Inicializar contador

    # Contar la frecuencia de los dígitos
    for num in arr:
        digit = (num // exp) % base
        count[digit] += 1

    # Calcular las posiciones finales de los dígitos
    for i in range(1, base):
        count[i] += count[i - 1]

    # Construir el arreglo ordenado
    sorted_arr = [0] * n
    for num in reversed(arr):
        digit = (num // exp) % base
        sorted_arr[count[digit] - 1] = num
        count[digit] -= 1

    # Actualizar la lista original con el arreglo ordenado
    for i in range(n):
        arr[i] = sorted_arr[i]

# Ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print(arr)
