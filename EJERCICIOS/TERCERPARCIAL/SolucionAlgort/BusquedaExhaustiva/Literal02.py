def find_permutations(string):
    def backtrack(path):
        if len(path) == len(string):
            result.append(path)
            return
        for char in string:
            if char not in path:
                backtrack(path + char)

    result = []
    backtrack('')
    return result

# Ejemplo de uso:
string = "ACI"
print(find_permutations(string))
