def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for nbr in graph [start]:
        if nbr not in visited:
            order += dfs(
                graph,nbr,visited)
    return order
graph = {
    'A':['B','C'],
    'B':['A','D','F'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E'],
}
print(dfs(graph,'C'))