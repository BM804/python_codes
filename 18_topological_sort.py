"""Topologically order a directed acyclic graph with Kahn's algorithm."""
from collections import deque

def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    nodes = set(graph)
    for neighbors in graph.values():
        nodes.update(neighbors)
    indegree = {node: 0 for node in nodes}
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1
    queue = deque(node for node in nodes if indegree[node] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(nodes):
        raise ValueError("Graph contains a cycle")
    return order

if __name__ == "__main__":
    print(topological_sort({"compile": ["test"], "test": ["ship"], "docs": ["ship"]}))
