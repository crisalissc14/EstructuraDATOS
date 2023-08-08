import matplotlib.pyplot as plt

def recurrence_tree(n):
    levels = 0
    while n > 1:
        n //= 2
        levels += 1
    return levels

n_values = list(range(1, 17))
result = []

for n in n_values:
    result.append(recurrence_tree(n))

plt.plot(n_values, result, marker='o')
plt.xlabel('n')
plt.ylabel('Number of Levels')
plt.title('Recurrence Tree Method')
plt.grid(True)
plt.show()

