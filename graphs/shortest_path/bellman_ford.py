def bellman_ford(edges, V, src):
    """
    Single-Source. Can detect negative cycles. Works with negative edge weights (unlike Dijkstra's)
    """
    dist = [[float('inf')] * V for _ in range(V)]
    dist[0][src] = 0

    for k in range(1, V):
        dist[k] = dist[k-1][:]
        for u, v, w in edges:
            if dist[k][v] > dist[k-1][u] + w:
                dist[k][v] = dist[k-1][u] + w
    
    for u, v, w in edges:
        if dist[k][v] > dist[k][u] + w:
            return [-1] # negative cycle exists
    
    return dist[-1]

    