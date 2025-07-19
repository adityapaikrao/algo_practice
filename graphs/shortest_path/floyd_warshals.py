
def Floyd_Warshal(adj, V):
    """
    adj -> adjacency matrix
    V -> number of vertices
    """
    dist = [[float('inf')] * V for _ in range(V)]
    
    for u in range(V):
        for v in range(V):
            if u == v: dist[u][v] = 0
            elif adj[u][v] is not None: dist[u][v] = adj[u][v]
    
    
    for k in range(V):
        for u in range(V):
            for v in range(V):
                if dist[u][v] > dist[u][k] + dist[k][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]

    for k in range(V):
        for u in range(V):
            for v in range(V):
                if dist[u][v] > dist[u][k] + dist[k][v]:
                    return [-1] # negative cycle
    
    return dist