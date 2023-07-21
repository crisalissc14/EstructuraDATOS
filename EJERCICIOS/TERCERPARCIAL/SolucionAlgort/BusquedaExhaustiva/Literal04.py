def find_paths(maze):
    def backtrack(x, y, path):
        if x == len(maze[0]) - 1 and y == len(maze) - 1:
            result.append(path)
            return
        if x + 1 < len(maze[0]) and not maze[y][x + 1]:
            backtrack(x + 1, y, path + [(x + 1, y)])
        if y + 1 < len(maze) and not maze[y + 1][x]:
            backtrack(x, y + 1, path + [(x, y + 1)])

    result = []
    backtrack(0, 0, [(3, 4)])
    return result

# Ejemplo de uso:
maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(find_paths(maze))
