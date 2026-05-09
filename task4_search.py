from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS
def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

# DFS
def dfs(start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(neighbor, goal, path)
            if new_path:
                return new_path

print("BFS Path:", bfs('A', 'F'))
print("DFS Path:", dfs('A', 'F'))