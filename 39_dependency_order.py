"""Resolve dependencies before a target package with cycle detection."""
def resolve(graph: dict[str, list[str]], target: str) -> list[str]:
    ordered = []
    visiting = set()
    visited = set()

    def visit(package: str):
        if package in visiting:
            raise ValueError(f"Dependency cycle detected at {package}")
        if package in visited:
            return
        visiting.add(package)
        for dependency in graph.get(package, []):
            visit(dependency)
        visiting.remove(package)
        visited.add(package)
        ordered.append(package)

    visit(target)
    return ordered[:-1]

if __name__ == "__main__":
    dependencies = {"app": ["ui", "db"], "ui": ["http"], "db": ["http"]}
    print(resolve(dependencies, "app"))
