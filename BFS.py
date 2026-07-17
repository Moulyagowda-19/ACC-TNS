from collections import deque
def bfs(graph,start):
    visited = {start}
    queue= deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in graph[node]: #nbr = neighbor
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return order
graph = {
    'A':['B','C'],
    'B':['A','D','F'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E'],
}
print(bfs(graph,'F'))