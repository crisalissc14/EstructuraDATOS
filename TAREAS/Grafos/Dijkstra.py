import heapq

def dijkstra(graph, start):
    # Inicializar distancias a infinito para todos los nodos excepto el nodo inicial
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Cola de prioridad para almacenar los nodos y sus distancias
    priority_queue = [(0, start)]

    while priority_queue:
        # Extraer el nodo con la menor distancia actual
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si la distancia extraída es mayor que la distancia almacenada, ignorar el nodo
        if current_distance > distances[current_node]:
            continue

        # Recorrer los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Si se encuentra un camino más corto, actualizar la distancia
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Ejemplo de uso

# Definir el grafo como un diccionario de listas de adyacencia
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 6, 'D': 1},
    'C': {'A': 5, 'B': 6, 'D': 2},
    'D': {'B': 1, 'C': 2}
}
''' Resultado en la terminal:
Distancia mínima desde A hasta A: 0
Distancia mínima desde A hasta B: 2
Distancia mínima desde A hasta C: 5
Distancia mínima desde A hasta D: 3
'''
start_node = 'A'
distances = dijkstra(graph, start_node)

# Mostrar el resultado en la terminal
for node, distance in distances.items():
    print(f"Distancia mínima desde {start_node} hasta {node}: {distance}")
