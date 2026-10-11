"""
Forld-Fulkerson algorithm for computing the maximum flow in a flow network.
"""

def ford_fulkerson(capacity: list[list[int]], source: int, sink: int):
    residual = [row[:] for row in capacity]
    V = len(capacity)

    def dfs(u, residual, flow):
        if u == sink:
            return flow

        visited.add(u)
        for v in range(V):
            if v in visited or residual[u][v] == 0: 
                continue

            new_flow = min(flow, residual[u][v])

            pushed = dfs(v, residual, new_flow)
            if pushed > 0:
                residual[u][v] -= pushed
                residual[v][u] += pushed
                return pushed
        
        return 0

    max_flow = 0
    while True:
        visited = set()
        
        pushed = dfs(source, residual, float('inf'))
        if pushed == 0: 
            break

        max_flow += pushed

    return max_flow
        