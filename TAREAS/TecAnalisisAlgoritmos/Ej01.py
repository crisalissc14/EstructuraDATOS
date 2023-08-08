def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Lista ordenada de ejemplo
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Elemento a buscar
elemento_buscado = 13

# Búsqueda binaria
indice_binario = busqueda_binaria(lista_ordenada, elemento_buscado)
if indice_binario != -1:
    print(f"El elemento {elemento_buscado} fue encontrado en la posición {indice_binario} (búsqueda binaria)")
else:
    print(f"El elemento {elemento_buscado} no fue encontrado")

# Búsqueda lineal
indice_lineal = busqueda_lineal(lista_ordenada, elemento_buscado)
if indice_lineal != -1:
    print(f"El elemento {elemento_buscado} fue encontrado en la posición {indice_lineal} (búsqueda lineal)")
else:
    print(f"El elemento {elemento_buscado} no fue encontrado")
