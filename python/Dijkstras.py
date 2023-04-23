import heapq

def dijkstra(graph, start):
    # Initialize distances and visited list
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    # Initialize priority queue with start vertex
    pq = [(0, start)]

    while pq:
        # Pop vertex with smallest distance
        (current_distance, current_vertex) = heapq.heappop(pq)

        # Ignore if already visited
        if current_vertex in visited:
            continue

        # Mark vertex as visited
        visited.add(current_vertex)

        # Update distances of neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
print(dijkstra(graph,start))