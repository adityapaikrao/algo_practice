from collections import deque

def TopoSort_dfs(adj, V):
    topo_order = []
    visited = [False for _ in range(V)]

    def dfs(node):
        nonlocal visited, topo_order

        visited[node] = True

        for nbr in adj[node]:
            if not visited[nbr]:
                dfs(nbr)
        
        topo_order.append(node)

    for start_node in range(V):
        if visited[start_node]: continue
        
        dfs(start_node)
    
    return topo_order[::-1]

def TopoSort_bfs(edges, V):
    in_degree = [0] * V
    adj = [[] for _ in range(V)]
    ordering = []

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    
    q = deque([])
    for u in range(V):
        if in_degree[u] == 0: q.append(u)
    
    while q:
        node = q.popleft()
        ordering.append(node)

        for nbr in adj[node]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                q.append(nbr)

    return ordering


if  __name__ == "__main__":
    edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]
    V = 6

    adj = [[] for _ in range(V)]

    for u, v in edges:
        adj[u].append(v)
    
    print(TopoSort_dfs(adj, V))
    print(TopoSort_bfs(edges, V))