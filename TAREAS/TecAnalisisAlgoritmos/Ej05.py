def find_duplicate_pairs(lst):
    duplicate_pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                duplicate_pairs.append((lst[i], lst[j]))
    return duplicate_pairs

# Ejemplo de uso
lista = [3, 2, 4, 1, 2, 5, 4, 6, 3]
duplicates = find_duplicate_pairs(lista)
print("Pares duplicados:", duplicates)
