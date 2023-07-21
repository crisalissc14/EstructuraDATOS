def find_combinations(nums, k):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path)
            return
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    result = []
    backtrack(0, [])
    return result

# Ejemplo de uso:
nums = [2, 3, 4, 5]
k = 3
print(find_combinations(nums, k))
