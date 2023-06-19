    # list -> lista ordenada en la que se va buscar
    # target -> numero objetivo 
def interpolation_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high and target >= list[low] and target <= list[high]:
        if low == high:
            if list[low] == target:
                return low
            return -1
# calcular posicion
        pos = low + int(((float(high - low) / (list[high] - list[low])) * (target - list[low])))

        if list[pos] == target:
            return pos

        if list[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Lista con números enteros ordenados
lista = [1, 2, 3,  4, 5, 6, 7, 8, 9, 10, 11, 12]

numero = int(input("Ingrese el numero a buscar: "))

resultado = interpolation_search(lista, numero)
if resultado != -1:
    print("El numero", numero, "se encuentra en la posicion", resultado)
else:
    print("El numero", numero, "no se encuentra en la lista.")