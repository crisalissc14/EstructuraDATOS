def find_coin_combinations(coins, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(coins)):
            if target - coins[i] >= 0:
                backtrack(i, target - coins[i], path + [coins[i]])

    result = []
    coins.sort()  # Ordenar las monedas para evitar duplicados en las combinaciones
    backtrack(0, target, [])
    return result

# Ejemplo de uso:
coins = [1, 3, 7]
target =6
print(find_coin_combinations(coins, target))
