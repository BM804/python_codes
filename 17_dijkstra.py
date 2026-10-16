"""Compute shortest paths in a nonnegative weighted graph."""
import heapq

def dijkstra(graph: dict[str, list[tuple[str, float]]], start: str):
    distances = {start: 0}
    previous = {}
    queue = [(0, start)]
    while queue:
        cost, node = heapq.heappop(queue)
        if cost != distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            if weight < 0:
                raise ValueError("Dijkstra requires nonnegative edge weights")
            candidate = cost + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                previous[neighbor] = node
                heapq.heappush(queue, (candidate, neighbor))
    return distances, previous

if __name__ == "__main__":
    graph = {"A": [("B", 4), ("C", 1)], "C": [("B", 2)], "B": []}
    print(dijkstra(graph, "A")[0])
