import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 101)  # Valores de n del 1 al 100

# Función cuadrática: g(n) = n^2
g_n = n ** 2

# Función logarítmica: h(n) = n * log(n)
h_n = n * np.log2(n)

plt.plot(n, g_n, label='g(n) = n^2')
plt.plot(n, h_n, label='h(n) = n * log(n)')
plt.xlabel('n')
plt.ylabel('Función')
plt.legend()
plt.show()
