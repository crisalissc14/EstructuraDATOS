#Implementar el algoritmo de ordenamiento Quicksort.
#Probar el algoritmo utilizando diferentes conjuntos de datos y verificar su correcta funcionalidad.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivote = arr[-1]
    menores = []
    mayores = []
    
    for elemento in arr[:-1]:
        if elemento <= pivote:
            menores.append(elemento)
        else:
            mayores.append(elemento)
    
    menores_ordenados = quicksort(menores)
    mayores_ordenados = quicksort(mayores)
    
    return menores_ordenados + [pivote] + mayores_ordenados

# Solicitar al usuario la lista de números
lista_numeros = input("Ingrese la lista de números separados por espacios: ").split()
# Convertir los elementos de la lista a enteros
numeros = [int(num) for num in lista_numeros]

print("Lista original:", numeros)

numeros_ordenados = quicksort(numeros)
print("Lista ordenada:", numeros_ordenados)

