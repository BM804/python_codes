"""Cluster two-dimensional points with a small k-means implementation."""
from math import dist

def kmeans(points: list[tuple[float, float]], k: int, steps: int = 20):
    if not points or not 1 <= k <= len(points):
        raise ValueError("k must be between 1 and the number of points")
    centers = list(points[:k])
    for _ in range(steps):
        groups = [[] for _ in centers]
        for point in points:
            closest = min(range(k), key=lambda index: dist(point, centers[index]))
            groups[closest].append(point)
        updated = [
            tuple(sum(point[axis] for point in group) / len(group) if group else centers[i][axis]
                  for axis in (0, 1))
            for i, group in enumerate(groups)
        ]
        if updated == centers:
            break
        centers = updated
    return centers, groups

if __name__ == "__main__":
    sample = [(1, 2), (2, 1), (8, 9), (9, 8)]
    print(kmeans(sample, 2))
